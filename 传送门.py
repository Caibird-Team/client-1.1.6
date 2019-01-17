import sys
from PyQt5.QtWidgets import QApplication
from handle import handle
from send_recv import Send_recv

def main():

    app = QApplication(sys.argv)#配置程序


    ui_handler=handle()#实例化UI对象

    ui_handler.showLogin()#显示UI登录窗口

    sys.exit(app.exec_())#开启程序


if __name__ == "__main__":
    main()

