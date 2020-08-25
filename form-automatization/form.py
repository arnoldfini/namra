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

class Song:

   i = 0

   @classmethod
   def counter(cls):

      if cls.i == 0:

         opts = webdriver.ChromeOptions()
         opts.add_experimental_option("detach", True)

         global driver
         driver = webdriver.Chrome('C:\\Program Files (x86)\\chromedriver.exe', options=opts)
         driver.maximize_window()

   def __init__(self, song, artist):

      self.title = song

      self.emotions = self.atributes()

      Song.counter()

      self.yturl = self.url(song, artist)

      Song.i += 1

   def atributes(self):

      emotions = emodict()
      emo = []

      for key, value in emotions.items():
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

         sleep(1)

         url = driver.current_url


      except:

         try:
            WebDriverWait(driver, 3).until(
               EC.element_to_be_clickable((By.LINK_TEXT, f'{artist} - {song}'))
            ).click()

            sleep(1)

            url = driver.current_url

         except:

            url = 'ERROR!'
            print(f'Error on song: {song}')



      return url

