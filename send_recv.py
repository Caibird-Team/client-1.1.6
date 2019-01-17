# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import  QMainWindow
import socket
from hall import *
from threading import Thread
from PyQt5.QtCore import pyqtSignal, QObject, QThread
import sys

class Send_recv(QThread):#继承Qthread线程类

    pressed=QtCore.pyqtSignal()#设置信号槽

    def __init__(self,sockfd):

        super(Send_recv,self).__init__()
        self.client=sockfd
        self.msg=''
        

    def run(self):
        while True:
            recv_data=self.client.recv(1024)
            data=recv_data.decode().split('::')
            self.msg=data
            self.pressed.emit()#发送给信号槽
   

    def data_to_server(self,data_pack):#将数据包发送给服务器
        self.text=data_pack
        self.client.send(self.text.encode())
        



        



            



            






