#Melakukan import package yang di butuhkan
#di dalam selenium ada class bernama webdriver itu yang di import 
from selenium import webdriver

#jika path belum di masukan ke environment path pake ini
#from selenium.webdriver.chrome.service import Service as ChromeService
#buat variable baru namanya service yang digunakan untuk memanggil chromeservice dan memasukan path web drivernya
#service = ChromeService(executable_path="C:\webdriver\chromedriver.exe")
##kemudian webdrivernya di panggil dengan parameter service sama dengan memanggil variable service yang sudah dibuat
#driver = webdriver.Chrome(service=service)

#agar saat run tidak langsung terclose 
#membuat variable bernama options untuk membuka clas chromeoptions
options = webdriver.ChromeOptions()
#memanggil variable options dan membuka isi chrome options bernama add_experimental_option
#dan di tambahkan argumen 
options.add_experimental_option('detach', True)

#membuat variable baru namanya driver 
#kemudian webdrivernya di panggil
#menambahkan parameter/argumen options sama dengan variable options yang telah dibuat
driver = webdriver.Chrome(options=options)

#membuka alamat website
#pakai get karena mengambil api url web yang akan kita buka
driver.get('https://stg-sob.ids.id/auth/login')

#menutup halaman website
driver.quit()