# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd4c_api_dialog_searchdataset.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject

class searchDataset(QObject):
        
        datasetEntered = QtCore.pyqtSignal(str)

class Ui_searchDataset(object):

    def __init__(self):
            
            self.search_dataset = searchDataset()
            self.themes_checkboxes = []
            self.tags_checkboxes = []
            self.alldatasets = []
            self.scrollLayout2 = QtWidgets.QVBoxLayout()
            self.scrollLayout3 = QtWidgets.QVBoxLayout()

    def setupUi(self, searchDataset):
        searchDataset.setObjectName("searchDataset")
        searchDataset.resize(794, 473)
        self.searchBarFilter = QtWidgets.QLineEdit(searchDataset)
        self.searchBarFilter.setGeometry(QtCore.QRect(20, 20, 311, 20))
        self.searchBarFilter.setObjectName("searchBarFilter")
        self.datasetAllList = QtWidgets.QListWidget(searchDataset)
        self.datasetAllList.setGeometry(QtCore.QRect(20, 80, 311, 351))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.datasetAllList.setFont(font)
        self.datasetAllList.setIconSize(QtCore.QSize(24, 24))
        self.datasetAllList.setGridSize(QtCore.QSize(0, 24))
        self.datasetAllList.setObjectName("datasetAllList")
        self.pushSelectDataset = QtWidgets.QPushButton(searchDataset)
        self.pushSelectDataset.setGeometry(QtCore.QRect(250, 440, 81, 23))
        self.pushSelectDataset.setObjectName("pushSelectDataset")
        self.pushFilter = QtWidgets.QPushButton(searchDataset)
        self.pushFilter.setGeometry(QtCore.QRect(620, 50, 131, 23))
        self.pushFilter.setObjectName("pushFilter")
        self.checkDisplayGeo = QtWidgets.QCheckBox(searchDataset)
        self.checkDisplayGeo.setGeometry(QtCore.QRect(360, 70, 151, 17))
        self.checkDisplayGeo.setObjectName("checkDisplayGeo")
        self.label = QtWidgets.QLabel(searchDataset)
        self.label.setGeometry(QtCore.QRect(350, 30, 431, 401))
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(searchDataset)
        self.label_2.setGeometry(QtCore.QRect(360, 40, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushClose = QtWidgets.QPushButton(searchDataset)
        self.pushClose.setGeometry(QtCore.QRect(710, 440, 75, 23))
        self.pushClose.setObjectName("pushClose")
        self.scrollArea_2 = QtWidgets.QScrollArea(searchDataset)
        self.scrollArea_2.setGeometry(QtCore.QRect(360, 110, 191, 311))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 189, 309))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.label_4 = QtWidgets.QLabel(searchDataset)
        self.label_4.setGeometry(QtCore.QRect(360, 90, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(searchDataset)
        self.label_5.setGeometry(QtCore.QRect(580, 90, 81, 16))
        self.label_5.setObjectName("label_5")
        self.scrollArea_3 = QtWidgets.QScrollArea(searchDataset)
        self.scrollArea_3.setGeometry(QtCore.QRect(580, 110, 191, 311))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 189, 309))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_4)
        self.comboBox = QtWidgets.QComboBox(searchDataset)
        self.comboBox.setGeometry(QtCore.QRect(20, 50, 311, 22))
        self.comboBox.setObjectName("comboBox")
        self.checkAz = QtWidgets.QCheckBox(searchDataset)
        self.checkAz.setGeometry(QtCore.QRect(510, 70, 51, 17))
        self.checkAz.setObjectName("checkAz")
        self.checkZa = QtWidgets.QCheckBox(searchDataset)
        self.checkZa.setGeometry(QtCore.QRect(560, 70, 51, 17))
        self.checkZa.setObjectName("checkZa")
        self.label.raise_()
        self.searchBarFilter.raise_()
        self.datasetAllList.raise_()
        self.pushSelectDataset.raise_()
        self.pushFilter.raise_()
        self.checkDisplayGeo.raise_()
        self.label_2.raise_()
        self.pushClose.raise_()
        self.scrollArea_2.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.scrollArea_3.raise_()
        self.comboBox.raise_()
        self.checkAz.raise_()
        self.checkZa.raise_()
        self.pushSelectDataset.clicked.connect(self.selectDataset)
        self.datasetAllList.itemDoubleClicked.connect(self.selectDataset)
        self.retranslateUi(searchDataset)
        QtCore.QMetaObject.connectSlotsByName(searchDataset)

    def retranslateUi(self, searchDataset):
        _translate = QtCore.QCoreApplication.translate
        searchDataset.setWindowTitle(_translate("searchDataset", "Trouver un jeu de données"))
        self.searchBarFilter.setPlaceholderText(_translate("searchDataset", "Chercher un jeu de données"))
        self.pushSelectDataset.setText(_translate("searchDataset", "Sélectionner"))
        self.pushFilter.setText(_translate("searchDataset", "Réinitialiser les filtres"))
        self.checkDisplayGeo.setText(_translate("searchDataset", "Afficher uniquement GEO"))
        self.label_2.setText(_translate("searchDataset", "Filtres :"))
        self.pushClose.setText(_translate("searchDataset", "Fermer"))
        self.label_4.setText(_translate("searchDataset", "Thèmes : "))
        self.label_5.setText(_translate("searchDataset", "Mot-clé : "))
        self.comboBox.setPlaceholderText(_translate("searchDataset", "Choisir une organisation"))
        self.checkAz.setText(_translate("searchDataset", "A - z"))
        self.checkZa.setText(_translate("searchDataset", "Z - a"))


    def selectDataset(self):
        dataset = self.datasetAllList.currentItem()
        if dataset:
            dataset = self.datasetAllList.currentItem().text()
            self.search_dataset.datasetEntered.emit(dataset)
