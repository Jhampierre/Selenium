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
    driver.find_element(By.XPATH,"//input[@name='first_name']").send_keys("Jhampierre")
    time.sleep(t)
    driver.find_element(By.XPATH,"//input[contains(@placeholder,'Last Name')]").send_keys("Colonia Fernandez")
    time.sleep(t)
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys("jhamcofer@gmail.com")
    time.sleep(t)
    driver.find_element(By.XPATH, "//input[contains(@name,'phone')]").send_keys("(51)94288385")
    time.sleep(t)
    driver.find_element(By.XPATH, "//input[contains(@name,'address')]").send_keys("Calle 1 MZ K LT 12, Los Olivos")
    time.sleep(t)
    driver.find_element(By.XPATH, "//input[contains(@name,'city')]").send_keys("Lima")
    time.sleep(t)
    StateSelect = driver.find_element(By.XPATH,"//select[contains(@name,'state')]")
    sel = Select(StateSelect)
    sel.select_by_index(random.randint(0,15))
    time.sleep(t)
    driver.find_element(By.XPATH, "//input[contains(@name,'zip')]").send_keys("15307")
    time.sleep(t)
    driver.find_element(By.XPATH, "//input[contains(@name,'website')]").send_keys("www.google.com.pe")
    time.sleep(t)
    driver.find_element(By.XPATH, "//input[contains(@value,'yes')]").click()
    time.sleep(t)
    driver.find_element(By.XPATH, "//textarea[contains(@class,'form-control')]").send_keys("This is a test")
    time.sleep(t)
    driver.find_element(By.XPATH, "//button[@type='submit'][contains(.,'Send')]").click()
    time.sleep(t)
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")
time.sleep(2)
driver.close()