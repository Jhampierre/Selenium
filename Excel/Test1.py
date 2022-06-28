import time
import unittest
import openpyxl
from Funciones_Ex import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import warnings
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from Funciones.Funciones import Funciones_Globales

tg=0.1

class base_test(unittest.TestCase):
    def setUp(self):
        ser = Service("C:\Drivers\chromedriver.exe")
        op = webdriver.ChromeOptions()

        self.driver = webdriver.Chrome(service=ser, options=op)
        warnings.simplefilter('ignore', ResourceWarning)

    def test1(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        fe = Funexcel(driver)
        f.Navegar("https://demoqa.com/text-box",tg)
        ruta="C://Users//Jhampierre//PycharmProjects//Curso_selenium//Excel//Datos_ok.xlsx"
        filas = fe.getRow(ruta,"Hoja1")

        for r in range(2, filas+1):
            nombre = fe.readData(ruta,"Hoja1",r,1)
            email = fe.readData(ruta,"Hoja1",r,2)
            dir1 = fe.readData(ruta, "Hoja1", r, 3)
            dir2 = fe.readData(ruta, "Hoja1", r, 4)

            f.Texto_Mixto("id","userName",nombre,tg)
            f.Texto_Mixto("id", "userEmail", email, tg)
            f.Texto_Mixto("id", "currentAddress", dir1, tg)
            f.Texto_Mixto("id", "permanentAddress", dir2, tg)
            f.Click_Mixto("id", "submit", tg)

            e=f.Existe("id","name",tg)
            if(e=="Existe"):
                print("El texto fue insertado")
                fe.writeData(ruta, "Hoja1",r,5,"Insertado")
            else:
                print("El texto no fue insertado")
                fe.writeData(ruta, "Hoja1",r,5,"Error")