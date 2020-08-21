# Web driver libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Driver
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

# Enter to youtube
driver.get("https://www.youtube.com/")

# Log in
#try:

login = driver.find_element_by_link_text('Iniciar sesión')
login.click()
'''
login = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.LINK_TEXT, 'Iniciar sesión'))
).click()
'''

#except:
#    driver.quit()
