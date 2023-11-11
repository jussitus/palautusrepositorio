import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote


class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()

        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 100

        def varasto_saldo(tuote_id):
            match tuote_id:
                case 1:
                    return 10
                case 2:
                    return 10
                case 3:
                    return 0

        def varasto_hae_tuote(tuote_id):
            match tuote_id:
                case 1:
                    return Tuote(1, "maito", 5)
                case 2:
                    return Tuote(2, "leipä", 6)
                case 3:
                    return Tuote(3, "juusto", 10)

        self.varasto_mock = Mock()
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_argumenteilla(
        self,
    ):
        kauppa = Kauppa(
            self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock
        )

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 100, "12345", "33333-44455", 5
        )

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_argumenteilla_ostaessa_kahta_eri_tuotetta_joita_varastossa(
        self,
    ):
        kauppa = Kauppa(
            self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock
        )
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 100, "12345", "33333-44455", 11
        )

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_argumenteilla_ostaessa_kahta_samaa_tuotetta_joita_varastossa(
        self,
    ):
        kauppa = Kauppa(
            self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock
        )
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 100, "12345", "33333-44455", 10
        )

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_argumenteilla_ostaessa_tuotetta_jota_on_ja_tuotetta_jota_ei_ole_varastossa(
        self,
    ):
        kauppa = Kauppa(
            self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock
        )
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(3)
        kauppa.tilimaksu("matti", "54321")
        self.pankki_mock.tilisiirto.assert_called_with(
            "matti", 100, "54321", "33333-44455", 5
        )
