# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def __init__(self):
        # Add instance variables and remove pass statement
        #
        # Defnie a variable for storing the calculator expression
        #
        # The expression should modify with each button click
        #
        # Hint: Define the expression variable as a string variable and use string methods to manipulate
        #       the expression variable. After clicking the '=' button the callback corresponding to the 
        #       '=' should be raised and the expression variable should be evaluated.
        #       The result of the evaluation can be used to set the 'self.label_Display' object
        pass

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(250, 370)
        MainWindow.setMaximumSize(QtCore.QSize(250, 370))
        MainWindow.setWindowTitle("Calculator")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton_Clear = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Clear.setGeometry(QtCore.QRect(190, 70, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_Clear.setFont(font)
        self.pushButton_Clear.setText("C")
        self.pushButton_Clear.setObjectName("pushButton_Clear")

        #Connect pushButton_Clear to a callback function

        self.pushButton_ClearEntry = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ClearEntry.setGeometry(QtCore.QRect(130, 70, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_ClearEntry.setFont(font)
        self.pushButton_ClearEntry.setText("CE")
        self.pushButton_ClearEntry.setObjectName("pushButton_ClearEntry")

        #Connect pushButton_ClearEntry to a callback function

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 130, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setText("7")
        self.pushButton_7.setObjectName("pushButton_7")

        #Connect pushButton_Clear to a callback function

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 190, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setText("4")
        self.pushButton_4.setObjectName("pushButton_4")

        #Connect pushButton_4 to a callback function

        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(10, 250, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setText("1")
        self.pushButton_1.setObjectName("pushButton_1")

        #Connect pushButton_1 to a callback function

        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(10, 310, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_0.setFont(font)
        self.pushButton_0.setText("0")
        self.pushButton_0.setObjectName("pushButton_0")

        #Connect pushButton_0 to a callback function

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(70, 190, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setText("5")
        self.pushButton_5.setObjectName("pushButton_5")

        #Connect pushButton_5 to a callback function

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(70, 130, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setText("8")
        self.pushButton_8.setObjectName("pushButton_8")

        #Connect pushButton_8 to a callback function

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 250, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setText("2")
        self.pushButton_2.setObjectName("pushButton_2")

        #Connect pushButton_2 to a callback function

        self.pushButton_DecimalPoint = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_DecimalPoint.setGeometry(QtCore.QRect(70, 310, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_DecimalPoint.setFont(font)
        self.pushButton_DecimalPoint.setText(".")
        self.pushButton_DecimalPoint.setObjectName("pushButton_DecimalPoint")

        #Connect pushButton_DecimalPoint to a callback function

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(130, 190, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setText("6")
        self.pushButton_6.setObjectName("pushButton_6")

        #Connect pushButton_6 to a callback function

        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(130, 130, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setText("9")
        self.pushButton_9.setObjectName("pushButton_9")

        #Connect pushButton_9 to a callback function

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(130, 250, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setText("3")
        self.pushButton_3.setObjectName("pushButton_3")

        #Connect pushButton_3 to a callback function

        self.pushButton_Equal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Equal.setGeometry(QtCore.QRect(130, 310, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_Equal.setFont(font)
        self.pushButton_Equal.setText("=")
        self.pushButton_Equal.setObjectName("pushButton_Equal")

        #Connect pushButton_Equal to a callback function

        self.pushButton_Minus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Minus.setGeometry(QtCore.QRect(190, 250, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_Minus.setFont(font)
        self.pushButton_Minus.setText("–")
        self.pushButton_Minus.setObjectName("pushButton_Minus")

        #Connect pushButton_Minus to a callback function

        self.pushButton_Divide = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Divide.setGeometry(QtCore.QRect(190, 130, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_Divide.setFont(font)
        self.pushButton_Divide.setText("/")
        self.pushButton_Divide.setObjectName("pushButton_Divide")

        #Connect pushButton_Divide to a callback function

        self.pushButton_Multiply = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Multiply.setGeometry(QtCore.QRect(190, 190, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_Multiply.setFont(font)
        self.pushButton_Multiply.setText("×")
        self.pushButton_Multiply.setObjectName("pushButton_Multiply")

        #Connect pushButton_Multiply to a callback function

        self.pushButton_Plus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Plus.setGeometry(QtCore.QRect(190, 310, 50, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_Plus.setFont(font)
        self.pushButton_Plus.setText("+")
        self.pushButton_Plus.setObjectName("pushButton_Plus")

        #Connect pushButton_Plus to a callback function

        self.label_Display = QtWidgets.QLabel(self.centralwidget)
        self.label_Display.setGeometry(QtCore.QRect(10, 10, 230, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_Display.setFont(font)
        self.label_Display.setText("0")
        self.label_Display.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Display.setObjectName("label_Display")


        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

    #declare the callback functions for buttons here. Refer to the previous example for pushButton connect methods

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
