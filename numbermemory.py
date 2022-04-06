import pyautogui
import keyboard
import time
import pytesseract as tess
from PIL import Image
import win32con, win32api

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def main():
    click(10,10)
    time.sleep(0.6)
    im = pyautogui.screenshot(region=(250,345, 1300, 150))
    im.save(r'number.png')
    mainn()

def mainn():
    while keyboard.is_pressed("q") == False:
        try:
            img = Image.open('number.png')
            number = tess.image_to_string(img, config='--psm 6')
            pos = pyautogui.locateCenterOnScreen("bar.png", confidence=0.5)
            x = pos[0]
            y = pos[1]
            if x != "None":
                click(x,y)
                try:
                    numberr = str(number)
                    numberrr = numberr.replace(" ", "")
                except:
                    pass
                keyboard.write(numberrr)
                print(numberrr)
                time.sleep(1)
                keyboard.press_and_release("enter")
                time.sleep(1)
                keyboard.press_and_release("enter")
                main()
            else:
                mainn()
        except:
            mainn()
main()
