#Melakukan import package yang di butuhkan
from selenium.webdriver.common.by import By
from selenium import webdriver
#WebDriverWait memungkinkan kita memberi waktu ekstra untuk mencari elemen
from selenium.webdriver.support.ui import WebDriverWait
#expected_conditions (EC) menyediakan kondisi yang perlu dipenuhi agar elemen bisa diklik
from selenium.webdriver.support import expected_conditions as EC

#agar saat run tidak langsung terclose 
#membuat variable bernama options untuk membuka clas chromeoptions
options = webdriver.ChromeOptions()
#memanggil variable options dan membuka isi chrome options bernama add_experimental_option
#dan di tambahkan argumen 
options.add_experimental_option('detach', True)

#membuat variable baru namanya driver 
#kemudian webdrivernya di panggil
#menambahkan argumen bahwa options sama dengan variable options yang telah dibuat
driver = webdriver.Chrome(options=options)

#membuka alamat website
#pakai get karena mengambil api url web yang akan kita buka
driver.get('https://stg-sob.ids.id/auth/login') 

#mencari elemen menggunakan name "username" dan di isi "ryobranch"
driver.find_element(By.NAME, "username").send_keys("ryobranch") 

#mencari elemen menggunakan path dengan elemen button, dan atribut type=button di lanjutkan dengan aksi clik/tekan
driver.find_element(By.XPATH, "//button[@type='button']").click()

#mencari elemen menggunakan name "password" dan di isi "Test_1234"
driver.find_element(By.NAME, "password").send_keys("Test_1234") 

#mencari elemen menggunakan path dengan elemen button, dan atribut type=submit di lanjutkan dengan aksi clik/tekan
driver.find_element(By.XPATH, "//button[@type='submit']").click()

#membuat variable wait dan memanggil webdriver
#menambahkan argumen bahwa driver menunggu selama 10 detik
wait = WebDriverWait(driver, 10) 

#membuat variable baru bernama button untuk menyimpan kondisi yang wajib di penuhi 
#element_to_be_clickable yang akan mengecek apakah elemen bisa tekan
button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='MuiBox-root css-70qvj9']/*[name()='button'][@aria-label='open drawer']")))

#jika elemen bisa di tekan maka akan di tekan
button.click()

#menutup halaman website
driver.quit()