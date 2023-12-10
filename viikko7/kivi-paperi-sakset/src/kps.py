from tekoaly import Tekoaly, TekoalyParannettu
from tuomari import Tuomari


class KPSTehdas:
    @staticmethod
    def luo_peli(tyyppi):
        tuomari = Tuomari()
        match tyyppi:
            case "a":
                return KPSPelaajaVsPelaaja(tuomari)
            case "b":
                tekoaly = Tekoaly()
                return KPSTekoaly(tuomari, tekoaly)
            case "c":
                tekoaly = TekoalyParannettu(10)
                return KPSTekoaly(tuomari, tekoaly)
            case _:
                return None


class KiviPaperiSakset:
    def __init__(self, tuomari: Tuomari) -> None:
        self._tuomari = tuomari
        self._ekan_siirto = self._ensimmaisen_siirto()
        self._tokan_siirto = None

    def pelaa(self):
        while self._onko_ok_siirto(self._ekan_siirto) and self._onko_ok_siirto(
            self._tokan_siirto
        ):
            self._tuomari.kirjaa_siirto(self._ekan_siirto, self._tokan_siirto)
            print(self._tuomari)
            self._ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
            self._tokan_siirto = self._toisen_siirto(self._ekan_siirto)
        print("Kiitos!")
        print(self._tuomari)

    def _ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    # tämän metodin toteutus vaihtelee eri pelityypeissä
    def _toisen_siirto(self, ensimmaisen_siirto):
        # metodin oletustoteutus
        return "k"

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"


class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def __init__(self, tuomari) -> None:
        super().__init__(tuomari)
        self._tokan_siirto = self._toisen_siirto(self._ekan_siirto)

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = input("Toisen pelaajan siirto: ")
        return tokan_siirto


class KPSTekoaly(KiviPaperiSakset):
    def __init__(self, tuomari, tekoaly) -> None:
        super().__init__(tuomari)
        self._tekoaly = tekoaly        
        self._tokan_siirto = self._toisen_siirto(self._ekan_siirto)

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        self._tekoaly.aseta_siirto(ensimmaisen_siirto)
        return tokan_siirto
