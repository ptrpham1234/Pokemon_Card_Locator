from bs4 import BeautifulSoup
import requests
from gui import Ui_MainWindow
from PyQt6 import QtCore, QtGui, QtWidgets



# function to extract html document from given url
def getHTMLdocument(url):
    # request for HTML document of given url
    response = requests.get(url)

    # response will be provided in JSON format
    return response.text

def main():
    # assign required credentials
    # assign URL
    base_url = "https://www.pokellector.com"
    url_to_scrape = base_url + "/sets"

    # create document
    html_document = getHTMLdocument(url_to_scrape)

    # create soap object
    soup = BeautifulSoup(html_document, 'html.parser')

    pokemonCount = 0

    with open("output.txt", "w") as file:

        for button in soup.find_all("a", class_="button"):
            setPageURL = base_url + button.get("href")

            print(setPageURL)
            cardSoup = BeautifulSoup(getHTMLdocument(setPageURL), "html.parser")
            for pokemon in cardSoup.find_all("div", class_="plaque"):
                print(pokemon.text)

                pokemonCount += 1

        print(pokemonCount)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    main()
    MainWindow.show()
    sys.exit(app.exec())