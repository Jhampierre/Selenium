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

driver.get("https://testpages.herokuapp.com/styled/file-upload-test.html")
driver.maximize_window()    #Maximizar ventana
t=.5
#dias = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//select[contains(@id,'select-demo')]")))

#Try - Except es para que continue con el test aunque un caso falle
try:
    Buscar = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@id,'fileinput')]")))
    Buscar = driver.find_element(By.XPATH,"//input[contains(@id,'fileinput')]")
    Buscar.send_keys("C://Users//Jhampierre//PycharmProjects//Curso_selenium//Imagenes//demo1.jpg") #Las diagonales van de esta manera

    driver.find_element(By.XPATH,"//input[contains(@id,'itsanimage')]").click()
    driver.find_element(By.XPATH,"//input[contains(@type,'submit')]").click()
    time.sleep(t)
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")

driver.close()