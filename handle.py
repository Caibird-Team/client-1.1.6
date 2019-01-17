from PyQt5.QtWidgets import  QMainWindow
from PyQt5.QtCore import QThread ,  pyqtSignal, QObject
from PyQt5 import QtCore
from login import *
from hall import *
from threading import Thread
import time
from send_recv import Send_recv
import socket
import time


class handle(object):#继承object类，相当于无继承

    def __init__(self):

        self.LoginWindow = QMainWindow()#配置登录窗口
        self.loginWin = Ui_login_Dialog()#实例化登录UI模块
        self.loginWin.setupUi(self.LoginWindow)#配置登录UI
        self.loginWin.login_button.clicked.connect(self.get_login_data)#配置按钮
        self.loginWin.exit_botton.clicked.connect(self.login_exit)

        self.hall_window=QMainWindow()#配置大厅窗口
        self.hall_win=Hall()
        self.hall_win.setupUi(self.hall_window)
        self.hall_win.caicai_text_browser.append('我是小菜菜，有啥悄悄话都可以告诉我喔！')
        self.hall_win.send_all_button.clicked.connect(self.get_multi_chat_data)
        self.hall_win.send_caicai_button.clicked.connect(self.get_caicai_chat_data)
        self.hall_win.exit_button.clicked.connect(self.hall_exit)
        
        self.host='172.40.72.235'
        # self.host = socket.gethostbyname(socket.gethostname())#获取主机地址
        self.port = 11118
        self.address=(self.host,self.port)
        self.client=socket.socket()
        self.client.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.connState=False#配置服务器连接状态为关闭
        self.threadState=False#配置线程开启状态为关闭


        self.th = Send_recv(self.client)#实例化数据传输模块，传入socket参数
            

    def connectServer(self):#连接服务器

        if self.connState == False:
            try:
                self.client.connect(self.address) 
                self.connState = True
            except Exception:
                pass

            print('已连接服务器！')

        return self.connState#返回服务器连接状态
     
        
    def initUI(self):#启动线程
        if self.threadState == False:

            self.th.start()
            self.th.pressed.connect(self.display)#设置信号槽
            print('已开启子线程！')
            self.threadState = True
        
        return self.threadState#返回线程状态


    def display(self):#显示服务器传回的数据

        print('接收到来自服务器的数据：',self.th.msg)


        if self.th.msg[0]=='login':#如果服务器返回的是登录信息

            if self.th.msg[1] == 'OK':
                self.show_hall()
                self.login_exit()
            
            elif self.th.msg[1]=='NO':
                self.login_error()
        
        elif self.th.msg[0]=='rigister':#如果服务器返回的注册信息
            pass

        elif self.th.msg[0]=='multiChat':#如果服务器返回的群聊信息

            print(self.th.msg[0])
            print(self.th.msg[1])
            self.multi_msg=self.th.msg[1]

            name = self.th.msg[2]
            nowtime =  time.strftime("%H:%M:%S", time.localtime())
            header =name+nowtime+'\n'
            text=header+self.multi_msg+'\n'
            self.hall_win.textBrowser.append(text)

        elif self.th.msg[0]=='caicaiChat':#如果服务器返回的菜菜信息
            print(111)
            self.caicai_msg=self.th.msg[1]
            print('收到菜菜的数据：',self.caicai_chat_data)

            name ="小菜菜～(666666)       "
            nowtime =  time.strftime("%H:%M:%S", time.localtime())
            header =name+nowtime+'\n'
            text=header+self.caicai_msg+'\n'
            self.hall_win.caicai_text_browser.append(text)


    def showLogin(self):#显示登录框
        self.LoginWindow.show()

    def login_exit(self):#退出登录框
        self.loginWin.login_dialog.close()

    def show_hall(self):#显示大厅
        self.hall_window.show()

    def hall_exit(self):#退出大厅
        self.hall_win.hall_dialog.close()

    def tryConnServer(self):#连接服务器
        if not self.connectServer():
            QMessageBox.warning(self.LoginWindow,
                "警告",
                "无法连接服务器！",
                QMessageBox.Ok)
            return False
        return True


    def login_error(self):#如果用户名错误
        QMessageBox.warning(self.LoginWindow,
                    "警告",
                    "用户名或密码错误！",
                    QMessageBox.Ok)
    
    def send_to_server(self):#发送给服务器

        if self.tryConnServer():#如果连接上服务器

            if not self.initUI():#如果没有开启线程，先开启线程

                self.th.data_to_server(self.pack_data)

            else:
                self.th.data_to_server(self.pack_data)


    def get_login_data(self):#获取登录数据
        self.account=self.loginWin.user_account.text()
        self.password=self.loginWin.pwd_input.text()
        self.loginWin.user_account.setText('')
        self.loginWin.pwd_input.setText('')
        self.pack_data='login::%s::%s' % (self.account,self.password)
        print('准备打包发送的数据：',self.pack_data)
        self.send_to_server()

    def get_multi_chat_data(self):#获取群聊输入数据
        self.multi_chat_data=self.hall_win.text_edit.text()
        self.hall_win.text_edit.setText('')
        self.name ="xixi～(656723962)       "
        self.pack_data='multiChat::%s::%s'% (self.multi_chat_data,self.name)
        print('准备打包发送的数据：',self.pack_data)
        self.send_to_server()

    def get_caicai_chat_data(self):#获取菜菜输入数据

        self.caicai_chat_data=self.hall_win.text_edit.text()
        self.hall_win.text_edit.setText('')
        self.pack_data='caicaiChat::%s'%(self.caicai_chat_data)
        print('准备打包发送的数据：',self.pack_data)
        self.send_to_server()

        name ="xixi～(656723962)       "
        nowtime =  time.strftime("%H:%M:%S", time.localtime())
        header =name+nowtime+'\n'
        text=header+self.caicai_chat_data+'\n'
        self.hall_win.caicai_text_browser.append(text)



  

