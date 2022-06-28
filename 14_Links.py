from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys #Para el TAB
from selenium.webdriver.common.by import By #Para el find
import random
# #Para el sleep
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #Para el explicit
from selenium.webdriver.support.ui import Select    #Escoger opciones
from selenium.common.exceptions import TimeoutException #Agregar la excepcion

ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://demo.seleniumeasy.com/input-form-demo.html")
driver.maximize_window()    #Maximizar ventana

t=0.1

try:
    #Obteniendo todos los links de la pagina
    links = driver.find_elements(By.TAG_NAME,"a")
    print("El numero de links que hay en la pagina es: ", len(links))
    for x in links:
        print(x.text)
    driver.find_element(By.LINK_TEXT,"Date pickers").click()
    time.sleep(t)
    driver.find_element(By.LINK_TEXT, "JQuery Date Picker").click()
    time.sleep(t)
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")
time.sleep(2)
driver.close()