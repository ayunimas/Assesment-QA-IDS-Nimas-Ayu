#Melakukan import package yang di butuhkan
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

#TC 41
wait = WebDriverWait(driver, 10) 
profile=wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 css-1u0pmz0']")))
profile.click()

driver.find_element(By.XPATH, ("//li[text()='Change Password']")).click()

wait = WebDriverWait(driver, 10) 
password=wait.until(EC.element_to_be_clickable((By.NAME, "password")))
password.send_keys("Test_1234") 
driver.find_element(By.NAME, "newPassword").send_keys("Test_12345") 
driver.find_element(By.NAME, "confirmNewPassword").send_keys("Test_12345") 

time.sleep(2)

driver.find_element(By.ID, 'button-submit-form').click()

time.sleep(2)

#TC42
wait = WebDriverWait(driver, 10) 
profile=wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 css-1u0pmz0']")))
profile.click()

time.sleep(2)

driver.find_element(By.XPATH, ("//li[text()='Logout']")).click()
#driver.quit()
  


