from tuomari import Tuomari

class KPSTehdas:
    @staticmethod
    def luo_peli(tyyppi):
        match tyyppi:
            case "pvp":
                pass
            case "tekoaly":
                pass
            case "parempi_tekoaly":
                pass
            case _:
                return None



class KiviPaperiSakset:
    def __init__(self, tuomari: Tuomari) -> None:
        self._tuomari = tuomari
        self._ekan_siirto = self._ensimmaisen_siirto()
        self._tokan_siirto = None
    def pelaa(self):
        while self._onko_ok_siirto(self._ekan_siirto) and self._onko_ok_siirto(self._tokan_siirto):
            pass
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
        self._tokan_siirto = self._toisen_siirto(self._ekan_siirto)
        self._tekoaly = tekoaly
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = input("Toisen pelaajan siirto: ")
        return tokan_siirto