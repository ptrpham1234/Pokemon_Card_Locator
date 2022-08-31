# Form implementation generated from reading ui file '.\form.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIntValidator, QValidator
import requests
from bs4 import BeautifulSoup
import time

base_url = "https://www.pokellector.com"
url_to_scrape = base_url + "/sets"

class Ui_MainWindow(object):
    def __init__(self, MainWindow, setList):
        self.setCount = 0
        self.setCardCount = dict.fromkeys(setList, 0)
        self.setList = setList
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 208)
        MainWindow.setMinimumSize(QtCore.QSize(600, 0))
        MainWindow.setMaximumSize(QtCore.QSize(60000, 20800))
        MainWindow.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.setNameLabel = QtWidgets.QLabel(self.centralWidget)
        self.setNameLabel.setMaximumSize(QtCore.QSize(90, 24))
        self.setNameLabel.setObjectName("setNameLabel")
        self.gridLayout.addWidget(self.setNameLabel, 0, 0, 1, 1)
        self.searchLabel = QtWidgets.QLabel(self.centralWidget)
        self.searchLabel.setMaximumSize(QtCore.QSize(90, 24))
        self.searchLabel.setObjectName("searchLabel")
        self.gridLayout.addWidget(self.searchLabel, 1, 0, 1, 1)
        self.dropBox = QtWidgets.QComboBox(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dropBox.sizePolicy().hasHeightForWidth())
        self.dropBox.setSizePolicy(sizePolicy)
        self.dropBox.setMinimumSize(QtCore.QSize(240, 0))
        self.dropBox.setMaximumSize(QtCore.QSize(5000, 24))
        self.dropBox.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.dropBox.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.dropBox.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.dropBox.setMaxVisibleItems(100)
        self.dropBox.setSizeAdjustPolicy(QtWidgets.QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.dropBox.setObjectName("dropBox")
        self.dropBox.addItem("")
        self.gridLayout.addWidget(self.dropBox, 0, 1, 1, 1)
        self.calculateButton = QtWidgets.QPushButton(self.centralWidget)
        self.calculateButton.setMaximumSize(QtCore.QSize(130, 24))
        self.calculateButton.setObjectName("calculateButton")
        self.gridLayout.addWidget(self.calculateButton, 2, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.inputBox = QtWidgets.QLineEdit(self.centralWidget)
        self.inputBox.setMaximumSize(QtCore.QSize(100, 24))
        self.inputBox.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDigitsOnly|QtCore.Qt.InputMethodHint.ImhNoAutoUppercase)
        self.inputBox.setObjectName("inputBox")
        self.inputBox.setMaxLength(3)
        self.horizontalLayout_3.addWidget(self.inputBox)
        spacerItem = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.totalCardNumLabel = QtWidgets.QLabel(self.centralWidget)
        self.totalCardNumLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.totalCardNumLabel.setObjectName("totalCardNumLabel")
        self.horizontalLayout_3.addWidget(self.totalCardNumLabel)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        spacerItem1 = QtWidgets.QSpacerItem(30, 30, QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.outputDisplay = QtWidgets.QTextBrowser(self.centralWidget)
        self.outputDisplay.setObjectName("outputDisplay")
        self.horizontalLayout.addWidget(self.outputDisplay)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.dropBox, self.inputBox)
        MainWindow.setTabOrder(self.inputBox, self.calculateButton)
        MainWindow.setTabOrder(self.calculateButton, self.outputDisplay)

        self.main_func()

    #############################################################################################################
    # Function:            main
    # Author:              Peter Pham (pxp180041)
    # Date Started:        08/12/2022
    #
    # Description:
    # function to extract html document from given url
    #############################################################################################################
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pokemon Card Location"))
        self.setNameLabel.setText(_translate("MainWindow", "Set Name:"))
        self.searchLabel.setText(_translate("MainWindow", "Search Number:  "))
        self.dropBox.addItems(self.setList)
        self.dropBox.setItemText(0, "Select a set")
        self.calculateButton.setText(_translate("MainWindow", "Calculate"))
        self.totalCardNumLabel.setText(_translate("MainWindow", "sampleLabel"))
        self.outputDisplay.setHtml(_translate("MainWindow", "This is a text display"))

    #############################################################################################################
    # Function:            main
    # Author:              Peter Pham (pxp180041)
    # Date Started:        08/12/2022
    #
    # Description:
    # function to extract html document from given url
    #############################################################################################################
    def main_func(self):

        self.dropBox.activated.connect(self.getCardCount)

    #############################################################################################################
    # Function:            main
    # Author:              Peter Pham (pxp180041)
    # Date Started:        08/12/2022
    #
    # Description:
    # function to extract html document from given url
    #############################################################################################################
    def getCardCount(self):
        self.totalCardNumLabel.setText("Loading")
        selectedSet = self.dropBox.currentText()

        if self.setCardCount[selectedSet] == 0:
            url = base_url + "/" + selectedSet.replace(" ", "-") + "-Expansion/"

            html = self.getHTMLdocument(url)

            cardSoup = BeautifulSoup(html, "lxml")
            pokemonCount = len(cardSoup.find_all("div", class_="plaque"))
            self.totalCardNumLabel.setText("/ " + str(pokemonCount))
            self.setCardCount[selectedSet] = pokemonCount
        else:
            self.totalCardNumLabel.setText("/ " + str(self.setCardCount[selectedSet]))


    #############################################################################################################
    # Function:            main
    # Author:              Peter Pham (pxp180041)
    # Date Started:        08/12/2022
    #
    # Description:
    # function to extract html document from given url
    #############################################################################################################
    def getHTMLdocument(self, url):
        # request for HTML document of given url
        response = requests.get(url)

        # response will be provided in JSON format
        return response.text















