#Melakukan import package/library yang di butuhkan
from selenium.webdriver.common.by import By
from selenium import webdriver

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

#mencari element menggunakan name "username" dan di isi dengan "asdas"
driver.find_element(By.NAME, "username").send_keys("asdas")

#mencari element menggunakan path 
#dengan path mencari yang ber elemen button, kemudian memiliki atribut type=button 
#dan di lanjutkan dengan aksi clik/menekan(show pw)
driver.find_element(By.XPATH, "//button[@type='button']").click()

#mencari elemen berdasarkan name "password" dan di isi dengan "12345"
driver.find_element(By.NAME, "password").send_keys("12345") 

#mencari element menggunakan path 
#dengan path mencari yang ber elemen button, kemudian memiliki atribut type=submit 
#dan di lanjutkan dengan aksi clik/menekan(show pw)
driver.find_element(By.XPATH, "//button[@type='submit']").click() 

#menutup halaman website
driver.quit()