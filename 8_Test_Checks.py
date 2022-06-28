from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #Para el find
from selenium.webdriver.common.keys import Keys #Para el TAB
import time #Para el sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
op.add_argument('--ignore-ssl-errors=yes')  #Ignorar certificados
op.add_argument('--ignore-certificate-errors')
#Inicializar el driver
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://demo.seleniumeasy.com/basic-checkbox-demo.html")
driver.maximize_window()    #Maximizar ventana
t=2
driver.implicitly_wait(5)
btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[contains(.,'Click on this check box')]")))
btn.click()

#Deslizar - Scroll down
driver.execute_script("window.scrollTo(0,300)")
time.sleep(1)

btn2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[contains(.,'Option 1')]")))
btn2.click()

btn4 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[contains(.,'Option 4')]")))
btn4.click()

time.sleep(t)
driver.close()