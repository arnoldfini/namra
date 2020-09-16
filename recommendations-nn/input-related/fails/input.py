import math
from emotions import *
from googleapiclient import discovery
import pprint
import requests
import re
from time import sleep

def main():
    my_api_key = "AIzaSyAN7JLUUQmBQkoFgadlogUrzemvyHqdG4w"
    my_cse_id = "12b39448873aeb2c6"


    google('Alpicat', my_api_key, my_cse_id)


def google(query, API_KEY, SEARCH_ENGINE_ID):

    '''
    Search aspects
    '''

    # using the first page
    page = 1

    # constructing the URL
    # doc: https://developers.google.com/custom-search/v1/using_rest
    # calculating start, (page=2) => (start=11), (page=3) => (start=21)
    start = (page - 1) * 10 + 1
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"

    sleep(3)

    # make the API request
    data = requests.get(url).json()
    print(url)
    '''
    Weather aspects
    '''
    # get the result items
    search_items = data.get("items")


    # iterate over 10 results found
    for i, item in enumerate(str(search_items), start=1):

        if re.search(r'Weather Forecast', str(item)):

            # get the page title
            title = search_item.get("title")

            # page snippet
            snippet = search_item.get("snippet")

            # alternatively, you can get the HTML snippet (bolded keywords)
            html_snippet = search_item.get("htmlSnippet")

            # extract the page url
            link = search_item.get("link")
            print(link)
            # print the results
            # print("Description:", snippet)
            # print(url)
            print(snippet)
            break

    try:

        for i in range(len(snippet)):

            if re.search(r'°', snippet[i]):

                # Concatenate the two chars before the 'º' sign and convert to celsius
                degree = celsius(int(snippet[i - 2] + snippet[i - 1]))

                print(degree)
                break
        return degree

    except NameError:

        print('Could not find weather ')
        exit(0)






def celsius(degreefahr):
    # conversion from fahrenheit to celsius
    celsius = (degreefahr - 32)/1.8

    return celsius


if __name__ == '__main__':
    main()
