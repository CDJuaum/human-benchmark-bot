import pyautogui
from time import sleep
import win32api, win32con
import keyboard

# click on screen function
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


# checks if letter "q" was clicked on keyboard if it was it stops the loop
while keyboard.is_pressed('q') == False:
    try:
        SS = pyautogui.locateCenterOnScreen("Test-subject.png", confidence=0.3)
        # gets the 1st part of the above output
        x = SS[0]
        # gets the 2nd part of the above output
        y = SS[1]
        # checks if the image was detected and if it was it clicks on the coordinates
        if SS != "None":
            click(x,y)              
    except:
        pass