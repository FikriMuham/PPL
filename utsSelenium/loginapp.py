from lib2to3.pgen2 import driver
from selenium import webdriver

#driver = webdriver.Chrome()

driver = webdriver.Chrome(executable_path='C:\chromedriver_win32/chromedriver.exe')
driver.get("https://syncnau.poltektegal.ac.id/login")

##valid
driver.find_element_by_name("usename").send_keys("19090126")
driver.find_element_by_id("password").send_keys("12052001")
driver.find_element_by_id("submit").click()

##Invalid
#driver.find_element_by_name("username").send_keys("19090126")
#driver.find_element_by_id("password").send_keys("fikri12")
#driver.find_element_by_id("submit").click()

