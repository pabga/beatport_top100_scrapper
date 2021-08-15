from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import pandas as pd
# Opciones de navegación
options =  webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\\webdriver\\chromedriver.exe'
driver = webdriver.Chrome(driver_path, chrome_options = options)

# Inicia el navegador
driver.get('https://www.beatport.com/genre/funky-groove-jackin-house/81/top-100')
#driver.get('https://www.beatport.com/genre/trance/7/top-100')

# acepta el cartel de cookies
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[1]/div[1]/div[4]/a[2]')))\
    .click()
#busca en web

#WebDriverWait(driver, 5)\
 #   .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
 #                                     'input#inputSearch')))\
#    .send_keys('Madrid')

#WebDriverWait(driver, 5)\
  #  .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
 #                                     'i.icon.icon-search')))\
#    .click()

#WebDriverWait(driver, 5)\
 #   .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
   #                                   'i.icon_weather_s.icon.icon-local')))\
  #  .click()

#WebDriverWait(driver, 5)\
#    .until(EC.element_to_be_clickable((By.XPATH,
#                                      '/html/body/div[7]/main/div[4]/div/section[4]/section/div/article/section/ul/li[2]/a')))\
#    .click()
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                      '/html/body/div[3]/div/section/main/div/div[2]')))
texto_columnas = driver.find_element_by_xpath('/html/body/div[3]/div/section/main/div/div[2]')
texto_columnas = texto_columnas.text
#print(texto_columnas)
header = texto_columnas.split("1")[0].split('\n')[0:-1]
top100c = texto_columnas.split('\n')[6:-1]
top100 = texto_columnas.split('\n')[6:-1] # row por comas
print("////////////////////////////////////////////////////////////////////////")
track1s = top100[2]+" - " + top100[1]
track2s = top100[9]+" - " + top100[8]
track3s = top100[16]+" - " + top100[15]
track4s = top100[23]+" - " + top100[22]
track5s = top100[30]+" - " + top100[29]
track6s = top100[37]+" - " + top100[36]
track7s = top100[44]+" - " + top100[43]
track8s = top100[51]+" - " + top100[50]
track9s = top100[58]+" - " + top100[57]
track10s = top100[65]+" - " + top100[64]
def printTop10s():

    print(track1s)
    print(track2s)
    print(track3s)
    print(track4s)
    print(track5s)
    print(track6s)
    print(track7s)
    print(track8s)
    print(track9s)
    print(track10s)
print(printTop10s())
#for indice,valor in enumerate (top100):
#   print('I:{}-Val: {} '.format(indice, valor)) #imprime cada elemento de la lista con su indice
#imprime como lista corrida top 100 desde el 1
#for i in range(len(top100)):
#   print(top100[i])
#print (header)
#print (top100c)
#print(top100[:3]) #imprime el primer registro
#track1prueba = top100[:3]
#track2prueba = top100[7:10]
#Remix = "Remix"
#if "Remix" in (top100)
# print(top100[0]+". " + top100[2]+" " - " + top100[1])
#estructura [nro_track] + [artista] +      [titulo]
track1 = top100[0]+". " + top100[2]+" - " + top100[1]
track2 = top100[7]+". " + top100[9]+" - " + top100[8]
track3 = top100[14]+". " + top100[16]+" - " + top100[15]
track4 = top100[21]+". " + top100[23]+" - " + top100[22]
track5 = top100[28]+". " + top100[30]+" - " + top100[29]
track6 = top100[35]+". " + top100[37]+" - " + top100[36]
track7 = top100[42]+". " + top100[44]+" - " + top100[43]
track8 = top100[49]+". " + top100[51]+" - " + top100[50]
track9 = top100[56]+". " + top100[58]+" - " + top100[57]
track10 = top100[63]+". " + top100[65]+" - " + top100[64]
def printTop10 ():
    print(track1)
    print(track2)
    print(track3)
    print(track4)
    print(track5)
    print(track6)
    print(track7)
    print(track8)
    print(track9)
    print(track10)
print(printTop10())
"""rank = list()
artista = list()
titulo = list()
remixer = list()
for i in range(0,len(top100c), 8):
    rank.append(top100c[i])
    artista.append(top100c[i+2])
    titulo.append(top100c[i+1])
    remixer.append(top100c[i+3])
print(df)

df = pd.DataFrame({'rank': rank, 'artista': artista, 'titulo':titulo,'remixer':remixer})
df.to_csv('top100.csv', index=False)
driver.quit()"""
#abre nueva pestaña para la pagina de descargas
WebDriverWait(driver, 3)

driver.execute_script("window.open('https://biffhard.click/','_blank')")

alltabs = driver.window_handles

for tab in alltabs:
    driver.switch_to_window(tab)
    print(driver.current_url)
#click en busqueda y pasteado del track1
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#he-search-text')))\
    .send_keys(track1s)
#click buscar
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      'input#he-search-submit')))\
    .click()
time.sleep(2)

# descarga del track1
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                     '/html/body/div[1]/div/div[2]/aside[1]/div[1]/ul/li[1]/div[1]/a')))\
   .click()
time.sleep(2)

WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.XPATH,
                                     '/html/body/div[1]/div/div[2]/aside[1]/div[1]/div/div[2]/a[2]')))\
   .click()


