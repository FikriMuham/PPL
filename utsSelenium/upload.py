from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\chromedriver_win32/chromedriver.exe')

driver.get("https://syncnau.poltektegal.ac.id/profil")

driver.find_element_by_name("user_foto").send_keys("D:\KULIAH POLTEK_HARBER\Semester\Semester 6\bu fina\Selenium\SS\1.JPG")
driver.find_element_by_name("simpan_foto").click()
