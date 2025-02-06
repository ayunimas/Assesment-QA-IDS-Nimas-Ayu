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

#mencari element menggunakan nama dan di isi dengan "ryobranch"
driver.find_element(By.NAME, "username").send_keys("ryobranch") 

#menutup halaman website
driver.quit()