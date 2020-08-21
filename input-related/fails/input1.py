import requests
import re

def main():
    my_api_key = "AIzaSyAN7JLUUQmBQkoFgadlogUrzemvyHqdG4w"
    my_cse_id = "93d294c6d1891ce69"


    google(input('El tiempo en: '), my_api_key, my_cse_id)


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
    print(url)

    # make the API request
    data = requests.get(url).json()

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

            # print the results
            # print("Description:", snippet)
            # print(url)
            print(snippet)
            break
main()