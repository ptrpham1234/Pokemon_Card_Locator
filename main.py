#!/usr/bin/env python3
#############################################################################################################
# Project Name:         S3_Manager
# File Name:            main.py
# Author:               Peter Pham (pxp180041)
# Date Started:         08/10/2022
#
# Description:
#
#
#
# TODO: implement access key and secret key read in
# TODO: implement boto3 upload
# TODO: implement
#############################################################################################################

################# I M P O R T S #################
import re

import sys
import requests
from bs4 import BeautifulSoup
from gui import Ui_MainWindow
from PyQt6 import QtCore, QtGui, QtWidgets



base_url = "https://www.pokellector.com"
url_to_scrape = base_url + "/sets"


#############################################################################################################
# Function:            main
# Author:              Peter Pham (pxp180041)
# Date Started:        08/10/2022
#
# Description:
#
#############################################################################################################
def main():
    # assign required credentials
    # assign URL

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()



    # create document
    html_document = getHTMLdocument(url_to_scrape)

    # create soap object
    soup = BeautifulSoup(html_document, 'html.parser')

    # Get the names of the sets
    setList = set_name_getter(soup)

    # send the list to the UI here
    ui = Ui_MainWindow(MainWindow, setList)
    MainWindow.show()
    app.exec()

#############################################################################################################
# Function:            main
# Author:              Peter Pham (pxp180041)
# Date Started:        08/12/2022
#
# Description:
# function to extract html document from given url
#############################################################################################################
def getHTMLdocument(url):
    # request for HTML document of given url
    response = requests.get(url)

    # response will be provided in JSON format
    return response.text


#############################################################################################################
# Function:            main
# Author:              Peter Pham (pxp180041)
# Date Started:        08/12/2022
#
# Description:
# function to extract html document from given url
#############################################################################################################
def set_name_getter(soup):

    pokemonSets = list()

    for button in soup.find_all("a", class_="button"):

        setName = button.get("href").strip()
        setName = setName[1:-1].replace("-", " ")
        setName = setName.replace(" Expansion", "")
        pokemonSets.append(setName)


    return pokemonSets


#############################################################################################################
# Function:            main
# Author:              Peter Pham (pxp180041)
# Date Started:        08/12/2022
#
# Description:

#############################################################################################################
if __name__ == "__main__":
    main()

    # print(setPageURL)
    # cardSoup = BeautifulSoup(getHTMLdocument(setPageURL), "html.parser")
    # for pokemon in cardSoup.find_all("div", class_="plaque"):
    #     print(pokemon.text)