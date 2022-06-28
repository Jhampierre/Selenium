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

class base_test(unittest.TestCase):
    def setUp(self):
        ser = Service("C:\Drivers\chromedriver.exe")
        op = webdriver.ChromeOptions()

        self.driver = webdriver.Chrome(service=ser, options=op)
        t = 2
        warnings.simplefilter('ignore', ResourceWarning)
    def test1(self):
        driver = self.driver
        driver.get("https://doradobet.com/gestion/misbonos")
        #driver.maximize_window()  # Maximizar ventana
        time.sleep(4)

    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()

