import pyautogui
import time
import os

size = pyautogui.size()
text = (63, 334)
# time.sleep(10)
pyautogui.PAUSE = 1
working = pyautogui.prompt('работать будешь? (д/н)')
shutdown = pyautogui.prompt('После завершения роботы нужно выключить компьютер? (д/н)')
pyautogui.click(pyautogui.locateCenterOnScreen('googleTim.png'))
pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('StableDiffusion.png', confidence=0.5)))
pyautogui.moveTo(text)
pyautogui.click()
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('delete')
toGenerate = open('to generate.txt', 'r').read()
i = toGenerate.count('\n')
last = -1
while i != 0:
    for x in range(0, 1):
        pyautogui.write(toGenerate[last + 1:toGenerate.find('\n', last + 2)])
        generateButton = pyautogui.locateOnScreen('generate.png', confidence=0.8)
        if generateButton is None:
            while generateButton is None:
                generateButton = pyautogui.locateOnScreen('generate.png', confidence=0.8)
                time.sleep(20)
        pyautogui.click(generateButton)
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('goOutGoogleTim.png', confidence=0.8)))
        time.sleep(1)
        if working == 'д':
            pyautogui.alert("Я работать начал")
        pyautogui.click(pyautogui.locateCenterOnScreen('googleTim.png'))
        pyautogui.click(pyautogui.center(pyautogui.locateOnScreen('StableDiffusion.png', confidence=0.5)))
        pyautogui.moveTo(text)
        pyautogui.click()
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('delete')

    last = toGenerate.find('\n', last + 2)
    i -= 1
if shutdown == 'д':
    os.system('shutdown /s /t 1')
