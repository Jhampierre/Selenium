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

driver.get("https://demoqa.com/text-box")
driver.maximize_window()    #Maximizar ventana

time.sleep(1)
#nom=driver.find_element_by_xpath("//input[contains(@id,'userName')]")
nom=driver.find_element(By.XPATH,"//input[@type='text' and @id='userName']")
nom.send_keys("Jhampierre")
nom.send_keys(Keys.TAB + "jhamcofer@gmail.com" + Keys.TAB + "direccion 1" + Keys.TAB + "direccion 2" + Keys.TAB + Keys.ENTER)

driver.execute_script("window.scrollTo(0,300)")
time.sleep(1)
driver.close()