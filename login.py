# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets,Qt
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Ui_login_Dialog(object):

    def setupUi(self, login_Dialog):


        self.login_dialog=login_Dialog
        login_Dialog.setObjectName("login_Dialog")
        login_Dialog.resize(300, 185)
        icon=QtGui.QPixmap('C:/Users/Python/Desktop/client 1.1.6/logo.png')
        login_Dialog.setWindowIcon(QIcon(icon))

        picture_label=QtWidgets.QLabel()
        self.logo = QtWidgets.QLabel(self.login_dialog)
        self.logo.setGeometry(QtCore.QRect(0, 0, 300, 53))
        png=QtGui.QPixmap("C:/Users/Python/Desktop/client 1.1.6/未标题-1.png")
        
        self.logo.setObjectName("logo")
        self.logo.setPixmap(png)

        picture_label2=QtWidgets.QLabel()
        self.logo2 = QtWidgets.QLabel(self.login_dialog)
        self.logo2.setGeometry(QtCore.QRect(0, 53, 300, 132))
        png2=QtGui.QPixmap("C:/Users/Python/Desktop/client 1.1.6/背景图.png")
        self.logo2.setObjectName("logo")
        self.logo2.setPixmap(png2)
        

        self.user_account = QtWidgets.QLineEdit(self.login_dialog)
        self.user_account.setGeometry(QtCore.QRect(40,70,221,25))
        self.user_account.setObjectName("user_account")

        self.pwd_input = QtWidgets.QLineEdit(self.login_dialog)
        self.pwd_input.setGeometry(QtCore.QRect(40,105,221,25))
        self.pwd_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwd_input.setObjectName("pwd_input")

        self.login_button = QtWidgets.QPushButton(self.login_dialog)
        self.login_button.setGeometry(QtCore.QRect(60,140,170,35))
        self.login_button.setObjectName("login_button")


        self.exit_botton = QtWidgets.QPushButton(self.login_dialog)
        self.exit_botton.setGeometry(QtCore.QRect(243,150,40,23))
        self.exit_botton.setObjectName("exit_botton")

        self.register_botton = QtWidgets.QPushButton(self.login_dialog)
        self.register_botton.setGeometry(QtCore.QRect(8,150,40,23))
        self.register_botton.setObjectName("register_botton")

        self.retranslateUi(login_Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.login_dialog)




    def retranslateUi(self, login_Dialog):
        _translate = QtCore.QCoreApplication.translate
        login_Dialog.setWindowTitle(_translate("login_Dialog", "BirdChat"))
        # self.welcome.setText(_translate("login_Dialog", "菜鸟聊天系统登录界面"))
        self.user_account.setPlaceholderText(_translate("login_Dialog", "请输入账号"))
        self.pwd_input.setPlaceholderText(_translate("login_Dialog", "请输入密码"))
        self.login_button.setText(_translate("login_Dialog", "登录"))
        self.exit_botton.setText(_translate("login_Dialog", "退出"))
        self.register_botton.setText(_translate("login_Dialog", "注册"))

    


