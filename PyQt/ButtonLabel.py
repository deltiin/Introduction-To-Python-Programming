# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ButtonLabel.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 200)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        MainWindow.setWindowTitle("Button & Label")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(25, 50, 150, 50))
        self.pushButton.setText("Button1")
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.buttonClick1)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(225, 50, 150, 50))
        self.pushButton_2.setText("Button2")
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.buttonClick2)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(25, 120, 350, 50))
        self.label.setText("Hello World")
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

    def buttonClick1(self):
        print('Button 1 Pressed')
        self.label.setText('Button 1 Pressed')
        self.label.move(25,120)

    def buttonClick2(self):
        print('Button 2 Pressed')
        self.label.setText('Button 2 Pressed')
        self.label.move(225,120)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())