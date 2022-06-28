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
t=1

class Pagina_Login():
    def __init__(self,driver):
        self.driver = driver
    def Login_Master(self,url, name, clave, t):
        driver = self.driver
        f=Funciones_Globales(driver)
        f.Navegar(url, t)
        f.Texto_Xpath_Valida("//input[@id='user-name']",name, t)
        f.Texto_Xpath_Valida("//input[@id='password']", clave, t)
        f.Click_Xpath_Valida("//input[@id='login-button']",t)