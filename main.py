from bs4 import BeautifulSoup
import requests
import re


# function to extract html document from given url
def getHTMLdocument(url):
    # request for HTML document of given url
    response = requests.get(url)

    # response will be provided in JSON format
    return response.text


# assign required credentials
# assign URL
url_to_scrape = "https://www.pokellector.com/sets"

# create document
html_document = getHTMLdocument(url_to_scrape)

# create soap object
soup = BeautifulSoup(html_document, 'html.parser')

with open("output.txt", "w") as file:
    source = soup.find_all("a", class_="button")
    print("done")