
import datetime
import pyautogui as gui, time

class Raport_Anulowane:

    def pobierz_anulowane(self):

        data1 = datetime.datetime.now().strftime('%Y%m%d')
        data2 = (datetime.datetime.now() - datetime.timedelta(days=30)).strftime('%Y%m%d')

        time.sleep(0.1)
        gui.click(85, 372)
        time.sleep(0.1)
        gui.click(85, 210)
        gui.click(85, 210)
        time.sleep(0.1)
        gui.click(622, 321)
        gui.typewrite('388', interval=0.01)
        gui.press('enter')
        gui.click(651, 274)
        gui.press('enter')
        gui.press('enter')
        gui.press('F2')
        gui.typewrite(data2, interval=0.01)
        gui.press('enter')
        gui.press('enter')
        gui.press('enter')
        gui.typewrite(data1, interval=0.01)
        gui.click(1002, 700)
        time.sleep(5)
        gui.keyDown('ctrl')
        gui.press('a')
        gui.keyUp('ctrl')
        gui.keyDown('ctrl')
        gui.press('c')
        gui.keyUp('ctrl')
        time.sleep(15)
        gui.click(1155, 355)
        gui.click(1169, 213)