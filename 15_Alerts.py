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

driver.get("https://demo.seleniumeasy.com/bootstrap-modal-demo.html")
driver.maximize_window()    #Maximizar ventana

t=0.1

driver.find_element(By.XPATH,"//a[@href='#myModal0']").click()

try:
    #driver.switch_to_alert().accept() #Ejecutar el boton Aceptar
    Buscar = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,"(//a[@href='#'][contains(.,'Save changes')])[1]")))
    driver.find_element(By.XPATH,"(//a[@href='#'][contains(.,'Save changes')])[1]").click()

    #driver.switch_to_alert().dismiss()  #Ejecutar el boton Close
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")

time.sleep(t)
driver.close()