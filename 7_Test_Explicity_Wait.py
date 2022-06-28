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

driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
driver.maximize_window()    #Maximizar ventana
t=.5
#driver.implicitly_wait(5)
btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='#'][contains(.,'No, thanks!')]")))
btn.click()
driver.find_element(By.XPATH,"//input[contains(@id,'user-message')]").send_keys("Bienvenidos a Selenium" + Keys.TAB + Keys.ENTER)
time.sleep(t)
driver.find_element(By.XPATH,"//input[contains(@id,'sum1')]").send_keys("5" + Keys.TAB + "4" + Keys.TAB + Keys.ENTER)
time.sleep(t)
driver.close()