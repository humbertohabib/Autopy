# EXCEL
import openpyxl
wb = openpyxl.load_workbook('produtos_ficticios.xlsx')
ws = wb['Produtos']
for r in ws.iter_rows(min_row=2):
    for i in range(0, len(r)):
        # if (i == 0):
        #     pass
        # elif i == 1:
        #     pass
        # else:
        #     pass
        print (r[i].value)
    break

# CLIPBOARD
import pyperclip # para copiar preservando acentos
pyperclip.copy("A")

# AUTOMATE GUI
import pyautogui
pyautogui.click(828,585, interval=0.1)
pyautogui.hotkey('ctrl', 'v')

# DELAY
from time import sleep
sleep(1)

