#Melakukan import package yang di butuhkan
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

#TC18

driver.find_element(By.NAME, "username").send_keys("ryobranch") 
driver.find_element(By.XPATH, "//button[@type='button']").click()
driver.find_element(By.NAME, "password").send_keys("Test_1234") 
driver.find_element(By.XPATH, "//button[@type='submit']").click()
wait = WebDriverWait(driver, 10) 
button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='MuiBox-root css-70qvj9']/*[name()='button'][@aria-label='open drawer']")))
button.click()

driver.find_element(By.XPATH, "//span[text()='SetorKu']").click()
driver.find_element(By.XPATH, "//span[text()='Partner Transaction']").click()

wait = WebDriverWait(driver, 10) 
filter = wait.until(EC.element_to_be_clickable((By.ID, "button-filter")))
filter.click()

#TC19

wait = WebDriverWait(driver, 10) 
fromDate=wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Choose date, selected date is Jan 6, 2025']")))
fromDate.click()

driver.find_element(By.XPATH, "//button[normalize-space()='1']").click()

#menutup halaman website
#driver.quit()