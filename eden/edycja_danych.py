
class Edycja_Danych:

    def _edycja_danych(self, nazwa):

        if nazwa == 'zrealizowane':

            self.object['Ilosc'] = self.object['Ilosc'].replace(',00', '', regex=True)
            self.object['Ilosc'] = self.object['Ilosc'].astype(int)
            self.object['Sprzedaż'] = self.object['Sprzedaż'].replace(',', '.', regex=True)
            self.object['Sprzedaż'] = self.object['Sprzedaż'].astype(float)
            
        elif nazwa == 'anulowane':

            from waluta import Waluta

            self.object['gNiezrealizowanaIlosc'] = self.object['gNiezrealizowanaIlosc'].replace(',00', '', regex=True)
            self.object['gNiezrealizowanaIlosc'] = self.object['gNiezrealizowanaIlosc'].astype(int)
            self.object['gNiezrealizowanaWartosc'] = self.object['gNiezrealizowanaWartosc'].replace(',', '.', regex=True)
            self.object['gNiezrealizowanaWartosc'] = self.object['gNiezrealizowanaWartosc'].astype(float)
            self.object['lCenaNetPoRab'] = self.object['lCenaNetPoRab'].replace(',', '.', regex=True)
            self.object['lCenaNetPoRab'] = self.object['lCenaNetPoRab'].astype(float)
            
            EUR = Waluta('euro')

            self.object['gNiezrealizowanaWartosc'] = round(self.object['gNiezrealizowanaWartosc'] * EUR, 2)
            self.object['lCenaNetPoRab'] = round(self.object['lCenaNetPoRab'] * EUR, 2)

            print(EUR)