from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        """
        Method for GUI interface and initializing widgets
        :param MainWindow: Initializes main window for GUI
        :return: None
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(250, 300)
        MainWindow.setMinimumSize(QtCore.QSize(250, 300))
        MainWindow.setMaximumSize(QtCore.QSize(250, 300))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(40, 10, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.ID_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.ID_label.setGeometry(QtCore.QRect(40, 50, 21, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ID_label.setFont(font)
        self.ID_label.setObjectName("ID_label")
        self.ID_entry = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.ID_entry.setGeometry(QtCore.QRect(65, 50, 113, 20))
        self.ID_entry.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.ID_entry.setObjectName("ID_entry")
        self.candidates_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.candidates_label.setGeometry(QtCore.QRect(80, 90, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.candidates_label.setFont(font)
        self.candidates_label.setObjectName("candidates_label")
        self.jane_radio = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.jane_radio.setGeometry(QtCore.QRect(90, 120, 51, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.jane_radio.setFont(font)
        self.jane_radio.setObjectName("jane_radio")
        self.john_radio = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.john_radio.setGeometry(QtCore.QRect(90, 150, 51, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.john_radio.setFont(font)
        self.john_radio.setObjectName("john_radio")
        self.submit_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.submit_button.setGeometry(QtCore.QRect(50, 180, 141, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.submit_button.setFont(font)
        self.submit_button.setObjectName("submit_button")
        self.message_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.message_label.setGeometry(QtCore.QRect(50, 220, 171, 20))
        self.message_label.setText("")
        self.message_label.setStyleSheet("color: red;")
        self.message_label.setObjectName("message_label")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 50, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color: red;")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 250, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """
        Method to set titles for widgets
        :param MainWindow: main window for GUI
        :return: None
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ClaireVoteApp"))
        self.title_label.setText(_translate("MainWindow", "VOTING APPLICATION"))
        self.ID_label.setText(_translate("MainWindow", "ID"))
        self.candidates_label.setText(_translate("MainWindow", "CANDIDATES"))
        self.jane_radio.setText(_translate("MainWindow", "Jane"))
        self.john_radio.setText(_translate("MainWindow", "John"))
        self.submit_button.setText(_translate("MainWindow", "Submit Vote"))
        self.label.setText(_translate("MainWindow", "*"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
