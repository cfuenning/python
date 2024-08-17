from PyQt6.QtWidgets import *
from gui import *
from pandas import *

import csv

class IDinUseException(Exception):
    """
    Custom Exception for when an ID has already been used
    """
    pass

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """
        Method to initialize UI and buttons
        """
        super().__init__()
        self.setupUi(self)
        self.jane_radio.setChecked(True)
        self.submit_button.clicked.connect(lambda: self.submit())

    def submit(self):
        """
        Method for verifying input and saving data to csv file
        :return: None
        """
        try:
            ID_entered = int(self.ID_entry.text())

            if ID_entered > 999:
                raise ValueError
            elif ID_entered < 99:
                raise ValueError
            elif not ID_entered:
                raise ValueError

            data = read_csv('data.csv')
            id_num = data['ID Number'].tolist()

            for i in id_num:
                if i == ID_entered:
                    raise IDinUseException

            # check to see which candidate was selected
            if self.john_radio.isChecked():
                vote = 'John'
            if self.jane_radio.isChecked():
                vote = 'Jane'

            # if no exceptions thrown, saved data
            with open('data.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([ID_entered, vote])

            # confirmation message of data saved to CSV
            self.message_label.setText('\tVote Saved')
            self.clear()

        except ValueError:
            self.ID_entry.clear()
            self.message_label.setText(f'Enter Valid ID. Format is ###')

        except IDinUseException:
            self.ID_entry.clear()
            self.message_label.setText(f'ID already used, try again')

    def clear(self):
        """
        Method to clear entered data and reset widgets
        :return: None
        """
        self.john_radio.setChecked(False)
        self.jane_radio.setChecked(True)
        self.ID_entry.clear()
