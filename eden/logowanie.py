
import pyautogui as gui, time

class Logowanie:

    def _logowanie(self):

        screenWidth, screenHeight = gui.size()
        gui.moveTo(5,screenHeight-5)
        gui.click()
        time.sleep(0.5)
        gui.typewrite('eden nowszy (2)', interval=0.1)
        gui.press('enter')
        time.sleep(0.5)
        gui.typewrite('florenz', interval=0.1)
        gui.press('enter')
        gui.typewrite('florenz', interval=0.1)
        gui.press('enter')
        gui.press('enter')