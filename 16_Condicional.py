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

driver.get("https://demoqa.com/text-box")
driver.maximize_window()    #Maximizar ventana

t=0.1

try:
    '''
    titulo=driver.find_element(By.XPATH,"//img[@src='/images/Toolsqa.jpg']")
    print(titulo.is_displayed()) #El elemento de la imagen es mostrado?
    btn1=driver.find_element(By.XPATH,"//div[@class='card mt-4 top-card'][contains(.,'Elements')]")
    if(titulo.is_displayed()==True):
        print("Existe la imagen")
        btn1.click()
        time.sleep(2)
    else:
        print("No existe la imagen")
    '''
    btn2 = driver.find_element(By.XPATH,"//button[contains(@id,'submit')]")
    if(btn2.is_enabled()==True):
        driver.find_element(By.XPATH,"//input[contains(@id,'userName')]").send_keys("Jhampierre Colonia"+Keys.TAB+"jhamcofer@gmail.com"+Keys.TAB+"Calel 1, Los Olivos"+Keys.TAB+"Hola 2")
        driver.execute_script("arguments[0].scrollIntoView();", btn2) #dirigirme al boton
        time.sleep(2)
        btn2.click()
    else:
        "El elemento esta desactivado"
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")

time.sleep(2)
driver.close()