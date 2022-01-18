from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

global password
password = "password"
arguments = list(sys.argv)
arguments.remove(arguments[0])
if len(arguments)>1:
    if arguments[0] == "-c":
        arguments.remove("-c")
global strcmd
strcmd = str(" ".join(arguments))


def allow():
    os.system(f"echo {password} | sudo -E -S {strcmd}")


strcmd = str(" ".join(arguments))

class Window (QtWidgets.QDialog):
    def setupUi(self, Dialog, strcmd, sizex, sizey):
        Dialog.setObjectName("simple-sudo")
        Dialog.resize(sizex, sizey)
        Dialog.setMinimumSize(QtCore.QSize(355, 82))
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox, 0, QtCore.Qt.AlignLeft)
        self.retranslateUi(Dialog, strcmd)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def retranslateUi(self, Dialog, strcmd):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Simple Sudo", "Simple Sudo"))
        self.label.setText(_translate("Dialog", f"Command '{strcmd}' is trying to run with superuser permissions"))
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        sizex = 355 + (len(strcmd)*8)
        sizey = 82
        if sizex == 355:
            sizex += 4
        self.setupUi(self, strcmd, sizex, sizey)
        self.buttonBox.accepted.connect(self.close)
        self.buttonBox.accepted.connect(allow)
        self.buttonBox.rejected.connect(self.close)
        self.close()


app = QtWidgets.QApplication(sys.argv)
form = Window()
form.show()
sys.exit(app.exec())
