import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = r'C:\Users\vcm70\OneDrive\Área de Trabalho\dev\automação twitter\chromedriver.exe'
driver = webdriver.Chrome(PATH)

emails = input("Digite os links separados por vírgulas: ")
lista_emails = emails.split(',')

spamar = input('escreve teu spam ai doidao: ')
print(lista_emails)

driver.get('https://twitter.com/login')
print('voce tem 20 segundos para fazer login')
time.sleep(23)

def enviar_msg():
  for x in lista_emails:
    driver.get(x)
    time.sleep(5)
    dm = driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[1]/div[2]/div[2]')
    dm.click()
    time.sleep(10)
    texto = driver.find_element("xpath", '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div/aside/div[2]/div[2]/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div')
    texto.send_keys(spamar, Keys.ENTER)
enviar_msg()