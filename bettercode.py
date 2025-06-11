import pyautogui
import time

pyautogui.useImageNotFoundException()

"""
Script for automating the Stimulation Clicker browser game.
Game link: https://neal.fun/stimulation-clicker/
Game link: https://neal.fun/stimulation-clicker/
Game link: https://neal.fun/stimulation-clicker/
"""

# imgs for this stuff
clickme = 'images/image.png'
treasure = 'images/treasure.png'
start = 'images/start.png'
collect = 'images/collect.png'
centerduo = 'images/centerduo.png'
buy = 'images/buy.png'
sell = 'images/sell.png'

def move_and_click(image, clicks=1, offset=(0, 0), confidence=0.8):
    try:
        x, y = pyautogui.locateCenterOnScreen(image, confidence=confidence)
        pyautogui.moveTo(x + offset[0], y + offset[1])
        for _ in range(clicks):
            pyautogui.click()
        return True
    except pyautogui.ImageNotFoundException:
        return False

def click_stimulation(x, y):
    pyautogui.moveTo(x, y)
    for _ in range(100):
        pyautogui.click()
    pyautogui.moveTo(x - 20, y + 210)
    for _ in range(10):
        pyautogui.click()

def rapid_clicking_phase(x, y):
    pyautogui.moveTo(x, y)
    for _ in range(500):
        pyautogui.click()
    pyautogui.moveTo(x - 100, y + 190)
    pyautogui.click()
    pyautogui.moveTo(x - 170, y + 190)
    pyautogui.click()

# main click me buttona round which it all revolves
x, y = pyautogui.locateCenterOnScreen(clickme, confidence=0.4)

while True:
    for _ in range(3):
        move_and_click(buy, clicks=10)            # Buy 10 stocks
        move_and_click(start) or click_stimulation(x, y)  # Press start or fallback to clicking

        if move_and_click(collect): # collect press
            time.sleep(1.5)

        # treasure
        while move_and_click(treasure):
            pass

        move_and_click(sell, clicks=10)           # Sell 10 stocks

        # Try to solve Duolingo if visible
        try:
            x1, y1 = pyautogui.locateCenterOnScreen(centerduo, confidence=0.8)
            pyautogui.moveTo(x1 + 10, y1)
            pyautogui.click()
            
        except pyautogui.ImageNotFoundException:
            pass

    rapid_clicking_phase(x, y)
