from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.page_load_strategy = 'eager'
login_url = 'https://www.instagram.com/direct/inbox/'

def purchase(username, password, us_teman, text):
    print("----- Borneo Kalsel ------")
    print("-- Bot Auto While DM IG --\n")
    print("Bot Sedang Berjalan\n")
    driver = webdriver.Firefox(executable_path = 'webdriver/geckodriver.exe', options = options)
    wait = WebDriverWait(driver, 10)
    
    driver.get(login_url)
    wait.until(presence_of_element_located((By.NAME, 'username')))
    driver.find_element_by_name('username').send_keys(username)
    driver.find_element_by_name('password').send_keys(password + Keys.RETURN)
    print("----- Berhasil Login ------\n")
    wait.until(presence_of_element_located((By.CLASS_NAME, 'xWeGp')))
    driver.find_element_by_class_name('xWeGp').click()   
    wait.until(presence_of_element_located((By.CLASS_NAME, 'aOOlW')))
    driver.find_element_by_class_name('aOOlW').click() 
    wait.until(presence_of_element_located((By.CLASS_NAME, 'QBdPU ')))
    driver.find_element_by_class_name('QBdPU ').click() 
    wait.until(presence_of_element_located((By.NAME, 'queryBox')))
    driver.find_element_by_name('queryBox').send_keys(us_teman)
    wait.until(presence_of_element_located((By.CLASS_NAME, 'glyphsSpriteCircle__outline__24__grey_2 ')))
    driver.find_element_by_class_name('glyphsSpriteCircle__outline__24__grey_2 ').click()
    wait.until(presence_of_element_located((By.CLASS_NAME, 'rIacr')))
    driver.find_element_by_class_name('rIacr').click() 
    wait.until(presence_of_element_located((By.CLASS_NAME, 'aOOlW')))
    driver.find_element_by_class_name('aOOlW').click()  
    i = 10
    while i < 5: # ganti 5 jadi banyak pesan dikirim
        print('Telah Terkirim ')
        print(i)
        i += 1
        driver.find_element_by_xpath("//textarea[@placeholder='Message...']").send_keys(text + Keys.RETURN)
    print('Selesai')

username = '' # isi dengan username
us_teman = '' # isi dengan username teman
password = '' # isi dengan password 
text     = '' # isi pesannya
purchase(username, password, us_teman, text)
