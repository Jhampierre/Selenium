from selenium import webdriver
from selenium.webdriver.chrome.service import Service
ser = Service("C:\Drivers\chromedriver.exe")
op = webdriver.ChromeOptions()
#Inicializar el driver
driver = webdriver.Chrome(service=ser, options=op)

driver.get("https://demoqa.com/text-box")

print("Bienvenido a " + driver.title)

driver.close()