
import pyperclip, re
import pandas as pd, pandas
import numpy as np

class Wklejanie_Danych:

    def _wklejanie_danych(self, nazwa):

        a = pyperclip.paste()

        if nazwa != 288:
            
            a = a.split('\r\n')
            for i in range(len(a)):
                a[i] = a[i].split('\t')
        
        else:
            
            a = re.sub('"\r\n"', '"xxx\r\n"', a)
            a = re.sub('sGrupaTowarowa\r\n', 'sGrupaTowarowaxxx\r\n', a)
            a = re.sub('"\t"', '"xxx\t"', a)
            a = a.split('xxx\r\n')
            for i in range(len(a)):
                if i == 0:
                    a[i] = a[i].split('\t')
                else:
                    a[i] = a[i].split('xxx\t')

        self.object = pandas.DataFrame(a[1:-1], columns = a[0])
        self.object = self.object.replace(np.nan, '', regex=True)
        self.object = self.object.replace('"', '', regex=True)