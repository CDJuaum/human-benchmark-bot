import pyautogui
from pynput.keyboard import Controller
import win32api, win32con
from time import sleep
from PIL import Image
import pytesseract as tess

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

keyboard = Controller()

#click function
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

SS = pyautogui.screenshot('noice.png',region=(450,380, 1000, 180)) #screenshots the text
SS1 = pyautogui.locateCenterOnScreen("noice.png", confidence=0.27) #finds the type box
x = SS1[0] #x coordinates for the type box
y = SS1[1] #y coordinates for the type box

im = Image.open('noice.png') #open text image

text = tess.image_to_string(im) #gets text from image

click(x,y) #clicks the type box

textt = str(text) #to string
texttt = textt.replace("\n" or "  ", " ") #deletes newlines and/or double spaces

keyboard.type(texttt) #types the text