
from wklejanie_danych import Wklejanie_Danych
from pobieranie_danych import Pobieranie_Danych
from logowanie import Logowanie
from edycja_danych import Edycja_Danych
from zamkniecie_edena import Zamkniecie_Edena
import pandas as pd, pandas

class Eden(pandas.DataFrame, Logowanie, Pobieranie_Danych, Wklejanie_Danych, Edycja_Danych, Zamkniecie_Edena):

    def __init__(self, nazwa, marka = 'broger', jezyk = 'de', grupa_towarowa = '%', czyaudyt = False):

        super().__init__()
        
        self._logowanie()
        self._pobieranie_danych(nazwa, marka, jezyk, grupa_towarowa, czyaudyt)
        self._wklejanie_danych(nazwa)
        self._zamkniecie_edena()
        self._edycja_danych(nazwa)

        self.append(super().__init__(self.object))

if __name__ == "__main__":

    a = Eden(425, jezyk = 'es')
    print(a)