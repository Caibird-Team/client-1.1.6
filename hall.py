# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets,Qt
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Hall(object):
    def setupUi(self, Dialog):

        self.hall_dialog=Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(761, 515)




        self.hall_background = QtWidgets.QLabel( self.hall_dialog)
        self.hall_background.setGeometry(QtCore.QRect(0, 0, 791, 521))
        png=QtGui.QPixmap("C:/Users/Python/Desktop/client 1.1.6/hall.jpg")
        self.hall_background.setObjectName("logo")
        self.hall_background.setPixmap(png)

        self.name = QtWidgets.QLabel(Dialog)
        self.name.setGeometry(QtCore.QRect(100, 110, 81, 31))
        png2=QtGui.QPixmap("C:/Users/Python/Desktop/client 1.1.6/pig.jpg")
        self.name.setPixmap(png)

        
        
        self.welcome = QtWidgets.QLabel(Dialog)
        self.welcome.setGeometry(QtCore.QRect(30, 10, 311, 31))
        self.welcome.setStyleSheet("color:yellow")

        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(16)
        self.welcome.setFont(font)
        self.welcome.setObjectName("welcome")
        self.wheather = QtWidgets.QLabel(Dialog)
        self.wheather.setGeometry(QtCore.QRect(250, 40, 211, 41))
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(12)
        self.wheather.setFont(font)
        self.wheather.setObjectName("wheather")
        self.wheather.setStyleSheet("color:yellow")

        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(12)

        # self.id_image.setFont(font)
        # self.id_image.setObjectName("id_image")
        self.touxiang = QtWidgets.QTextBrowser(Dialog)
        self.touxiang.setGeometry(QtCore.QRect(20, 100, 61, 51))
        self.touxiang.setObjectName("id_image")
        self.touxiang.setStyleSheet("background-image:url(C:/Users/Python/Desktop/client 1.1.6/pig.jpg)")

        
        
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(12)
        self.name.setFont(font)
        self.name.setObjectName("name")
        self.name.setStyleSheet("color:yellow")

        self.signature = QtWidgets.QLabel(Dialog)
        self.signature.setGeometry(QtCore.QRect(20, 140, 120, 60))
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(12)
        self.signature.setFont(font)
        self.signature.setObjectName("signature")
        self.signature.setStyleSheet("color:yellow")
        self.signature.setWordWrap(True)


        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(10, 410, 61, 31))
        self.label_7.setObjectName("label_7")
        self.cai_first = QtWidgets.QPushButton(Dialog)
        self.cai_first.setGeometry(QtCore.QRect(70, 380, 75, 23))
        self.cai_first.setObjectName("cai_first")
        self.cai_second = QtWidgets.QPushButton(Dialog)
        self.cai_second.setGeometry(QtCore.QRect(70, 400, 75, 23))
        self.cai_second.setObjectName("cai_second")
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(70, 420, 75, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.text_edit = QtWidgets.QLineEdit(Dialog)
        self.text_edit.setGeometry(QtCore.QRect(180, 380, 301, 71))
        self.text_edit.setObjectName("text_edit")
        
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(180, 110, 301, 231))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setStyleSheet("background-image:url(C:/Users/Python/Desktop/client 1.1.6/small.png)")
        self.more_caibird_button = QtWidgets.QPushButton(Dialog)
        self.more_caibird_button.setGeometry(QtCore.QRect(70, 460, 75, 23))
        self.more_caibird_button.setObjectName("more_caibird_button")
        self.send_all_button = QtWidgets.QPushButton(Dialog)
        self.send_all_button.setGeometry(QtCore.QRect(320, 470, 75, 23))
        self.send_all_button.setObjectName("send_all_button")
        self.send_caicai_button = QtWidgets.QPushButton(Dialog)
        self.send_caicai_button.setGeometry(QtCore.QRect(410, 470, 75, 23))
        self.send_caicai_button.setObjectName("send_caicai_button")
        self.exit_button = QtWidgets.QPushButton(Dialog)
        self.exit_button.setGeometry(QtCore.QRect(660, 480, 75, 23))
        self.exit_button.setObjectName("exit_button")
        self.caicai_label = QtWidgets.QLabel(Dialog)
        self.caicai_label.setGeometry(QtCore.QRect(540, 170, 191, 41))
        self.caicai_label.setStyleSheet("color:yellow")
        font = QtGui.QFont()
        font.setFamily("ADMUI3Lg")
        font.setPointSize(12)
        self.caicai_label.setFont(font)
        self.caicai_label.setObjectName("caicai_label")
        self.history_button = QtWidgets.QPushButton(Dialog)
        self.history_button.setGeometry(QtCore.QRect(410, 350, 75, 23))
        self.history_button.setObjectName("history_button")
        self.setting_botton = QtWidgets.QPushButton(Dialog)
        self.setting_botton.setGeometry(QtCore.QRect(540, 110, 75, 23))
        self.setting_botton.setObjectName("setting_botton")
        self.feedback_botton = QtWidgets.QPushButton(Dialog)
        self.feedback_botton.setGeometry(QtCore.QRect(640, 110, 75, 23))
        self.feedback_botton.setObjectName("feedback_botton")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(620, 90, 20, 81))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(540, 140, 181, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        
        self.caicai_text_browser = QtWidgets.QTextBrowser(Dialog)
        self.caicai_text_browser.setGeometry(QtCore.QRect(500, 230, 241, 221))
        self.caicai_text_browser.setObjectName("caicai_text_browser")
        self.caicai_text_browser.setStyleSheet("background-image:url(C:/Users/Python/Desktop/client 1.1.6/small.png)")
        


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.welcome.setText(_translate("Dialog", "欢迎来到菜鸟群聊大厅..."))
        self.wheather.setText(_translate("Dialog", "2019.1.1 北京，多云"))
        # self.id_image.setText(_translate("Dialog", "222"))
        self.name.setText(_translate("Dialog", "风儿"))
        self.signature.setText(_translate("Dialog", "签名:你是风儿，我是沙。。。"))


        self.label_7.setText(_translate("Dialog", "群聊列表"))
        self.cai_first.setText(_translate("Dialog", "菜鸟1号"))
        self.cai_second.setText(_translate("Dialog", "菜鸟2号"))
        self.pushButton_6.setText(_translate("Dialog", "菜鸟3号"))
        self.more_caibird_button.setText(_translate("Dialog", "更多菜鸟"))
        self.send_all_button.setText(_translate("Dialog", "发给群聊"))
        self.send_caicai_button.setText(_translate("Dialog", "发给小菜菜"))
        self.exit_button.setText(_translate("Dialog", "退出大厅"))
        self.caicai_label.setText(_translate("Dialog", "小菜菜有什么可以帮您?"))
        self.history_button.setText(_translate("Dialog", "消息记录"))
        self.setting_botton.setText(_translate("Dialog", "大厅设置"))
        self.feedback_botton.setText(_translate("Dialog", "问题反馈"))
        self.text_edit.setText('')

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    widget=QtWidgets.QWidget()
    ui=Hall()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())