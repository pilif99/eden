
import pyautogui as gui, time

class Raport_425:

    def pobierz_425(self, jezyk):

        time.sleep(0.1)
        gui.click(85, 372)
        time.sleep(0.1)
        gui.click(85, 210)
        gui.click(85, 210)
        time.sleep(0.1)
        gui.click(622, 321)
        gui.typewrite('425', interval=0.01)
        gui.press('enter')
        gui.click(651, 274)
        gui.press('enter')
        gui.press('enter')
        gui.press('f2')
        gui.typewrite(jezyk, interval=0.01)
        gui.click(1011, 703)
        time.sleep(3)
        gui.keyDown('ctrl')
        gui.press('a')
        gui.keyUp('ctrl')
        gui.keyDown('ctrl')
        gui.press('c')
        gui.keyUp('ctrl')
        time.sleep(10)
        gui.click(1166, 356)
        gui.click(1170, 218)