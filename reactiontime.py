import pyautogui
import win32api, win32con

#click function
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)



while True: #loop, unstopable just cuz
    x, y = pyautogui.position() #gets position from your cursor
    pixelColor = pyautogui.screenshot().getpixel((x, y)) #gets the rgb code from the color your cursor is hovering
    if pixelColor ==  (75,  219,  106): #if the color is green
        click(x,y) #click where the cursor is
