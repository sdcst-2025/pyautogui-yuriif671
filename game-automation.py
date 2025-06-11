import pyautogui
import time

pyautogui.useImageNotFoundException()

"""

script is meant for the stimulation clicker browser game

https://neal.fun/stimulation-clicker/
https://neal.fun/stimulation-clicker/
https://neal.fun/stimulation-clicker/

"""


clickme = 'images/image.png'
treasure = 'images/treasure.png'
start = 'images/start.png'
collect = 'images/collect.png'
centerduo = 'images/centerduo.png'
buy = 'images/buy.png'
sell = 'images/sell.png'


x, y = pyautogui.locateCenterOnScreen(clickme, confidence=0.4)

while True:

    for i in range(3):
        # buy 10 stocks
        try:
            pyautogui.moveTo(pyautogui.locateOnScreen(buy, confidence=0.8))
            for i in range(10):
                pyautogui.click()
        except:
            pass
        # clickidy click
        try:
            pyautogui.moveTo(pyautogui.locateOnScreen(start, confidence=0.8))
            pyautogui.click()
        except Exception:
            pass

            pyautogui.moveTo(x, y)
            for i in range(10):
                pyautogui.click()

            pyautogui.moveTo(x + 20, y + 220)
            for i in range(10):
                pyautogui.click()


        # collect press
        try:
            pyautogui.moveTo(pyautogui.locateOnScreen(collect, confidence=0.8))
            pyautogui.click()

            time.sleep(1.5)
        except Exception:
            pass
        
        # open treasure
        try:
            while True:
                pyautogui.moveTo(pyautogui.locateOnScreen(treasure, confidence=0.8))
                pyautogui.click()

        except:
            pass
        
        # sell 10 stocks
        try:
            pyautogui.moveTo(pyautogui.locateOnScreen(sell, confidence=0.8))
            for i in range(10):
                pyautogui.click()
        except:
            pass

        #try to solve duolingo
        try:
            x1, y1 = pyautogui.locateCenterOnScreen(centerduo, confidence=0.8)
            
            pyautogui.moveTo(x1+10, y1)
            pyautogui.click()
            
        except:
            pass
        

    pyautogui.moveTo(x, y)
    for i in range(500):
        pyautogui.click()
    
    pyautogui.moveTo(x - 100, y + 190)    
    pyautogui.click()

    pyautogui.moveTo(x - 170, y + 190)
    pyautogui.click()