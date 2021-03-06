from sys import argv, exit
from PyQt5.QtWidgets import *
from PyQt5 import uic
from math import *
from PyQt5.QtCore import Qt

# Constants
G = '9.80665'
GRAV = '6.67e-11'
E = '2.997925e+8'

widgets = []
##########################
# The calculator project #
##########################


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
        self.btn_eq.clicked.connect(self.equal)
        self.line.returnPressed.connect(self.eq)
        self.btn_c.clicked.connect(self.clear)
        # Change calculator type
        self.common.clicked.connect(self.change_type)
        self.engineer.clicked.connect(self.change_type)
        self.physics.clicked.connect(self.change_type)
        self.programmer.clicked.connect(self.change_type)
        self.graf_building.clicked.connect(self.change_type)

    # keyboard input
    def keyPressEvent(self, event):
        # num pressed:
        if event.key() == Qt.Key_1:
            self.line.setText(self.line.text() + '1')
        elif event.key() == Qt.Key_2:
            self.line.setText(self.line.text() + '2')
        elif event.key() == Qt.Key_3:
            self.line.setText(self.line.text() + '3')
        elif event.key() == Qt.Key_4:
            self.line.setText(self.line.text() + '4')
        elif event.key() == Qt.Key_5:
            self.line.setText(self.line.text() + '5')
        elif event.key() == Qt.Key_6:
            self.line.setText(self.line.text() + '6')
        elif event.key() == Qt.Key_7:
            self.line.setText(self.line.text() + '7')
        elif event.key() == Qt.Key_8:
            self.line.setText(self.line.text() + '8')
        elif event.key() == Qt.Key_9:
            self.line.setText(self.line.text() + '9')
        elif event.key() == Qt.Key_0:
            self.line.setText(self.line.text() + '0')
        # operations:
        elif event.key() == Qt.Key_Enter:
            self.eq()
        elif event.key() == Qt.Key_Plus:
            self.add()
        elif event.key() == Qt.Key_Minus:
            self.sub()
        elif event.key() == Qt.Key_Asterisk:
            self.mult()
        elif event.key() == Qt.Key_Slash:
            self.div()
        elif event.key() == Qt.Key_Backspace:
            self.line.setText(self.line.text()[:-1])
        # change calculator hot-keys:
        if int(event.modifiers()) == Qt.AltModifier:
            if event.key() == Qt.Key_C:
                self.hide()
                CommonCalculator.show_widget()
            if event.key() == Qt.Key_I:
                self.hide()
                EngineerCalculator.show_widget()
            if event.key() == Qt.Key_F:
                self.hide()
                PhysicsCalculator.show_widget()
            if event.key() == Qt.Key_P:
                self.hide()
                ProgrammerCalculator.show_widget()
            if event.key() == Qt.Key_G:
                self.hide()
                GraphCalculator.show_widget()

    # sqrt button
    def qsqrt(self):
        try:
            x = float(self.line.text())
            self.line.setText(str(round(sqrt(x), 6)))
        except Exception as err:
            self.line.setText('ERROR')

    # facrotial button
    def fact(self):
        try:
            x = int(float(self.line.text()))
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

    # equal button for Enter press
    # allow only one operation
    def eq(self):
        try:
            x = self.line.text()
            if '+' in x:
                x = [float(i) for i in x.split('+')]
                if len(x) > 2:
                    raise Exception
                self.line.setText(str(x[0] + x[1]))
            elif '*' in x:
                x = [float(i) for i in x.split('*')]
                if len(x) > 2:
                    raise Exception
                self.line.setText(str(x[0] * x[1]))
            elif '/' in x:
                x = [float(i) for i in x.split('/')]
                if len(x) > 2:
                    raise Exception
                self.line.setText(str(x[0] / x[1]))
            elif '-' in x:
                x = [float(i) for i in x.split('-')]
                if len(x) > 2:
                    raise Exception
                self.line.setText(str(x[0] - x[1]))
            elif '^' in x:
                x = [float(i) for i in x.split('^')]
                if len(x) > 2:
                    raise Exception
                self.line.setText(str(pow(x[0], x[1])))
            elif 'mod' in x:
                x = [float(i) for i in x.split('mod')]
                if len(x) > 2:
                    raise Exception
                self.line.setText(str(x[0] % x[1]))
        except Exception as err:
            self.line.setText('ERROR')

    # equal button, output 'ERROR' in case of Exception
    def equal(self):
        try:
            y = float(self.line.text())
            x = float(self.first_num)
            if self.operation == '+':
                self.line.setText(str(round(x + y, 6)))
            elif self.operation == '-':
                self.line.setText(str(round(x - y, 6)))
            elif self.operation == '*':
                self.line.setText(str(round(x * y, 6)))
            elif self.operation == '/':
                self.line.setText(str(round(x / y, 6)))
            elif self.operation == '^':
                self.line.setText(str(round(pow(x, y), 6)))
            # Engineer calculator option
            elif self.operation == 'mod':
                self.line.setText(str(round(x % y, 6)))
        except Exception as err:
            self.eq()

    # change calculator type
    def change_type(self):
        x = self.sender().text()
        self.hide()
        if x == 'Обычный':
            CommonCalculator.show_widget()
        elif x == 'Инженерный':
            EngineerCalculator.show_widget()
        elif x == 'Физический':
            PhysicsCalculator.show_widget()
        elif x == 'Программист':
            ProgrammerCalculator.show_widget()
        elif x == 'Построение графиков':
            GraphCalculator.show_widget()

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

    def __init__(self, file):
        EngineerCalculator.widgets.append(self)
        # widgets.append(self)
        super().__init__(file)
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
        # logarithm buttons
        self.btn_ln.clicked.connect(self.ln)
        self.btn_lg.clicked.connect(self.lg)
        # modation button
        self.btn_mod.clicked.connect(self.mod)
        # absolute value button
        self.btn_abs.clicked.connect(self.abs)
        # math constants
        self.btn_e.clicked.connect(self.add_constant_e)
        self.btn_pi.clicked.connect(self.add_constant_pi)
        # gain num power of 2
        self.btn_powto2.clicked.connect(self.pow_to_two)

    def pow_to_two(self):
        try:
            x = float(self.line.text())
            self.line.setText(str(pow(x, 2)))
        except Exception as err:
            self.line.setText('ERROR')

    # common trigonometric functions
    def sin(self):
        try:
            x = float(self.line.text())
            if self.degrees.isChecked():
                x = x * pi / 180
            self.line.setText(str(round(sin(x), 9)))
        except Exception as err:
            self.line.setText('ERROR')

    def cos(self):
        try:
            x = float(self.line.text())
            if self.degrees.isChecked():
                x = x * pi / 180
            self.line.setText(str(round(cos(x), 9)))
        except Exception as err:
            self.line.setText('ERROR')

    def tg(self):
        try:
            x = float(self.line.text())
            if self.degrees.isChecked():
                x = x * pi / 180
            self.line.setText(str(round(tan(x), 9)))
        except Exception as err:
            self.line.setText('ERROR')

    # inverse trigonometric functions
    def arcsin(self):
        try:
            x = float(self.line.text())
            x = asin(x)
            if self.degrees.isChecked():
                x = x / pi * 180
            self.line.setText(str(round(x, 9)))
        except Exception as err:
            self.line.setText('ERROR')

    def arccos(self):
        try:
            x = float(self.line.text())
            x = acos(x)
            if self.degrees.isChecked():
                x = x / pi * 180
            self.line.setText(str(round(x, 9)))
        except Exception as err:
            self.line.setText('ERROR')

    def arctg(self):
        try:
            x = float(self.line.text())
            x = atan(x)
            if self.degrees.isChecked():
                x = x / pi * 180
            self.line.setText(str(round(x, 9)))
        except Exception as err:
            self.line.setText('ERROR')

    # logarithm function (e)
    def ln(self):
        try:
            x = float(self.line.text())
            self.line.setText(str(log(x)))
        except Exception as err:
            self.line.setText('ERROR')

    # logarithm function (10)
    def lg(self):
        try:
            x = float(self.line.text())
            self.line.setText(str(log(x, 10)))
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


# Physics calculator class:
# Engineer calculator + some physical constants
class PhysicsCalculator(EngineerCalculator):
    widgets = []

    def __init__(self):
        PhysicsCalculator.widgets.append(self)
        # widgets.append(self)
        super().__init__('Physics.ui')
        # physical constants
        self.btn_g.clicked.connect(self.add_constant_g)
        self.btn_G.clicked.connect(self.add_constant_gravitation)
        self.btn_light_speed.clicked.connect(self.add_constant_light_speed)

    def add_constant_g(self):
        self.line.setText(G)

    def add_constant_gravitation(self):
        self.line.setText(GRAV)

    def add_constant_light_speed(self):
        self.line.setText(E)


# Programmer calculator class:
class ProgrammerCalculator(QDialog):
    widgets = []

    def __init__(self):
        ProgrammerCalculator.widgets.append(self)
        super().__init__()
        self.ui = uic.loadUi('Programmer.ui', self)
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
        # Equal and C button
        self.btn_eq.clicked.connect(self.eq)
        self.btn_c.clicked.connect(self.clear)
        # Change calculator type
        self.common.clicked.connect(self.change_type)
        self.engineer.clicked.connect(self.change_type)
        self.physics.clicked.connect(self.change_type)
        self.programmer.clicked.connect(self.change_type)
        self.graf_building.clicked.connect(self.change_type)

    # clear all fields
    def clear(self):
        self.line_bin.setText('')
        self.line_oct.setText('')
        self.line_dec.setText('')
        self.line_hex.setText('')

    # add number to the line
    def sym(self):
        x = self.sender().text()
        if self.bin.isChecked():
            self.line_bin.setText(self.line_bin.text() + x)
        elif self.oct.isChecked():
            self.line_oct.setText(self.line_oct.text() + x)
        elif self.dec.isChecked():
            self.line_dec.setText(self.line_dec.text() + x)
        elif self.hex.isChecked():
            self.line_hex.setText(self.line_hex.text() + x)

    def eq(self):
        try:
            x = 0
            if self.bin.isChecked():
                x = int(self.line_bin.text(), 2)
            elif self.oct.isChecked():
                x = int(self.line_oct.text(), 8)
            elif self.dec.isChecked():
                x = int(self.line_dec.text())
            elif self.hex.isChecked():
                x = int(self.line_hex.text(), 16)
            self.line_bin.setText(str(bin(x))[2:])
            self.line_oct.setText(str(oct(x))[2:])
            self.line_dec.setText(str(x))
            self.line_hex.setText(str(hex(x))[2:])
        except Exception as err:
            if self.bin.isChecked():
                self.line_bin.setText('ERROR')
            elif self.oct.isChecked():
                self.line_oct.setText('ERROR')
            elif self.dec.isChecked():
                self.line_dec.setText('ERROR')
            elif self.hex.isChecked():
                self.line_hex.setText('ERROR')

    # change calculator type
    def change_type(self):
        x = self.sender().text()
        self.hide()
        if x == 'Обычный':
            CommonCalculator.show_widget()
        elif x == 'Инженерный':
            EngineerCalculator.show_widget()
        elif x == 'Физический':
            PhysicsCalculator.show_widget()
        elif x == 'Программист':
            ProgrammerCalculator.show_widget()
        elif x == 'Построение графиков':
            GraphCalculator.show_widget()

    # Show calculator widget
    @classmethod
    def show_widget(cls):
        cls.widgets[0].show()

    # Hide calculator widget
    @classmethod
    def hide_widget(cls):
        cls.widgets[0].hide()


# Graph build calculator class
class GraphCalculator(QDialog):
    widgets = []

    def __init__(self):
        GraphCalculator.widgets.append(self)
        super().__init__()
        self.ui = uic.loadUi('Graph.ui', self)
        # Change calculator type
        self.common.clicked.connect(self.change_type)
        self.engineer.clicked.connect(self.change_type)
        self.physics.clicked.connect(self.change_type)
        self.programmer.clicked.connect(self.change_type)
        self.graf_building.clicked.connect(self.change_type)
        # Build graph button
        self.build_graph.clicked.connect(self.build)

    # build graph
    def build(self):
        try:
            accuracy = float(self.accuracy.value())
            lower_limit = float(self.lower_limit.value())
            higher_limit = float(self.higher_limit.value())
            parabola = False
            polynomial = False
            # making default function
            # I know that assigning lambda functions to variables
            # is not right following PEP8 , but writing all
            # functions with def is more irrationally
            func = lambda x: x
            # exponential function case
            if self.radio_exponential_function.isChecked():
                a = float(self.exponential_function.text())
                func = lambda x: pow(a, x)
            # sin function case
            if self.radio_sin_function.isChecked():
                a1 = float(self.sin_function_coef1.text())
                a2 = float(self.sin_function_coef2.text())
                func = lambda x: sin(a1 + a2 * x)
            # polynomial
            if self.radio_polynomial.isChecked():
                arg = [float(i) for i in self.polynomial_coefs.text().split(',')]
                polynomial = True
            # parabola function case
            if self.radio_parabol_function.isChecked():
                arg = [float(i) for i in self.parabol_nulls.text().split(',')]
                coef = float(self.coef.text())
                parabola = True
            result_x = [l * accuracy for l
                        in range(int(lower_limit // accuracy),
                                 int(higher_limit // accuracy))] + [higher_limit]
            result_y = []
            # parabola function is definite case because
            # it can consists of many functions, it is
            # specific curve line, for example:
            # (x + 5)(x - 6)(x - 3)(x + 9) ...
            if polynomial:
                for i in result_x:
                    res = [float(k*pow(i, num)) for num, k in enumerate(arg)]
                    res = sum(res)
                    result_y.append(res)
            elif parabola:
                for i in result_x:
                    res = [float(k + i) for k in arg]
                    mult = 1.0
                    for l in res:
                        mult *= l
                    result_y.append(mult * coef)
            else:
                result_y = [func(k) for k in result_x]
            self.graphicsView.clear()
            self.graphicsView.plot(result_x, result_y, pen='r')
            self.err.setText('')
        except Exception as err:
            self.err.setText('ERROR')

    # change calculator type
    def change_type(self):
        x = self.sender().text()
        self.hide()
        if x == 'Обычный':
            CommonCalculator.show_widget()
        elif x == 'Инженерный':
            EngineerCalculator.show_widget()
        elif x == 'Физический':
            PhysicsCalculator.show_widget()
        elif x == 'Программист':
            ProgrammerCalculator.show_widget()
        elif x == 'Построение графиков':
            GraphCalculator.show_widget()

    # Show calculator widget
    @classmethod
    def show_widget(cls):
        cls.widgets[0].show()

    # Hide calculator widget
    @classmethod
    def hide_widget(cls):
        cls.widgets[0].hide()


# main
if __name__ == '__main__':
    app = QApplication(argv)
    # Common calculator init
    cc = CommonCalculator('Common.ui')
    # Engineer calculator init
    ec = EngineerCalculator('Engineer.ui')
    ec.hide()
    # Physics calculator init
    pc = PhysicsCalculator()
    pc.hide()
    # Programmer calculator init
    prc = ProgrammerCalculator()
    prc.hide()
    # Graph calculator init
    gc = GraphCalculator()
    gc.hide()

    cc.show()
    exit(app.exec())
