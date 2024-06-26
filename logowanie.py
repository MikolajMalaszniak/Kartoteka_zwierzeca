# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/logowanie.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap
from hashlib import md5
from db.db_conn import dbConnection
from messageBox import messagebox as msgbox
import json
from ast import literal_eval
from petappmain import Ui_MainWindow
from register import Ui_Form_register



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 200)
        Form.setMinimumSize(QtCore.QSize(640, 200))
        Form.setMaximumSize(QtCore.QSize(800, 300))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelImage = QtWidgets.QLabel(Form)
        self.labelImage.setMinimumSize(QtCore.QSize(200, 0))
        self.labelImage.setText("")
        self.labelImage.setObjectName("labelImage")
        self.horizontalLayout_2.addWidget(self.labelImage)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelEmail = QtWidgets.QLabel(Form)
        self.labelEmail.setObjectName("labelEmail")
        self.verticalLayout.addWidget(self.labelEmail)
        self.lineEditEmail = QtWidgets.QLineEdit(Form)
        self.lineEditEmail.setObjectName("lineEditEmail")
        self.verticalLayout.addWidget(self.lineEditEmail)
        self.labelPassword = QtWidgets.QLabel(Form)
        self.labelPassword.setObjectName("labelPassword")
        self.verticalLayout.addWidget(self.labelPassword)
        self.lineEditPassword = QtWidgets.QLineEdit(Form)
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.verticalLayout.addWidget(self.lineEditPassword)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBoxShowPassword = QtWidgets.QCheckBox(Form)
        self.checkBoxShowPassword.setObjectName("checkBoxShowPassword")
        self.horizontalLayout.addWidget(self.checkBoxShowPassword)
        self.checkBoxRemember = QtWidgets.QCheckBox(Form)
        self.checkBoxRemember.setObjectName("checkBoxRemember")
        self.horizontalLayout.addWidget(self.checkBoxRemember)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pushButtonLogin = QtWidgets.QPushButton(Form)
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.verticalLayout.addWidget(self.pushButtonLogin)
        self.pushButtonRegister = QtWidgets.QPushButton(Form)
        self.pushButtonRegister.setObjectName("pushButtonRegister")
        self.verticalLayout.addWidget(self.pushButtonRegister)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButtonLogin.clicked.connect(self.login)
        self.checkBoxShowPassword.toggled.connect(self.showpass)
        self.pushButtonRegister.clicked.connect(self.register)

        try:
            with open(".config", "r+t") as f:
                # checking if file is empty
                if f.read().strip():
                    f.seek(0)
                    l = f.readline()
                    l =json.loads(l)
                    user_conf = dict(l)
                    user_conf["rememberme"] = literal_eval(user_conf["rememberme"])
                    self.checkBoxRemember.setChecked(user_conf["rememberme"])
                    if user_conf["rememberme"]:
                        self.lineEditEmail.setText(user_conf["email"])
                        self.lineEditPassword.setText(user_conf["password"])
                else:
                    raise Exception("File is empty")
        except (Exception,FileNotFoundError) as e:
            print(f"config er: {e}")

    def showpass(self):
        if self.checkBoxShowPassword.isChecked():
            self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)

    def register(self):
        self.regWindow = QtWidgets.QWidget()
        self.uiwidget = Ui_Form_register()
        self.uiwidget.setupUi(self.regWindow)
        self.regWindow.show()
        Form.hide() # Hide the logowanie window

        # Connect the registration completion signal to a slot
        self.uiwidget.registerCompleted.connect(self.showLogowanieWindow)

    def showLogowanieWindow(self):
        Form.show()
        self.regWindow.close()

    def login(self):
        try:
            db = dbConnection()
            db.connect()
            if self.checkBoxRemember.isChecked:
                q = """select "id", "email", "password" from users where users.email=%s and users.password=%s;"""
            else:
                q = """select "id", "email" from users where users.email=%s and users.password=%s;"""
            email = self.lineEditEmail.text()
            password = md5(self.lineEditPassword.text().encode()).hexdigest()
            params = (email, password)
            rows=db.fetchone(q, params)
            if rows != None:
                with open(".config", "w") as f:
                    if self.checkBoxRemember.isChecked():
                        conf = json.dumps(dict({"id":str(rows[0]), "email":str(rows[1]), "password":self.lineEditPassword.text(), "rememberme":"True"}))
                    else:
                        conf = json.dumps(dict({"id":str(rows[0]), "email":str(rows[1]), "rememberme":"False"}))
                    f.write(str(conf))
                msgbox("Sucess login", f"You are logged as {rows[1]}", "Information")

                self.mainwin = QtWidgets.QMainWindow()
                self.ui = Ui_MainWindow()
                self.ui.setupUi(self.mainwin)
                self.mainwin.show()
                Form.close()
            else:
                msgbox("Failed", "Wrong email or password", "Warning")
        except Exception as e:
            msgbox("ERROR", f"{e}", "Warning")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Logowanie"))
        self.labelEmail.setText(_translate("Form", "E-mail"))
        self.labelPassword.setText(_translate("Form", "Password"))
        self.checkBoxShowPassword.setText(_translate("Form", "Show password"))
        self.checkBoxRemember.setText(_translate("Form", "Remember me"))
        self.pushButtonLogin.setText(_translate("Form", "Login"))
        self.pushButtonRegister.setText(_translate("Form", "Register"))
        
        pixmap = QPixmap('assets/padlock.png')
        self.labelImage.setPixmap(pixmap)  

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
