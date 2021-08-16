#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1

pyautogui.hotkey('ctrl','t')
link = 'https://aluno.uninove.br/'
pyperclip.copy(link)
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')

time.sleep(5)
pyautogui.click(x=407, y=431)
pyautogui.write('*****')#login
pyautogui.press('tab')#senha
senha = '*****'
pyperclip.copy(senha)
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')

time.sleep(4)
pyautogui.click(x=784, y=631)
time.sleep(4)
pyautogui.click(x=502, y=361)

time.sleep(4)
pyautogui.click(x=1009, y=471)
time.sleep(6)
pyautogui.press('enter')
time.sleep(4)
pyautogui.press('enter')

pyautogui.hotkey('ctrl','t')
link = 'https://mail.google.com'
pyperclip.copy(link)
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')

time.sleep(5)
pyautogui.click(x=39, y=171)
pyautogui.write("******")#destinatario 
pyautogui.press("tab")
pyautogui.press("tab")

assunto ="Boleto"
pyperclip.copy(assunto)
pyautogui.hotkey('ctrl','v')
pyautogui.press("tab")

texto = f"""
BOLETO DESSE MES
"""
pyautogui.write(texto)

pyautogui.click(x=938, y=823)
time.sleep(5)
pyautogui.click(x=97, y=199)
time.sleep(5)
pyautogui.click(x=265, y=177, clicks = 2)

time.sleep(5)
pyautogui.hotkey("ctrl","enter")





