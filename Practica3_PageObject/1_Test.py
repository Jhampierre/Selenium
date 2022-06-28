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
from Funciones.Funciones import Funciones_Globales #carpeta#nombre archivo#Clase
from Funciones.Page_Login import Pagina_Login

tg=.5

class PruebaLogin(unittest.TestCase):
    def setUp(self):
        ser = Service("C:\Drivers\chromedriver.exe")
        op = webdriver.ChromeOptions()

        self.driver = webdriver.Chrome(service=ser, options=op)
        warnings.simplefilter('ignore', ResourceWarning)
    def test1(self):
        driver = self.driver
        f=Funciones_Globales(driver)
        '''pg=Pagina_Login(driver)
        pg.Login_Master("https://www.saucedemo.com/","Jhampierre","admin123",tg)
        '''
        f.Navegar("https://demoqa.com/text-box",tg)
        #f.Select_Xpath_Text("//select[contains(@id,'select-demo')]","Sunday",tg)
        #f.Select_Xpath_Type("//select[contains(@id,'select-demo')]","index",3,tg)
        '''for n in range(2,6):
            f.Check_Xpath_Multiples(.3,"(//input[contains(@type,'checkbox')])["+str(n)+"]")
            '''
        #f.Texto_Mixto("xpath","//input[contains(@id,'userName')]","Jhampierre", tg)
        f.Texto_Mixto("id", "userName", "Jhampierre", tg)
        f.Click_Mixto("xpath","//button[contains(@id,'submit')]",tg)
    def tearDown(self):
        driver = self.driver
        driver.close()

if __name__ == '__main__':
    unittest.main()

