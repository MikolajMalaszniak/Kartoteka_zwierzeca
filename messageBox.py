from PyQt5 import QtWidgets


def messagebox(title, message, icon):
    mess = QtWidgets.QMessageBox()
    mess.setWindowTitle(title)
    mess.setText(message)
    if icon == 'Information':
        mess.setIcon(QtWidgets.QMessageBox.Information)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
    elif icon == "Warning":
        mess.setIcon(QtWidgets.QMessageBox.Warning)
        mess.setStandardButtons(QtWidgets.QMessageBox.Cancel)
    mess.exec_()