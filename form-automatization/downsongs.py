import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import requests
import csv
import re

def main():

    '''
    Get the titles of the first 100 songs
    '''
    songdata = pd.read_csv(r'C:\Users\serio\PycharmProjects\neurontest\csv-related\songs.csv', index_col=None, na_values=['NA'], delimiter=',', encoding="utf-8-sig")

    songdata.drop(songdata.index[100:], axis=0, inplace=True)

    titles = []

    for i in range(len(songdata)):
        titles.append(songdata['song.name'][i])

    titles[0] = 'Tanssi Vain'

    ytUrls(titles, songdata)




def ytUrls(titles, songdata):

    '''
    Download an array of songs
    '''

    # Driver declaration
    PATH = 'C:\Program Files (x86)\chromedriver.exe'
    driver = webdriver.Chrome(PATH)

    #options = webdriver.ChromeOptions()
    #options.add_argument("window-size=1200x600")

    urls = []
    errors = []

    i = 0

    for song in titles:

        driver.get('https://www.youtube.com')

        # Search song in YT
        search = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'search_query'))
        )
        search.click()
        search.send_keys(f'{songdata["song.artist"][i]} - {song}')
        search.send_keys(Keys.RETURN)

        sleep(2)
        #driver.execute_script("window.scrollTo(0, window.scrollY + 100)")
        #driver.implicitly_wait(3)

        try:
            # Click video
            WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.LINK_TEXT, song))
            ).click()

        except:
            print(f'Error at song: {song}')
            errors.append([song, driver.current_url])
            i += 1
            continue

        sleep(1)

        i += 1

        urls.append([song, driver.current_url])

        sleep(1)

    '''
    Convert the arrays of URLS and Errors to a doc .txt
    '''
    with open('ytsongs.csv', 'w+'):

        writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for i in range(len(urls)):
            writer.writerow(urls[i]: urls[j])

    with open('errorytsongs.csv''w+'):
        writer = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)

        for i in range(len(errors)):
            writer.writerow(errors[i]: errors[j])

    return



if __name__ == '__main__':
    main()






