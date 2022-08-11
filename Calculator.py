from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from Calculator_UI import *
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    variable_list = []
    symbol_list = ['+', '-', '*', '/']
    input_number = ''
    pre_input_number = ''
    addition_var = ''
    minus_var = ''
    multiplication_var = ''
    division_var = ''
    calculator_result = ''
    add_1 = ''
    add_2 = ''
    minus_1 = ''
    minus_2 = ''
    pre_symbol = ''
    add_flag = False
    minus_flag = False

    operator_list = []
    operator_str = ''
    numbers_list = []
    numbers_str = ''
    total_list = []
    total_str = ''
    calculator_operator = []
    calculator_number = []

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.center()

        self.pushButton.clicked.connect(lambda: self.button_event('1'))
        self.pushButton_2.clicked.connect(lambda: self.button_event('2'))
        self.pushButton_3.clicked.connect(lambda: self.button_event('3'))
        self.pushButton_4.clicked.connect(lambda: self.button_event('4'))
        self.pushButton_5.clicked.connect(lambda: self.button_event('5'))
        self.pushButton_6.clicked.connect(lambda: self.button_event('6'))
        self.pushButton_7.clicked.connect(lambda: self.button_event('7'))
        self.pushButton_8.clicked.connect(lambda: self.button_event('8'))
        self.pushButton_9.clicked.connect(lambda: self.button_event('9'))
        self.pushButton_10.clicked.connect(lambda: self.button_event('0'))
        self.pushButton_11.clicked.connect(lambda: self.button_event('00'))
        self.pushButton_12.clicked.connect(lambda: self.button_event('.'))
        self.pushButton_13.clicked.connect(lambda: self.button_event('+'))
        self.pushButton_14.clicked.connect(lambda: self.button_event('-'))
        self.pushButton_15.clicked.connect(lambda: self.button_event('*'))
        self.pushButton_16.clicked.connect(lambda: self.button_event('/'))
        self.pushButton_17.clicked.connect(self.clear_event)
        self.pushButton_18.clicked.connect(self.calculator_event)

    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()
        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()
        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)
        # top left of rectangle be

    def erase_number(self, weight_flag, temp_operator=''):
        for i in range(2):
            self.calculator_number.pop()
        if weight_flag:
            # self.calculator_operator.pop(1)
            if temp_operator:
                self.calculator_operator.remove(temp_operator)
        else:
            self.calculator_operator.pop(0)

    def button_event(self, temp_input):
        # if isinstance(temp_input, str):
            # self.variable_list.append(self.input_number)
            # self.input_number = ''
            # self.symbol_list.append(temp_input)
        if temp_input in self.symbol_list:
            self.operator_list.append(temp_input)
            self.operator_str = self.operator_str + temp_input
            self.calculator_operator.append(temp_input)
            self.numbers_list.append(self.numbers_str)
            self.calculator_number.append(self.numbers_str)
            self.numbers_str = ''
        else:
            # self.numbers_list.append(temp_input)
            self.numbers_str = self.numbers_str + temp_input
            # self.calculator_number.append(temp_input)

        self.total_list.append(temp_input)
        self.total_str = self.total_str + temp_input

        self.textEdit.setText(self.total_str)


        if len(self.calculator_operator) >= 2:
            if self.calculator_operator[-1] in ['+', '-']:
                if self.calculator_operator[-1] == '+':
                    if self.calculator_operator[-2] == self.calculator_operator[-1]:
                        result = int(self.calculator_number[-2]) + int(self.calculator_number[-1])
                        self.erase_number(0)
                    else:
                        if self.calculator_operator[-2] == '-':
                            result = int(self.calculator_number[-2]) - int(self.calculator_number[-1])
                            self.erase_number(0)
                        elif self.calculator_operator[-2] == '*':
                            result = int(self.calculator_number[-2]) * int(self.calculator_number[-1])
                            self.erase_number(1, '*')
                            self.calculator_number.append(result)
                            if len(self.calculator_operator) > 1:
                                if self.calculator_operator[-2] == '+':
                                    result = int(self.calculator_number[-2]) + int(self.calculator_number[-1])
                                    self.erase_number(0)
                                else:
                                    result = int(self.calculator_number[-2]) - int(self.calculator_number[-1])
                                    self.erase_number(0)
                        else:
                            result = int(self.calculator_number[-2]) / int(self.calculator_number[-1])
                            self.erase_number(1, '/')
                            self.calculator_number.append(result)
                            if len(self.calculator_operator) > 1:
                                if self.calculator_operator[-2] == '-':
                                    result = int(self.calculator_number[-2]) - int(self.calculator_number[-1])
                                    self.erase_number(0)
                                else:
                                    result = int(self.calculator_number[-2]) + int(self.calculator_number[-1])
                                    self.erase_number(0)
                    if self.calculator_number[-1] != result:
                        self.calculator_number.append(result)
                    # print(self.calculator_number)
                else:
                    if self.calculator_operator[-2] == self.calculator_operator[-1]:
                        result = int(self.calculator_number[-2]) - int(self.calculator_number[-1])
                        self.erase_number(0)
                    else:
                        if self.calculator_operator[-2] == '+':
                            result = int(self.calculator_number[-2]) + int(self.calculator_number[-1])
                            self.erase_number(0)
                        elif self.calculator_operator[-2] == '*':
                            result = int(self.calculator_number[-2]) * int(self.calculator_number[-1])
                            self.erase_number(1, '*')
                            self.calculator_number.append(result)
                            if len(self.calculator_operator) > 1:
                                if self.calculator_operator[-2] == '+':
                                    result = int(self.calculator_number[-2]) + int(self.calculator_number[-1])
                                    self.erase_number(0)
                                else:
                                    result = int(self.calculator_number[-2]) - int(self.calculator_number[-1])
                                    self.erase_number(0)
                        else:
                            result = int(self.calculator_number[-2]) / int(self.calculator_number[-1])
                            self.erase_number(1, '/')
                            self.calculator_number.append(result)
                            if len(self.calculator_operator) > 1:
                                if self.calculator_operator[-2] == '-':
                                    result = int(self.calculator_number[-2]) - int(self.calculator_number[-1])
                                    self.erase_number(0)
                                else:
                                    result = int(self.calculator_number[-2]) + int(self.calculator_number[-1])
                                    self.erase_number(0)
                    if self.calculator_number[-1] != result:
                        self.calculator_number.append(result)
                    # print(self.calculator_number)
                # self.textEdit_2.setText(str(self.calculator_number[-1]))
            else:
                # if len(self.calculator_operator) == 3:
                if self.calculator_operator[-1] == '*':
                    if self.calculator_operator[-2] == self.calculator_operator[-1]:
                        result = int(self.calculator_number[-2]) * int(self.calculator_number[-1])
                    else:
                        result = int(self.calculator_number[-2]) / int(self.calculator_number[-1])
                    self.erase_number(1)
                    self.calculator_number.append(result)
                else:
                    if self.calculator_operator[-2] == self.calculator_operator[-1]:
                        result = int(self.calculator_number[-2]) / int(self.calculator_number[-1])
                    else:
                        result = int(self.calculator_number[-2]) * int(self.calculator_number[-1])
                    self.erase_number(1)
                    self.calculator_number.append(result)
            self.textEdit_2.setText(str(self.calculator_number[-1]))
        # if temp_input in self.symbol_list:
        #     if not self.pre_symbol:
        #         self.pre_symbol = temp_input
        #     else:
        #         if self.pre_symbol in '+' or self.pre_symbol in '-':
        #             if temp_input in '*' or temp_input in '/':
        #                 if self.pre_symbol in '+':
        #                     self.add_1 = self.calculator_result
        #                     self.calculator_result = ''
        #                 else:
        #                     self.minus_1 = self.calculator_result
        #                     self.calculator_result = ''
        #             # else:
        #             #     if temp_input in '+' or temp_input in '-':
        #             #         if temp_input in '+':
        #             #
        #             #     else:
        #             #         if self.pre_symbol in '+':
        #             #             if self.calculator_result:
        #             #                 self.calculator_result = str(int(self.calculator_result) + int(self.input_number))
        #             #             else:
        #             #                 self.calculator_result = str(int(self.pre_input_number) + int(self.input_number))
        #             #         else:
        #             #             if self.calculator_result:
        #             #                 self.calculator_result = str(int(self.calculator_result) - int(self.input_number))
        #             #             else:
        #             #                 self.calculator_result = str(int(self.pre_input_number) - int(self.input_number))
        #             #         self.textEdit.setText(self.calculator_result)
        #         # if self.pre_symbol in '-':
        #         #     if self.calculator_result:
        #         #         self.calculator_result = str(int(self.calculator_result) - int(self.input_number))
        #         #     else:
        #         #         self.calculator_result = str(int(self.pre_input_number) - int(self.input_number))
        #         #     self.textEdit.setText(self.calculator_result)
        #         if self.pre_symbol in '*':
        #             if self.calculator_result:
        #                 self.calculator_result = str(int(self.calculator_result) * int(self.input_number))
        #             else:
        #                 self.calculator_result = str(int(self.pre_input_number) * int(self.input_number))
        #             self.textEdit.setText(self.calculator_result)
        #         if self.pre_symbol in '/':
        #             if self.calculator_result:
        #                 self.calculator_result = str(int(self.calculator_result) / int(self.input_number))
        #             else:
        #                 self.calculator_result = str(int(self.pre_input_number) / int(self.input_number))
        #             self.textEdit.setText(self.calculator_result)
        #     # if temp_input in '+':
        #     #     if self.calculator_result:
        #     #         self.calculator_result = str(int(self.calculator_result) + int(self.input_number))
        #     #         self.textEdit.setText(self.calculator_result)
        #     #     else:
        #     #         self.calculator_result = self.input_number
        #     # if temp_input in '-':
        #     #     if self.calculator_result:
        #     #         self.calculator_result = str(int(self.calculator_result) - int(self.input_number))
        #     #         self.textEdit.setText(self.calculator_result)
        #     #     else:
        #     #         self.calculator_result = self.input_number
        #         # self.add_num += 1
        #         # if self.add_num == 1:
        #         #     self.temp_add_a = self.input_number
        #         #     if self.add_result:
        #         #         self.add_result = str(int(self.add_result) + int(self.temp_add_a))
        #         #     self.textEdit.setText(self.add_result)
        #         # else:
        #         #     self.temp_add_b = self.input_number
        #         #     if self.add_result:
        #         #         self.add_result = str(int(self.add_result) + int(self.temp_add_b))
        #         #     else:
        #         #         self.add_result = str(int(self.temp_add_a) + int(self.temp_add_b))
        #         #     self.textEdit.setText(self.add_result)
        #         #     self.add_num = 0
        #     self.pre_symbol = temp_input
        #     self.pre_input_number = self.input_number
        #     self.input_number = ''
        # else:
        #     if self.input_number == '':
        #         self.textEdit.setText('')
        #     self.input_number = self.input_number + str(temp_input)
        #     self.textEdit.setText(self.input_number)

    def clear_event(self):
        # self.symbol_list = []
        # self.variable_list = []
        # self.pre_symbol = ''
        # self.pre_input_number = ''
        # self.input_number = ''
        # self.calculator_result = ''
        self.operator_list = []
        self.operator_str = ''
        self.numbers_list = []
        self.numbers_str = ''
        self.total_list = []
        self.total_str = ''
        self.calculator_operator = []
        self.calculator_number = []
        self.textEdit.setText('')
        self.textEdit_2.setText('')

    def calculator_event(self):
        self.variable_list.append(self.input_number)
        self.input_number = ''
        first_variable = self.variable_list[0]
        temp_result = 0
        del self.variable_list[0]
        # while len(self.variable_list) > 0:
        #     calculator_dict = {
        #         '+':
        #     }
        print(self.variable_list)


if __name__ == '__main__':
    temp_app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(temp_app.exec_())
