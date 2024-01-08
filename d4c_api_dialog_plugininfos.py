# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd4c_api_dialog_plugininfos.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_pluginInfos(object):
    def setupUi(self, pluginInfos):
        self.plugin_dir = os.path.dirname(__file__)
        pluginInfos.setObjectName("pluginInfos")
        pluginInfos.resize(460, 300)
        self.label_pluginversion = QtWidgets.QLabel(pluginInfos)
        self.label_pluginversion.setGeometry(QtCore.QRect(10, 60, 441, 231))
        self.label_pluginversion.setFrameShape(QtWidgets.QFrame.Box)
        self.label_pluginversion.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_pluginversion.setLineWidth(1)
        self.label_pluginversion.setOpenExternalLinks(True)
        self.label_pluginversion.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.label_pluginversion.setObjectName("label_pluginversion")
        self.label = QtWidgets.QLabel(pluginInfos)
        self.label.setGeometry(QtCore.QRect(150, 10, 41, 41))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(os.path.join(self.plugin_dir, 'img', 'd4c_icon.png')))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(pluginInfos)
        self.label_2.setGeometry(QtCore.QRect(190, 10, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(pluginInfos)
        QtCore.QMetaObject.connectSlotsByName(pluginInfos)

    def retranslateUi(self, pluginInfos):
        _translate = QtCore.QCoreApplication.translate
        pluginInfos.setWindowTitle(_translate("pluginInfos", "Informations du Plugin"))
        self.label_pluginversion.setText(_translate("pluginInfos", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">Détail de l\'extension </span><span style=\" font-weight:600;\">:</span> Cette extension utilise l\'API de Data4Citizen afin de</p><p>manipuler des Jeux de Données depuis Qgis.</p><p><span style=\" font-weight:600; text-decoration: underline;\">Auteur </span>: Matthieu Serek @ BPM-conseil<br/><br/><span style=\" font-weight:600; text-decoration: underline;\">Contact</span>: matthieu.serek@bpm-conseil.com</p><p><span style=\" font-weight:600; text-decoration: underline;\">Git</span> :<a href=\"https://github.com/Riyolait/d4c-extension\"><span style=\" text-decoration: underline; color:#0000ff;\"> https://github.com/Riyolait/d4c-extension</span></a></p><p><span style=\" font-weight:600; text-decoration: underline;\">BPM-Conseil</span> :<a href=\"http://www.bpm-conseil.com/fr\"><span style=\" text-decoration: underline; color:#0000ff;\"> http://www.bpm-conseil.com/fr</span></a></p><p><span style=\" font-weight:600; text-decoration: underline;\">Librairie(s) Python Externe</span> : cryptography</p><p><span style=\" font-weight:600; text-decoration: underline;\">Version </span>: v1.4</p></body></html>"))
        self.label_2.setText(_translate("pluginInfos", "Data4Citizen"))
