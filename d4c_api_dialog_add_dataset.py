# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd4c_api_dialog_add_dataset.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject
import requests
import json

class Dialog(QObject):
        datasetEntered = QtCore.pyqtSignal(str, str, str)

class Ui_Dialog(object):
    
    def __init__(self):
        
        self.dataset_entered = Dialog()
        self.themes_checkboxes = []
        self.tags_checkboxes = []
        self.scrollLayout2 = QtWidgets.QVBoxLayout()
        self.scrollLayout3 = QtWidgets.QVBoxLayout()
    
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(612, 516)
        self.newDatasetName = QtWidgets.QLineEdit(Dialog)
        self.newDatasetName.setGeometry(QtCore.QRect(40, 120, 291, 20))
        self.newDatasetName.setObjectName("newDatasetName")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 261, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.checkPrivate = QtWidgets.QCheckBox(Dialog)
        self.checkPrivate.setGeometry(QtCore.QRect(40, 200, 70, 17))
        self.checkPrivate.setObjectName("checkPrivate")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(410, 480, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 150, 291, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 100, 141, 16))
        self.label_3.setObjectName("label_3")
        self.orgCombobox = QtWidgets.QComboBox(Dialog)
        self.orgCombobox.setGeometry(QtCore.QRect(40, 170, 291, 22))
        self.orgCombobox.setObjectName("orgCombobox")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(170, 50, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(170, 70, 291, 22))
        self.comboBox.setObjectName("comboBox")
        self.hideInCatalogue = QtWidgets.QCheckBox(Dialog)
        self.hideInCatalogue.setGeometry(QtCore.QRect(370, 120, 151, 17))
        self.hideInCatalogue.setObjectName("hideInCatalogue")
        self.hideInGraph = QtWidgets.QCheckBox(Dialog)
        self.hideInGraph.setGeometry(QtCore.QRect(370, 150, 211, 17))
        self.hideInGraph.setObjectName("hideInGraph")
        self.hideInMap = QtWidgets.QCheckBox(Dialog)
        self.hideInMap.setGeometry(QtCore.QRect(370, 180, 211, 17))
        self.hideInMap.setObjectName("hideInMap")
        self.pushExit = QtWidgets.QPushButton(Dialog)
        self.pushExit.setGeometry(QtCore.QRect(510, 480, 91, 31))
        self.pushExit.setObjectName("pushExit")
        self.themeScrollArea = QtWidgets.QScrollArea(Dialog)
        self.themeScrollArea.setGeometry(QtCore.QRect(70, 250, 191, 221))
        self.themeScrollArea.setWidgetResizable(True)
        self.themeScrollArea.setObjectName("themeScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 189, 219))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.themeScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea = QtWidgets.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(340, 250, 201, 221))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 199, 219))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(70, 230, 47, 13))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(340, 230, 51, 16))
        self.label_6.setObjectName("label_6")
        self.keywordSearch = QtWidgets.QLineEdit(Dialog)
        self.keywordSearch.setGeometry(QtCore.QRect(390, 230, 151, 20))
        self.keywordSearch.setObjectName("keywordSearch")
        self.keywordSearch.setPlaceholderText("Rechercher un mot-clef")


        self.pushButton.clicked.connect(self.createDataset)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Créer un Jeu de Donnée"))
        self.label.setText(_translate("Dialog", "Créer un nouveau Jeu de Donnée :"))
        self.checkPrivate.setText(_translate("Dialog", "Privée"))
        self.pushButton.setText(_translate("Dialog", "Créer"))
        self.label_2.setText(_translate("Dialog", "Organisation :"))
        self.label_3.setText(_translate("Dialog", "Nom du Jeu de donnée :"))
        self.label_4.setText(_translate("Dialog", "Site D4C actuel :"))
        self.hideInCatalogue.setText(_translate("Dialog", "Cacher dans le catalogue"))
        self.hideInGraph.setText(_translate("Dialog", "Cacher dans l\'interface des graphiques"))
        self.hideInMap.setText(_translate("Dialog", "Cacher dans l\'interface des cartes"))
        self.pushExit.setText(_translate("Dialog", "Annuler"))
        self.label_5.setText(_translate("Dialog", "Thèmes :"))
        self.label_6.setText(_translate("Dialog", "Mot-clefs :"))
        self.keywordSearch.setPlaceholderText(_translate("changeMetadatas", "Rechercher un mot-clef"))
    
    def createDataset(self):

        name = self.newDatasetName.text()

        org = self.orgCombobox.currentText()

        if self.checkPrivate.isChecked():
            private = 'true'
        else:
            private = 'false'

        self.dataset_entered.datasetEntered.emit(name, org, private)

        

