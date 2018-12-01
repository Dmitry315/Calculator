from sys import argv, exit
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from math import *

widgets = []


# Common calculator class
class CommonCalculator(QDialog):
    widgets = []

    def __init__(self, file):
        CommonCalculator.widgets.append(self)
        super().__init__()
        # Load Ui file:
        self.ui = uic.loadUi(file, self)
        # Number buttons (0 - 9) + '.':
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
        self.btn_dot.clicked.connect(self.sym)
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
        y = self.sender().text()
        self.line.setText(x + y)

    # Main operations: addition, subtraction, division and multiplication
    def add(self):
        self.first_num = self.line.text()
        self.line.setText('')
        self.operation = '+'

    def sub(self):
        if self.line.text() == '':
            self.line.setText('-')
        elif self.line.text() != '-':
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
            # Engineer calculator option
            elif self.operation == 'mod':
                self.line.setText(str(x % y))
        except Exception as err:
            self.line.setText('ERROR')

    # change calculator type
    def change_type(self):
        x = self.sender().text()
        if x == 'Обычный':
            CommonCalculator.show_widget()
        elif x == 'Инженерный':
            EngineerCalculator.show_widget()
            self.hide()
        elif x == 'Физический':
            uic.loadUi('Physics.ui', self)
        elif x == 'Программист':
            self.ui = uic.loadUi('Programmer.ui', self)
        elif x == 'Построение графиков':
            self.ui = uic.loadUi('Graf.ui', self)

    # Show calculator widget
    @classmethod
    def show_widget(cls):
        cls.widgets[0].show()

    # Hide calculator widget
    @classmethod
    def hide_widget(cls):
        cls.widgets[0].hide()


# Engineer calculator class:
# Common calculator + engineer capabilities
class EngineerCalculator(CommonCalculator):
    widgets = []

    def __init__(self):
        EngineerCalculator.widgets.append(self)
        widgets.append(self)
        super().__init__('Engineer.ui')
        # trigonometric functions
        # There is checkbox, if it is on
        # result will be calculated in degrees and
        # in radians in another option.
        self.btn_sin.clicked.connect(self.sin)
        self.btn_cos.clicked.connect(self.cos)
        self.btn_tg.clicked.connect(self.tg)
        self.btn_arcsin.clicked.connect(self.arcsin)
        self.btn_arccos.clicked.connect(self.arccos)
        self.btn_arctg.clicked.connect(self.arctg)
        # logarithm button
        self.btn_log.clicked.connect(self.log)
        # modation button
        self.btn_mod.clicked.connect(self.mod)
        # absolute value button
        self.btn_abs.clicked.connect(self.abs)
        # math constants
        self.btn_e.clicked.connect(self.add_constant_e)
        self.btn_pi.clicked.connect(self.add_constant_pi)

    # common trigonometric functions
    def sin(self):
        try:
            x = float(self.line.text())
            if self.degrees.isChecked():
                x = x * pi / 180
            self.line.setText(str(sin(x)))
        except Exception as err:
            self.line.setText('ERROR')

    def cos(self):
        try:
            x = float(self.line.text())
            if self.degrees.isChecked():
                x = x * pi / 180
            self.line.setText(str(cos(x)))
        except Exception as err:
            self.line.setText('ERROR')

    def tg(self):
        try:
            x = float(self.line.text())
            if self.degrees.isChecked():
                x = x * pi / 180
            self.line.setText(str(tan(x)))
        except Exception as err:
            self.line.setText('ERROR')

    # inverse trigonometric functions
    def arcsin(self):
        try:
            x = float(self.line.text())
            x = asin(x)
            if self.degrees.isChecked():
                x = x / pi * 180
            self.line.setText(str(x))
        except Exception as err:
            self.line.setText('ERROR')

    def arccos(self):
        try:
            x = float(self.line.text())
            x = acos(x)
            if self.degrees.isChecked():
                x = x / pi * 180
            self.line.setText(str(x))
        except Exception as err:
            self.line.setText('ERROR')

    def arctg(self):
        try:
            x = float(self.line.text())
            x = atan(x)
            if self.degrees.isChecked():
                x = x / pi * 180
            self.line.setText(str(x))
        except Exception as err:
            self.line.setText('ERROR')

    # logarithm function
    def log(self):
        try:
            x = float(self.line.text())
            self.line.setText(str(log(x)))
        except Exception as err:
            self.line.setText('ERROR')

    # modation operation function
    def mod(self):
        self.first_num = self.line.text()
        self.line.setText('')
        self.operation = 'mod'

    # absolute value function
    def abs(self):
        try:
            x = float(self.line.text())
            self.line.setText(str(abs(x)))
        except Exception as err:
            self.line.setText('ERROR')

    # constants functions
    # pi
    def add_constant_pi(self):
        self.line.setText(str(pi))

    # e
    def add_constant_e(self):
        self.line.setText(str(e))


# main
if __name__ == '__main__':
    app = QApplication(argv)
    # Common calculator init
    cc = CommonCalculator('Common.ui')
    # Engineer calculator init
    ec = EngineerCalculator()
    ec.hide()

    cc.show()
    exit(app.exec())
