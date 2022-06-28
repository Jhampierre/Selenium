import time
import unittest
import warnings

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys #Para el TAB
from selenium.webdriver.common.by import By #Para el find
import random
# #Para el sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #Para el explicit
from selenium.webdriver.support.ui import Select    #Escoger opciones
from selenium.common.exceptions import TimeoutException #Agregar la excepcion

class PruebaLogin(unittest.TestCase):
    def setUp(self):
        ser = Service("C:\Drivers\chromedriver.exe")
        op = webdriver.ChromeOptions()

        self.driver = webdriver.Chrome(service=ser, options=op)
        t = 2
        warnings.simplefilter('ignore', ResourceWarning)
    def test_login1(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()  # Maximizar ventana
        time.sleep(1)
        driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("Jhampierre")
        driver.find_element(By.XPATH,"//input[@id='password']").send_keys("admin123")
        driver.find_element(By.XPATH,"//input[@id='login-button']").click()
        time.sleep(1)
        error=driver.find_element(By.XPATH,"//h3[contains(@data-test,'error')]")
        error=error.text
        #print(error)
        if(error=="Epic sadface: Username and password do not match any user in this service"):
            print("El error de los datos es correcto")
            print("Prueba 1")

    def test_login2(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()  # Maximizar ventana
        time.sleep(1)
        driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("")
        driver.find_element(By.XPATH,"//input[@id='password']").send_keys("admin123")
        driver.find_element(By.XPATH,"//input[@id='login-button']").click()
        time.sleep(1)
        error=driver.find_element(By.XPATH,"//h3[contains(@data-test,'error')]")
        error=error.text
        print(error)
        if(error=="Epic sadface: Username is required"):
            print("Falta el nombre")
            print("Prueba 2")
    def test_login3(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()  # Maximizar ventana
        time.sleep(1)
        driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("Jhampierre")
        driver.find_element(By.XPATH,"//input[@id='password']").send_keys("")
        driver.find_element(By.XPATH,"//input[@id='login-button']").click()
        time.sleep(1)
        error=driver.find_element(By.XPATH,"//h3[contains(@data-test,'error')]")
        error=error.text
        print(error)
        if(error=="Epic sadface: Password is required"):
            print("Falta el Password")
            print("Prueba 3")

    def test_login4(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()  # Maximizar ventana
        time.sleep(1)
        driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("")
        driver.find_element(By.XPATH,"//input[@id='password']").send_keys("")
        driver.find_element(By.XPATH,"//input[@id='login-button']").click()
        time.sleep(1)
        error=driver.find_element(By.XPATH,"//h3[contains(@data-test,'error')]")
        error=error.text
        print(error)
        if(error=="Epic sadface: Username is required"):
            print("Falta Username y Password")
            print("Prueba 4")
    def test_login5(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()  # Maximizar ventana
        time.sleep(1)
        driver.find_element(By.XPATH,"//input[@id='user-name']").send_keys("standard_user")
        driver.find_element(By.XPATH,"//input[@id='password']").send_keys("secret_sauce")
        driver.find_element(By.XPATH,"//input[@id='login-button']").click()
        time.sleep(1)
        elemento = driver.find_element(By.XPATH,"//div[contains(@class,'app_logo')]")
        elemento.is_displayed()
        print("El elemento es: "+str(elemento))

        ''' 
        error=driver.find_element(By.XPATH,"//h3[contains(@data-test,'error')]")
        error=error.text
        print(error)
        if(error=="Epic sadface: Username is required"):
            print("Falta Username y Password")
            print("Prueba 5")
        '''
    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()

