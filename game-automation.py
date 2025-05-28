import pyautogui
import pyscreeze

# Path to the image file you want to find on the screen
image_path = 'click-me.png'

x, y = pyautogui.locateCenterOnScreen(image_path, confidence=0.8)

while True:
    pyautogui.moveTo(x, y)
    for i in range(100):
        pyautogui.click()

    pyautogui.moveTo(x - 20, y + 190)
    for i in range(10):
        pyautogui.click()

    pyautogui.moveTo(x - 100, y + 190)
    for i in range(10):
        pyautogui.click()
    
    pyautogui.moveTo(x - 170, y + 190)
    for i in range(10):
        pyautogui.click()

    

    