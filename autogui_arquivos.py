import pyautogui
import  time


pyautogui.alert("O código vai começar. Não use nada do seu computador")
pyautogui.PAUSE = 0.5
# abrir o Google Drive no meu computador
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('drive.google.seu.drive')# colocar o local do Google drive, de sua pasta
pyautogui.press('enter')

# entrar na minha area de trabalho
pyautogui.hotkey('winleft', 'd')

# cliquei no arquivo que eu quero fazr backup e arrastei ele
pyautogui.moveTo(1306, 35) # esta posição é única para cada computador, cada tela dará uma medida; 
pyautogui.mouseDown()
pyautogui.moveTo(843, 531)  # esta posição é única para cada computador, cada tela dará uma medida; 

# enquanto estou arrastando, eu vu mudar para o  Google Drive
pyautogui.hotkey('alt', 'tab')
time.sleep(3)

# larguei o arquivo no Google Drive
pyautogui.mouseUp()

# esperar 5 segundos
time.sleep(5)


pyautogui.alert("O código terminou. Pode voltar a usar seu computador")

