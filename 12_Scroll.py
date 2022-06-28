from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By #Para el find
from selenium.webdriver.common.keys import Keys #Para el TAB
import time #Para el sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select    #Escoger opciones
from selenium.common.exceptions import TimeoutException #Agregar la excepcion

ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
op.add_argument('--ignore-ssl-errors=yes')  #Ignorar certificados
op.add_argument('--ignore-certificate-errors')
#Inicializar el driver
driver = webdriver.Chrome(service=ser, options=op)

t=3

driver.get("https://pixabay.com/es/")
driver.maximize_window()    #Maximizar ventana
time.sleep(t)

#driver.execute_script("window.scrollTo(0,1000)")


#Try - Except es para que continue con el test aunque un caso falle
try:
    Buscar = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/es/images/search/?order=ec']")))
    Buscar=driver.find_element(By.XPATH,"//a[@href='/es/images/search/?order=ec']")
    ir=driver.execute_script("arguments[0].scrollIntoView();",Buscar)   #Se va al elemento deseado
    time.sleep(t)

except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")


driver.close()