from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome import service
from time import sleep
from emotions import *

'''
To scroll down

driver.execute_script("window.scrollTo(0, window.scrollY + 100)")
driver.implicitly_wait(3)
'''

global username
username = 'arnauperello2003'

global password
password = 'arni_96esp'


def slow_typing(element, text):
   for character in text:
      element.send_keys(character)
      time.sleep(0.3)


def Form(username, password):

   # webdriver_service = service.Service('C:\\Program Files (x86)\\operadriver.exe')
   # webdriver_service.start()
   # self.driver = webdriver.Remote(webdriver_service.service_url, webdriver.DesiredCapabilities.OPERA)
   opts = webdriver.ChromeOptions()
   opts.add_experimental_option("detach", True)

   global driver
   driver = webdriver.Chrome('C:\\Program Files (x86)\\chromedriver.exe', options=opts)
   driver.maximize_window()

   driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent%27')

   sleep(3)

   driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
   driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
   driver.find_element_by_xpath('//*[@id="identifierNext"]').click()

   sleep(3)

   driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
   driver.find_element_by_xpath('//*[@id="passwordNext"]').click()

   sleep(2)

   driver.get('https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiziqqn9KvrAhWh8uAKHQmqAIsQFjABegQIAhAB&url=https%3A%2F%2Fdocs.google.com%2Fforms%2Fu%2F0%2F&usg=AOvVaw3ymUTIOucUumzj_sd1Nax6')

   sleep(5)

   # Enter to form
   driver.find_element_by_xpath('//*[@class="docs-homescreen-grid-item-thumbnail"]').click()
   #driver.find_element_by_id(':1u').click()

class Song:

   def __init__(self, song, artist):

      self.title = song

      self.emotions = atributes()

      self.url = url(song, artist)

   def atributes(self):

      emotions = emodict()
      emo = []

      for key, value in emotions:
         emo.append(key)

      return emo

   def url(self, song, artist):

      driver.get('https://www.youtube.com')

      # Search song in YT
      search = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.NAME, 'search_query'))
      )
      search.click()
      search.send_keys(f'{artist} - {song}')
      search.send_keys(Keys.RETURN)

      sleep(2)
      # driver.execute_script("window.scrollTo(0, window.scrollY + 100)")
      # driver.implicitly_wait(3)

      try:
         # Click video
         WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.LINK_TEXT, song))
         ).click()

      except:
         pass

      sleep(1)

      i += 1

      return url, error

class FillForm:

   i = 0

   @classmethod
   def openChrome(cls):
      if cls.i == 0:
         Form(username, password)

   @classmethod
   def song_counter(cls):
      cls.i += 1


   def __init__(self, song):

      FillForm.openChrome()
      FillForm.song_counter()

      self.section(song)


   def section(self, song):

      if FillForm.i > 0:
         driver.execute_script("window.scrollTo(0, window.scrollY + 100)")
         driver.implicitly_wait(2)

      self.sect = driver.find_element_by_xpath('//*[@class="appsMaterialWizButtonEl appsMaterialWizButtonPapericonbuttonEl appsMaterialWizButtonPapericonbuttonLight freebirdFormeditorViewFatMenuItem"]').click()
      self.sect.send_keys(song)
      self.sect.send_keys(Keys.RETURN)

FillForm('Lol')
FillForm('XD')

