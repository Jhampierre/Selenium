from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #Para el find
from selenium.webdriver.common.keys import Keys #Para el TAB
import time #Para el sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select    #Escoger opciones
ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
op.add_argument('--ignore-ssl-errors=yes')  #Ignorar certificados
op.add_argument('--ignore-certificate-errors')
#Inicializar el driver
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
driver.maximize_window()    #Maximizar ventana
t=2
driver.implicitly_wait(5)
#dias = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[contains(@id,'select-demo')]")))
diaSelect = driver.find_element(By.XPATH,"//select[contains(@id,'select-demo')]")
ds = Select(diaSelect)  #agarrar las opciones

#forma 1 de seleccionar
ds.select_by_visible_text("Monday")
time.sleep(t)
#forma 2 de seleccionar
ds.select_by_index(5)
time.sleep(t)
#forma 3 de seleccionar
ds.select_by_value("Saturday")
time.sleep(t)

driver.execute_script("window.scrollTo(0,300)")
time.sleep(1)

ciudad = Select(driver.find_element(By.ID,"multi-select"))
ciudad.select_by_index(0)
time.sleep(1)
ciudad.select_by_index(2)
time.sleep(1)
ciudad.select_by_index(4)
time.sleep(1)
ciudad.select_by_index(6)
time.sleep(1)
driver.close()