#Melakukan import package yang di butuhkan
#di dalam selenium ada class bernama webdriver itu yang di import 
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#agar saat run tidak langsung terclose 
#membuat variable bernama options untuk membuka clas chromeoptions
options = webdriver.ChromeOptions()
#memanggil variable options dan membuka isi chrome options bernama add_experimental_option
#dan di tambahkan argumen 
options.add_experimental_option('detach', True)

#membuat variable baru namanya driver 
#kemudian webdrivernya di panggil
#menambahkan argumen options sama dengan variable options yang telah dibuat
driver = webdriver.Chrome(options=options)

#membuka alamat website
#pakai get karena mengambil api url web yang akan kita buka
driver.get('https://stg-sob.ids.id/auth/login') 


driver.find_element(By.NAME, "username").send_keys("ryobranch") 
driver.find_element(By.XPATH, "//button[@type='button']").click()
driver.find_element(By.NAME, "password").send_keys("Test_1234") 
driver.find_element(By.XPATH, "//button[@type='submit']").click()
wait = WebDriverWait(driver, 10) 
button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='MuiBox-root css-70qvj9']/*[name()='button'][@aria-label='open drawer']")))
button.click()


driver.find_element(By.XPATH, "//span[text()='SetorKu']").click()
driver.find_element(By.XPATH, "//span[text()='Bulk Upload']").click()

time.sleep(2)

#TC27
wait = WebDriverWait(driver, 10) 
button_add = wait.until(EC.element_to_be_clickable((By.ID, "button-add")))
button_add.click()

time.sleep(2)

#TC 28
driver.find_element(By.XPATH, "//button[normalize-space()='SUBMIT']").click()

time.sleep(2)

#TC29
driver.find_element(By.NAME, "filename").send_keys("Sucipto")
driver.find_element(By.XPATH, "//button[normalize-space()='SUBMIT']").click()

time.sleep(2)

#TC30 
wait = WebDriverWait(driver, 10) 
button_add = wait.until(EC.element_to_be_clickable((By.ID, "button-add")))
button_add.click()
driver.find_element(By.XPATH, "//button[normalize-space()='CANCEL']").click()
