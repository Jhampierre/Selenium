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

btn=driver.find_element(By.XPATH,"//button[@type='submit'][contains(.,'Send')]")
btn.click()
time.sleep(t)

name_val = driver.find_element(By.XPATH,"//small[@class='help-block'][contains(.,'Please supply your first name')]")
name=name_val.text #Que guarde el texto de la informacion
#print("El valor del error es "+name)

if(name=="Please supply your first name"):
    print("Falta el nombre")
    driver.find_element(By.XPATH,"//input[@name='first_name']").send_keys("Jhampiere Colonia")
    print("Nombre agregado")
else:
    print("Nombre corecto")

time.sleep(2)
driver.close()