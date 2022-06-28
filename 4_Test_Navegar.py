from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
op.add_argument('--ignore-ssl-errors=yes')  #Ignorar certificados
op.add_argument('--ignore-certificate-errors')
#Inicializar el driver
driver = webdriver.Chrome(service=ser, options=op)
t=4 #A veces cuando el tiempo es muy alto, la funcion back no funciona
driver.get("https://demoqa.com/text-box")
driver.maximize_window()    #Maximizar ventana
time.sleep(t)
driver.get("https://translate.google.com/?hl=es&sl=es&tl=zh-CN&text=zouting&op=translate")
time.sleep(t)
driver.get("https://github.com/Ebazhanov/linkedin-skill-assessments-quizzes")
time.sleep(t)
driver.back()
time.sleep(t)
#Retroceder
driver.execute_script("window.history.go(-1)")  #A veces no funciona la funcion back, esta es otra manera
time.sleep(t)
#Saltar
driver.execute_script("window.history.go(2)")
driver.close()