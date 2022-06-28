from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
op.add_argument('--ignore-ssl-errors=yes')  #Ignorar certificados
op.add_argument('--ignore-certificate-errors')
#Inicializar el driver
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://demoqa.com/text-box")
driver.maximize_window()    #Maximizar ventana
driver.implicitly_wait(15)  #Espera max 15s si es que alguno de los elementos falla, pero si funciona se corre normal
t=1
time.sleep(t)
#nom=driver.find_element_by_xpath("//input[contains(@id,'userName')]")
nom=driver.find_element(By.XPATH,"//input[contains(@id,'userName')]")
nom.send_keys("Jhampierre")
#email=driver.find_element_by_xpath("//input[@id='userEmail']")
email=driver.find_element(By.XPATH,"//input[@id='userEmail']")
email.send_keys("jhamcofer@gmail.com")
addresst=driver.find_element(By.XPATH,"//textarea[@id='currentAddress']").send_keys("Este es un test")
address2=driver.find_element(By.XPATH,"//textarea[@id='permanentAddress']").send_keys("Calle t Mz K")
time.sleep(t)
driver.execute_script("window.scrollTo(0,300)") #Quitar el anuncio, se ejecuta una funcion de Jscript. Scroll down
time.sleep(t)
driver.find_element(By.XPATH,"//button[@id='submit']").click()
time.sleep(t)
driver.close()