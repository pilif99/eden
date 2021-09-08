
import datetime
import pyautogui as gui, time

class Raport_Zrealizowane:

    def pobierz_zrealizowane(self):

        data1 = datetime.datetime.now().strftime('%Y%m%d')
        data2 = (datetime.datetime.now() - datetime.timedelta(days=30)).strftime('%Y%m%d')

        time.sleep(0.1)
        gui.click(85, 372)
        time.sleep(0.1)
        gui.mouseDown(227, 187)
        gui.mouseUp(227, 240)
        gui.click(76, 161)
        gui.click(76, 161)
        gui.click(654, 724)
        time.sleep(0.1)
        gui.click(973, 284)
        gui.keyDown('backspace')
        gui.click(487, 284)
        gui.typewrite(data2 + '..' + data1, interval=0.01)
        gui.click(760, 284)
        gui.typewrite('dlewandowska', interval=0.01)
        gui.click(661, 354)
        for i in range(7):
            gui.press('down')
        gui.press('enter')
        gui.click(1207, 354)
        time.sleep(15)
        gui.click(406, 417)
        gui.keyDown('ctrl')
        gui.press('c')
        gui.keyUp('ctrl')
        time.sleep(5)
        gui.click(1325, 206)
        gui.click(1602, 172)