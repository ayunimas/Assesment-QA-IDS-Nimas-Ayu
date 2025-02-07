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
wait = WebDriverWait(driver, 10) 
button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='MuiBox-root css-70qvj9']/*[name()='button'][@aria-label='open drawer']")))
button.click()

driver.find_element(By.XPATH, "//span[text()='SetorKu']").click()
driver.find_element(By.XPATH, "//span[text()='Bulk Upload']").click()

wait = WebDriverWait(driver, 10) 
filter = wait.until(EC.element_to_be_clickable((By.ID, "button-filter")))
filter.click()

driver.find_element(By.XPATH, "//button[normalize-space()='REMOVE FILTER']").click() #hrs gini biar datanya muncul 

#driver.find_element(By.LINK_TEXT, "Detail").click()
#menunggu tabel untuk memuat max 10
wait = WebDriverWait(driver, 10)
table = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='grid']")))


# MUI tables biasanya pake divs with role="row" untuk baris tablenya
rows = table.find_elements(By.XPATH, ".//div[@role='row']")  
# target text yang mau dicari
target_text = "OTO_SOLO_Syifa_050225134403"
# mencari data di column yang ada text "OTO_SOLO_Syifa_050225134403"
# Asumsi nya 1 data
target_column_index = 1
for row in rows:
    # MUI tables biasanya pake divs with role="gridcell" untuk columns
    columns = row.find_elements(By.XPATH, ".//div[@role='gridcell']")
    
    if len(columns) > target_column_index:  # Memastikan columns yang dicari ada
        column_text = columns[target_column_index].text 
        if column_text == target_text:
            # Kalau column text nya sesuai, klik button detail
            detail_button = row.find_element(By.XPATH, ".//button[contains(text(), 'Detail')]")
            detail_button.click()
            break  # Karena udah ketemu di break biar looping nya stop


driver.find_element(By.ID, '').click() #buat nekan tombol add data

#TC35
driver.find_element(By.ID, '').click() #buat nekan tombol submit di add data

# close browser
driver.quit()
