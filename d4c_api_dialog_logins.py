# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd4c_api_dialog_logins.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject
from qgis.PyQt.QtWidgets import QMessageBox
from .d4c_api_dialog_showsites import Ui_ShowSites
import os
import json
import requests

class LoginsWindow(QObject):
        loginsEntered = QtCore.pyqtSignal(str, str, str, bool)

class Ui_LoginsWindow(object):

    def __init__(self):
        
        self.logins_window = LoginsWindow() 

    def setupUi(self, LoginsWindow):
        
        self.plugin_dir = os.path.dirname(__file__)

        LoginsWindow.setObjectName("LoginsWindow")
        LoginsWindow.resize(400, 410)

        self.label = QtWidgets.QLabel(LoginsWindow)
        self.label.setGeometry(QtCore.QRect(60, 30, 21, 21))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(os.path.join(self.plugin_dir, 'img', 'internet_icon.png')))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(LoginsWindow)
        self.label_2.setGeometry(QtCore.QRect(80, 110, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setPixmap(QtGui.QPixmap(os.path.join(self.plugin_dir, 'img', 'usr_icon.png')))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(LoginsWindow)
        self.label_3.setGeometry(QtCore.QRect(80, 180, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setPixmap(QtGui.QPixmap(os.path.join(self.plugin_dir, 'img', 'pwd_icon.png')))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(LoginsWindow)
        self.label_4.setGeometry(QtCore.QRect(90, 30, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setScaledContents(False)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(LoginsWindow)
        self.label_5.setGeometry(QtCore.QRect(110, 110, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(LoginsWindow)
        self.label_6.setGeometry(QtCore.QRect(110, 180, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.siteUrl = QtWidgets.QLineEdit(LoginsWindow)
        self.siteUrl.setGeometry(QtCore.QRect(60, 60, 271, 20))
        self.siteUrl.setObjectName("siteUrl")

        self.user = QtWidgets.QLineEdit(LoginsWindow)
        self.user.setGeometry(QtCore.QRect(80, 130, 231, 20))
        self.user.setObjectName("user")

        self.password = QtWidgets.QLineEdit(LoginsWindow)
        self.password.setGeometry(QtCore.QRect(80, 200, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.password.setFont(font)
        self.password.setAutoFillBackground(False)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")

        self.validLoadedSite = QtWidgets.QPushButton(LoginsWindow)
        self.validLoadedSite.setGeometry(QtCore.QRect(280, 340, 81, 31))
        self.validLoadedSite.setCheckable(True)
        self.validLoadedSite.setObjectName("validLoadedSite")

        self.validLogins = QtWidgets.QPushButton(LoginsWindow)
        self.validLogins.setGeometry(QtCore.QRect(280, 240, 81, 31))
        self.validLogins.setCheckable(True)
        self.validLogins.setObjectName("validLogins")

        self.pushEditsites = QtWidgets.QPushButton(LoginsWindow)
        self.pushEditsites.setGeometry(QtCore.QRect(180, 340, 91, 31))
        self.pushEditsites.setObjectName("pushEditsites")

        self.label_7 = QtWidgets.QLabel(LoginsWindow)
        self.label_7.setGeometry(QtCore.QRect(70, 270, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.retranslateUi(LoginsWindow)

        self.comboBox = QtWidgets.QComboBox(LoginsWindow)
        self.comboBox.setGeometry(QtCore.QRect(70, 300, 231, 22))
        self.comboBox.setObjectName("comboBox")

        

        QtCore.QMetaObject.connectSlotsByName(LoginsWindow)

        self.validLogins.clicked.connect(self.getLogins)
        self.validLoadedSite.clicked.connect(self.getLoadedSite)
        self.pushEditsites.clicked.connect(self.openEditSites)
        


    def retranslateUi(self, LoginsWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginsWindow.setWindowTitle(_translate("LoginsWindow", "Connexion"))
        self.label_6.setText(_translate("LoginsWindow", "Mot de Passe :"))
        self.label_4.setText(_translate("LoginsWindow", "URL du Site :"))
        self.validLogins.setText(_translate("LoginsWindow", "Se connecter"))
        self.siteUrl.setPlaceholderText(_translate("LoginsWindow", "ex : https://website.data4citizen.com"))
        self.label_5.setText(_translate("LoginsWindow", "Utilisateur:"))
        self.label_7.setText(_translate("LoginsWindow", "Sites enregistrées :"))
        self.validLoadedSite.setText(_translate("LoginsWindow", "Se connecter"))
        self.pushEditsites.setText(_translate("LoginsWindow", "Gérer les sites"))


    def getLogins(self):
        site = self.siteUrl.text()
        user = self.user.text()
        pwd = self.password.text()

        if site.endswith('/') or site.endswith(' '):
            site = site[:-1]
        if site.startswith(' '):
            site = site[1:]
        site = site.lower()
        
        if user.endswith(' '):
            user = user[:-1]
        if user.startswith(' '):
            user = user[1:]
        
        if pwd.endswith(' '):
            pwd = pwd[:-1]
        if pwd.startswith(' '):
            pwd = pwd[1:]

        auth = (user, pwd)
        data = {
            'dataset_id': '',
        }
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded',  # Specify the data format (optional)
        }

        url = site + '/d4c/api/v1/dataset/find'
        response = requests.post(url, data=data, headers=headers, auth=auth)
        if response.status_code == 200:
            self.logins_window.loginsEntered.emit(site, user, pwd, False)
        else:
            self.show_error_message('Erreur lors de la connexion au site. Vérifiez vos identifiants.')
            


    def getLoadedSite(self):
        
        item = self.comboBox.currentIndex()
        sites_file_path = os.path.join(os.path.expanduser("~"), '.d4cplugin', 'sites.json')

        with open(sites_file_path, 'r') as json_file:
            data = json.load(json_file)
            sit = data['saved_sites']['sites'][item]['site_url']
            usr = data['saved_sites']['sites'][item]['username']
            pwd = data['saved_sites']['sites'][item]['password']

        self.logins_window.loginsEntered.emit(sit, usr, pwd, True)


    def openEditSites(self):
        self.windowSites = QtWidgets.QDialog()
        self.uiSites = Ui_ShowSites()
        self.uiSites.setupUi(self.windowSites)

        self.uiSites.listWidget.clear()
                # Set up the destination folder
        if not os.path.exists(os.path.expanduser("~") + '/.d4cplugin/'):
            os.makedirs(os.path.expanduser("~") + '/.d4cplugin/')
            
        sites_file_path = os.path.join(os.path.expanduser("~"), '.d4cplugin', 'sites.json')

        if os.path.exists(sites_file_path):
            with open(sites_file_path, 'r') as json_file:
                data = json.load(json_file)
                for sites in data['saved_sites']['sites']:
                    if sites['name'] == '':
                        self.uiSites.listWidget.addItem(sites['site_url'] + ' - ' + sites['username'])
                    else:
                        self.uiSites.listWidget.addItem(sites['name'])
        
        self.uiSites.pushClose.clicked.connect(self.windowSites.close)


        self.windowSites.exec_()
        self.updateComboBox()
    
    def updateComboBox(self):
        self.comboBox.clear()
        sites_file_path = os.path.join(os.path.expanduser("~"), '.d4cplugin', 'sites.json')

        if os.path.exists(sites_file_path):
            with open(sites_file_path, 'r') as json_file:
                data = json.load(json_file)
                for sites in data['saved_sites']['sites']:
                    if sites['name'] == '':
                        self.comboBox.addItem(sites['site_url'] + ' - ' + sites['username'])
                    else:
                        self.comboBox.addItem(sites['name'])


        
    def show_error_message(self, message):
        error_box = QMessageBox()
        error_box.setIcon(QMessageBox.Critical)
        error_box.setWindowTitle('Erreur')
        error_box.setText(message)
        error_box.exec_()