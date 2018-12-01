from sys import argv, exit
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from math import sqrt, factorial, pow


# Common calculator class
class Window(QDialog):
    def __init__(self, file):
        super().__init__()
        # Load Ui file:
        self.ui = uic.loadUi(file, self)
        # Number buttons (0 - 9):
        self.btn1.clicked.connect(self.sym)
        self.btn2.clicked.connect(self.sym)
        self.btn3.clicked.connect(self.sym)
        self.btn4.clicked.connect(self.sym)
        self.btn5.clicked.connect(self.sym)
        self.btn6.clicked.connect(self.sym)
        self.btn7.clicked.connect(self.sym)
        self.btn8.clicked.connect(self.sym)
        self.btn9.clicked.connect(self.sym)
        self.btn0.clicked.connect(self.sym)
        # Operation buttons:
        self.btn_add.clicked.connect(self.add)
        self.btn_sub.clicked.connect(self.sub)
        self.btn_mult.clicked.connect(self.mult)
        self.btn_div.clicked.connect(self.div)
        self.btn_sqrt.clicked.connect(self.qsqrt)
        self.btn_fact.clicked.connect(self.fact)
        self.btn_pow.clicked.connect(self.pow)
        # Equal and C button
        self.btn_eq.clicked.connect(self.eq)
        self.btn_c.clicked.connect(self.clear)
        # Change calculator type
        self.common.clicked.connect(self.change_type)
        self.engineer.clicked.connect(self.change_type)
        self.physics.clicked.connect(self.change_type)
        self.programmer.clicked.connect(self.change_type)
        self.graf_building.clicked.connect(self.change_type)
        # Engineer calculator buttons
        self.ui.show()

    # sqrt button
    def qsqrt(self):
        try:
            x = float(self.line.text())
            self.line.setText(str(sqrt(x)))
        except Exception as err:
            self.line.setText('ERROR')

    # facrotial button
    def fact(self):
        try:
            x = int(self.line.text())
            self.line.setText(str(factorial(x)))
        except Exception as err:
            self.line.setText('ERROR')

    # C button
    def clear(self):
        self.line.setText('')
        self.first_num = ''

    # add symbol in line
    def sym(self):
        x = self.line.text()
        self.line.setText(x + self.sender().text())

    # Main operations: addition, subtraction, division and multiplication
    def add(self):
        self.first_num = self.line.text()
        self.line.setText('')
        self.operation = '+'

    def sub(self):
        self.first_num = self.line.text()
        self.line.setText('')
        self.operation = '-'

    def div(self):
        self.first_num = self.line.text()
        self.line.setText('')
        self.operation = '/'

    def mult(self):
        self.first_num = self.line.text()
        self.line.setText('')
        self.operation = '*'

    # rise number to a power
    def pow(self):
        self.first_num = self.line.text()
        self.line.setText('')
        self.operation = '^'

    # equal button, output 'ERROR' in case of Exception
    def eq(self):
        try:
            y = float(self.line.text())
            x = float(self.first_num)
            if self.operation == '+':
                self.line.setText(str(x + y))
            elif self.operation == '-':
                self.line.setText(str(x - y))
            elif self.operation == '*':
                self.line.setText(str(x * y))
            elif self.operation == '/':
                self.line.setText(str(x / y))
            elif self.operation == '^':
                self.line.setText(str(pow(x, y)))
        except Exception as err:
            self.line.setText('ERROR')

    # change calculator type
    def change_type(self):
        x = self.sender().text()
        self.ui.close()
        self.clear()
        if x == 'Обычный':
            self.ui = uic.loadUi('Common.ui', self)
        elif x == 'Инженерный':
            self.ui = uic.loadUi('Engineer.ui', self)
        elif x == 'Физический':
            uic.loadUi('Physics.ui', self)
        elif x == 'Программист':
            self.ui = uic.loadUi('Programmer.ui', self)
        elif x == 'Построение графиков':
            self.ui = uic.loadUi('Graf.ui', self)
        self.ui.show()


# main
if __name__ == '__main__':
    app = QApplication(argv)
    ex = Window('Common.ui')
    exit(app.exec())
