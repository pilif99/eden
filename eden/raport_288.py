
import pyautogui as gui, time

class Raport_288:

    def pobierz_288(self, marka, czyaudyt):

        if czyaudyt:
            audyt = "'0', '7'"
        else:
            audyt = "'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'"

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
        lista = ['%', 'en', 'eur', marka, '%', audyt]
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