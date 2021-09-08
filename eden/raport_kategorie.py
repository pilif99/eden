
import pyautogui as gui, time

class Raport_Kategorie:

    def pobierz_kategorie(self, marka, grupa_towarowa):

        time.sleep(0.1)
        gui.click(85, 372)
        time.sleep(0.1)
        gui.click(85, 210)
        gui.click(85, 210)
        time.sleep(0.1)
        gui.click(622, 321)
        gui.typewrite('288', interval=0.01)
        gui.press('enter')
        gui.click(651, 274)
        lista = ['%', 'en', 'eur', marka, grupa_towarowa, "'0', '7'"]
        for i in range(len(lista)):
            if i != 1:
                gui.press('enter')
            gui.press('enter')
            gui.press('enter')
            gui.press('f2')
            gui.typewrite(lista[i], interval=0.01)
        gui.click(1000, 700)
        time.sleep(10)
        gui.keyDown('ctrl')
        gui.press('a')
        gui.keyUp('ctrl')
        time.sleep(1)
        gui.keyDown('ctrl')
        gui.press('c')
        gui.keyUp('ctrl')
        time.sleep(75)
        gui.click(1165, 365)
        gui.click(1165, 217)