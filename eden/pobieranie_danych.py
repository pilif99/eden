import datetime
import pyautogui as gui, time
from raport_288 import Raport_288
from raport_zrealizowane import Raport_Zrealizowane
from raport_anulowane import Raport_Anulowane
from raport_425 import Raport_425
from raport_kategorie import Raport_Kategorie

class Pobieranie_Danych(Raport_288, Raport_Zrealizowane, Raport_Anulowane, Raport_425, Raport_Kategorie):

    def _pobieranie_danych(self, nazwa, marka, jezyk, grupa_towarowa, czyaudyt):

        if nazwa == 288:
            
            self.pobierz_288(marka, czyaudyt)

        elif nazwa == 'zrealizowane':
            
            self.pobierz_zrealizowane()

        elif nazwa == 'anulowane':

            self.pobierz_anulowane()

        elif nazwa == 425:

            self.pobierz_425(jezyk)

        elif nazwa == 'kategorie':

            self.pobierz_kategorie(marka, grupa_towarowa)