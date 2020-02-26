from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from MyMath import evaluate_maths_expression, evaluate_logic_expression, fractions_calculator, fraction, \
    make_irreducible_fraction, get_percentage, convert_rational_numbers, decimal_number, mixed_number
import sys
from functools import partial

sys._excepthook = sys.excepthook


def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = my_exception_hook


class Ui_Form(QMainWindow):

    def __init__(self):
        super(Ui_Form, self).__init__()
        self.memory = 0
        self.result = 0
        self.setupUi()
        self.reset_calculator()
        self.previous_calculator_changes = []
        self.previous_text = ("", 0, False, False)

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(635, 494)
        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 631, 501))
        self.tabWidget.setObjectName("tabWidget")
        self.draw_advanced_calculator()
        self.draw_logical_calculator()
        self.draw_fraction_percent_calculator()
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.widget = QtWidgets.QWidget(self.tab_2)
        self.widget.setGeometry(QtCore.QRect(70, 30, 521, 41))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.function_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.function_label.setFont(font)
        self.function_label.setObjectName("function_label")
        self.horizontalLayout_2.addWidget(self.function_label)
        self.f_of_x_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.f_of_x_label.setFont(font)
        self.f_of_x_label.setObjectName("f_of_x_label")
        self.horizontalLayout_2.addWidget(self.f_of_x_label)
        self.func_input = QtWidgets.QLineEdit(self.widget)
        self.func_input.setObjectName("func_input")
        self.horizontalLayout_2.addWidget(self.func_input)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.comboBox = QtWidgets.QComboBox(self.tab_6)
        self.comboBox.setGeometry(QtCore.QRect(190, 30, 171, 61))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_6)
        self.comboBox_2.setGeometry(QtCore.QRect(130, 190, 71, 41))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_6)
        self.comboBox_3.setGeometry(QtCore.QRect(450, 190, 69, 41))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_5 = QtWidgets.QLabel(self.tab_6)
        self.label_5.setGeometry(QtCore.QRect(360, 180, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.equal_sign_4 = QtWidgets.QLabel(self.tab_6)
        self.equal_sign_4.setGeometry(QtCore.QRect(250, 180, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.equal_sign_4.setFont(font)
        self.equal_sign_4.setObjectName("equal_sign_4")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit.setGeometry(QtCore.QRect(30, 180, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.tabWidget.addTab(self.tab_6, "")

        self.retranslateUi(self)
        self.tabWidget.setCurrentIndex(0)
        self.fraction_percent_calculator_widget.setCurrentIndex(0)
        self.input_int_cb.setCurrentIndex(0)
        self.output_int_cb.setCurrentIndex(0)
        self.connect_buttons()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.mMinus_button.setText(_translate("Form", "M-"))
        self.minus_button.setText(_translate("Form", "-"))
        self.four_button.setText(_translate("Form", "4"))
        self.mr_button.setText(_translate("Form", "MR"))
        self.zero_button.setText(_translate("Form", "0"))
        self.mc_button.setText(_translate("Form", "MC"))
        self.mPlus_button.setText(_translate("Form", "M+"))
        self.nine_button.setText(_translate("Form", "9"))
        self.power_button.setText(_translate("Form", "**"))
        self.six_button.setText(_translate("Form", "6"))
        self.sinFunc_button.setText(_translate("Form", "sin()"))
        self.five_button.setText(_translate("Form", "5"))
        self.tanFunc_button.setText(_translate("Form", "tan()"))
        self.two_button.setText(_translate("Form", "2"))
        self.eight_button.setText(_translate("Form", "8"))
        self.squareRootFunc_button.setText(_translate("Form", "sqrt()"))
        self.three_button.setText(_translate("Form", "3"))
        self.seven_button.setText(_translate("Form", "7"))
        self.one_button.setText(_translate("Form", "1"))
        self.equal_button.setText(_translate("Form", "="))
        self.divide_button.setText(_translate("Form", "/"))
        self.logFunc_button.setText(_translate("Form", "ln()"))
        self.plus_button.setText(_translate("Form", "+"))
        self.multiply_button.setText(_translate("Form", "x"))
        self.cosFunc_button.setText(_translate("Form", "cos()"))
        self.dot_button.setText(".")
        self.open_paranthesis_button.setText("(")
        self.closing_paranthesis_button.setText(")")
        self.clean_button.setText("DEL")
        self.undo_button.setText("Undo")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.advanced_calculator_tab),
                                  _translate("Form", "Advanced Calculator"))
        self.choose_logic_value_1_cb.setItemText(0, _translate("Form", "True"))
        self.choose_logic_value_1_cb.setItemText(1, _translate("Form", "False"))
        self.choose_logic_value_2_cb.setItemText(0, _translate("Form", "True"))
        self.choose_logic_value_2_cb.setItemText(1, _translate("Form", "False"))
        self.choose_logic_operator_cb.setItemText(0, _translate("Form", "OR"))
        self.choose_logic_operator_cb.setItemText(1, _translate("Form", "AND"))
        self.choose_logic_operator_cb.setItemText(2, _translate("Form", "NOT"))
        self.choose_logic_operator_cb.setItemText(3, _translate("Form", "XOR"))
        self.choose_logic_operator_cb.setItemText(4, _translate("Form", "NAND"))
        self.equal_symbol.setText(_translate("Form", "="))
        self.result_label.setText(_translate("Form", "True"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.logic_calculator_tab),
                                  _translate("Form", "Logic Calculator"))
        self.convertor_button.setText(_translate("Form", "Convertor"))
        self.fraction_calculator_button.setText(_translate("Form", "Fraction Calculator"))
        self.percent_calculator_button.setText(_translate("Form", "Percentage Calculator"))
        self.percentage_input.setText("77")
        self.percentage_input_2.setText("100")
        self.equal_symbol_2.setText(_translate("Form", "="))
        self.result_label_2.setText(_translate("Form", "77 "))
        self.percent_of_label.setText(_translate("Form", "% of "))
        self.input_type_cb.setItemText(0, _translate("Form", "Fraction"))
        self.input_type_cb.setItemText(1, _translate("Form", "Decimal Number"))
        self.input_type_cb.setItemText(2, _translate("Form", "Percentage"))
        self.input_type_cb.setItemText(3, _translate("Form", "Mixed Numeral"))
        self.output_type_cb.setItemText(0, _translate("Form", "Irreducible Fraction"))
        self.output_type_cb.setItemText(1, _translate("Form", "Decimal Number"))
        self.output_type_cb.setItemText(2, _translate("Form", "Percentage"))
        self.output_type_cb.setItemText(3, _translate("Form", "Mixed Numeral"))
        self.output_type_cb.setItemText(4, _translate("Form", "Decimal Fraction"))
        self.to_label.setText(_translate("Form", "to"))
        self.label.setText(_translate("Form", "%"))
        self.label_3.setText(_translate("Form", "%"))
        self.equal_symbol_4.setText(_translate("Form", "="))
        self.fraction_operators_cb.setItemText(0, _translate("Form", "+"))
        self.fraction_operators_cb.setItemText(1, _translate("Form", "-"))
        self.fraction_operators_cb.setItemText(2, _translate("Form", "x"))
        self.fraction_operators_cb.setItemText(3, _translate("Form", "/"))
        self.equal_sign_2.setText(_translate("Form", "="))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fraction_percent_calculato_tabr),
                                  _translate("Form", "Fraction and Percent Calculator"))
        self.function_label.setText(_translate("Form", "Function :"))
        self.f_of_x_label.setText(_translate("Form", "f(x)="))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Function utilities"))
        self.label_5.setText(_translate("Form", "10"))
        self.equal_sign_4.setText(_translate("Form", "="))
        self.lineEdit.setText(_translate("Form", "10"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Form", "Metric units convertor"))

    def draw_advanced_calculator(self):
        self.advanced_calculator_tab = QtWidgets.QWidget()
        self.advanced_calculator_tab.setObjectName("advanced_calculator_tab")
        self.advanced_calculator_frame = QtWidgets.QFrame(self.advanced_calculator_tab)
        self.advanced_calculator_frame.setGeometry(QtCore.QRect(20, 0, 581, 481))
        self.advanced_calculator_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.advanced_calculator_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.advanced_calculator_frame.setObjectName("advanced_calculator_frame")
        self.gridLayoutWidget = QtWidgets.QWidget(self.advanced_calculator_frame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 130, 551, 341))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.advanced_calculator_layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.advanced_calculator_layout.setContentsMargins(0, 0, 0, 0)
        self.advanced_calculator_layout.setSpacing(20)
        self.advanced_calculator_layout.setObjectName("advanced_calculator_layout")
        self.mMinus_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.mMinus_button.setObjectName("mMinus_button")
        self.advanced_calculator_layout.addWidget(self.mMinus_button, 2, 1, 1, 1)
        self.minus_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.minus_button.setObjectName("minus_button")
        self.advanced_calculator_layout.addWidget(self.minus_button, 3, 1, 1, 1)
        self.four_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.four_button.setObjectName("four_button")
        self.advanced_calculator_layout.addWidget(self.four_button, 0, 3, 1, 1)
        self.mr_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.mr_button.setObjectName("mr_button")
        self.advanced_calculator_layout.addWidget(self.mr_button, 2, 2, 1, 1)
        self.zero_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.zero_button.setObjectName("zero_button")
        self.advanced_calculator_layout.addWidget(self.zero_button, 1, 4, 1, 1)
        self.mc_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.mc_button.setObjectName("mc_button")
        self.advanced_calculator_layout.addWidget(self.mc_button, 2, 3, 1, 1)
        self.mPlus_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.mPlus_button.setObjectName("mPlus_button")
        self.advanced_calculator_layout.addWidget(self.mPlus_button, 2, 0, 1, 1)
        self.nine_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.nine_button.setObjectName("nine_button")
        self.advanced_calculator_layout.addWidget(self.nine_button, 1, 3, 1, 1)
        self.power_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.power_button.setObjectName("power_button")
        self.advanced_calculator_layout.addWidget(self.power_button, 3, 4, 1, 1)
        self.six_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.six_button.setObjectName("six_button")
        self.advanced_calculator_layout.addWidget(self.six_button, 1, 0, 1, 1)
        self.sinFunc_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.sinFunc_button.setObjectName("sinFunc_button")
        self.advanced_calculator_layout.addWidget(self.sinFunc_button, 4, 2, 1, 1)
        self.five_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.five_button.setObjectName("five_button")
        self.advanced_calculator_layout.addWidget(self.five_button, 0, 4, 1, 1)
        self.tanFunc_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.tanFunc_button.setObjectName("tanFunc_button")
        self.advanced_calculator_layout.addWidget(self.tanFunc_button, 4, 4, 1, 1)
        self.two_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.two_button.setObjectName("two_button")
        self.advanced_calculator_layout.addWidget(self.two_button, 0, 1, 1, 1)
        self.eight_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.eight_button.setObjectName("eight_button")
        self.advanced_calculator_layout.addWidget(self.eight_button, 1, 2, 1, 1)
        self.squareRootFunc_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.squareRootFunc_button.setObjectName("squareRootFunc_button")
        self.advanced_calculator_layout.addWidget(self.squareRootFunc_button, 4, 0, 1, 1)
        self.three_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.three_button.setObjectName("three_button")
        self.advanced_calculator_layout.addWidget(self.three_button, 0, 2, 1, 1)
        self.seven_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.seven_button.setObjectName("seven_button")
        self.advanced_calculator_layout.addWidget(self.seven_button, 1, 1, 1, 1)
        self.one_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.one_button.setObjectName("one_button")
        self.advanced_calculator_layout.addWidget(self.one_button, 0, 0, 1, 1)
        self.equal_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.equal_button.setObjectName("equal_button")
        self.advanced_calculator_layout.addWidget(self.equal_button, 2, 4, 1, 1)
        self.divide_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.divide_button.setObjectName("divide_button")
        self.advanced_calculator_layout.addWidget(self.divide_button, 3, 3, 1, 1)
        self.logFunc_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.logFunc_button.setObjectName("logFunc_button")
        self.advanced_calculator_layout.addWidget(self.logFunc_button, 4, 1, 1, 1)
        self.plus_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.plus_button.setObjectName("plus_button")
        self.advanced_calculator_layout.addWidget(self.plus_button, 3, 0, 1, 1)
        self.multiply_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.multiply_button.setObjectName("multiply_button")
        self.advanced_calculator_layout.addWidget(self.multiply_button, 3, 2, 1, 1)
        self.cosFunc_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.cosFunc_button.setObjectName("cosFunc_button")
        self.advanced_calculator_layout.addWidget(self.cosFunc_button, 4, 3, 1, 1)
        self.dot_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.dot_button.setObjectName("dot_button")
        self.advanced_calculator_layout.addWidget(self.dot_button, 5, 1, 1, 1)
        self.open_paranthesis_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.open_paranthesis_button.setObjectName("open_paranthesis_button")
        self.advanced_calculator_layout.addWidget(self.open_paranthesis_button, 5, 2, 1, 1)
        self.closing_paranthesis_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.closing_paranthesis_button.setObjectName("closing_paranthesis_button")
        self.advanced_calculator_layout.addWidget(self.closing_paranthesis_button, 5, 3, 1, 1)
        self.clean_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.clean_button.setObjectName("clean_button")
        self.advanced_calculator_layout.addWidget(self.clean_button, 5, 0, 1, 1)
        self.undo_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.undo_button.setObjectName("undo_button")
        self.advanced_calculator_layout.addWidget(self.undo_button, 5, 4, 1, 1)
        self.Advanced_calculator_sheet = QtWidgets.QTextEdit(self.advanced_calculator_frame)
        self.Advanced_calculator_sheet.setGeometry(QtCore.QRect(10, 10, 561, 111))
        self.Advanced_calculator_sheet.setObjectName("Advanced_calculator_sheet")
        self.tabWidget.addTab(self.advanced_calculator_tab, "")

    def draw_logical_calculator(self):
        self.logic_calculator_tab = QtWidgets.QWidget()
        self.logic_calculator_tab.setObjectName("logic_calculator_tab")
        self.logic_calculatorframe = QtWidgets.QFrame(self.logic_calculator_tab)
        self.logic_calculatorframe.setGeometry(QtCore.QRect(9, -1, 601, 471))
        self.logic_calculatorframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logic_calculatorframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logic_calculatorframe.setObjectName("logic_calculatorframe")
        self.choose_logic_value_1_cb = QtWidgets.QComboBox(self.logic_calculatorframe)
        self.choose_logic_value_1_cb.setGeometry(QtCore.QRect(70, 100, 101, 61))
        self.choose_logic_value_1_cb.setObjectName("choose_logic_value_1_cb")
        self.choose_logic_value_1_cb.addItem("")
        self.choose_logic_value_1_cb.addItem("")
        self.choose_logic_value_2_cb = QtWidgets.QComboBox(self.logic_calculatorframe)
        self.choose_logic_value_2_cb.setGeometry(QtCore.QRect(390, 100, 101, 61))
        self.choose_logic_value_2_cb.setObjectName("choose_logic_value_2_cb")
        self.choose_logic_value_2_cb.addItem("")
        self.choose_logic_value_2_cb.addItem("")
        self.choose_logic_operator_cb = QtWidgets.QComboBox(self.logic_calculatorframe)
        self.choose_logic_operator_cb.setGeometry(QtCore.QRect(230, 100, 101, 61))
        self.choose_logic_operator_cb.setObjectName("choose_logic_operator_cb")
        self.choose_logic_operator_cb.addItem("")
        self.choose_logic_operator_cb.addItem("")
        self.choose_logic_operator_cb.addItem("")
        self.choose_logic_operator_cb.addItem("")
        self.choose_logic_operator_cb.addItem("")
        self.equal_symbol = QtWidgets.QLabel(self.logic_calculatorframe)
        self.equal_symbol.setGeometry(QtCore.QRect(240, 200, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.equal_symbol.setFont(font)
        self.equal_symbol.setObjectName("equal_symbol")
        self.result_label = QtWidgets.QLabel(self.logic_calculatorframe)
        self.result_label.setGeometry(QtCore.QRect(190, 330, 261, 81))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.result_label.setFont(font)
        self.result_label.setObjectName("result_label")
        self.tabWidget.addTab(self.logic_calculator_tab, "")
        
    def draw_fraction_percent_calculator(self):
        self.fraction_percent_calculato_tabr = QtWidgets.QWidget()
        self.fraction_percent_calculato_tabr.setObjectName("fraction_percent_calculato_tabr")

        self.fraction_percent_calculator_widget = QtWidgets.QStackedWidget(self.fraction_percent_calculato_tabr)
        self.fraction_percent_calculator_widget.setGeometry(QtCore.QRect(10, 20, 611, 451))
        self.fraction_percent_calculator_widget.setObjectName("fraction_percent_calculator_widget")

        self.back_button = QtWidgets.QPushButton(self.fraction_percent_calculato_tabr)
        self.back_button.setGeometry(QtCore.QRect(15, 10, 85, 20))
        self.back_button.setText("Home")
        self.back_button.setVisible(False)

        self.draw_fraction_calculator_homepage()

        self.draw_percent_calculator_page()

        self.draw_rational_number_convertor()

        self.draw_fraction_calculator()

    def draw_fraction_calculator_homepage(self):
        self.fraction_percent_calculator_homepage = QtWidgets.QWidget()
        self.fraction_percent_calculator_homepage.setObjectName("fraction_percent_calculator_homepage")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.fraction_percent_calculator_homepage)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(130, 90, 391, 201))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.fraction_percent_calculator_home_page_layout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.fraction_percent_calculator_home_page_layout.setContentsMargins(0, 0, 0, 0)
        self.fraction_percent_calculator_home_page_layout.setObjectName("fraction_percent_calculator_home_page_layout")
        self.convertor_button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.convertor_button.setObjectName("convertor_button")
        self.fraction_percent_calculator_home_page_layout.addWidget(self.convertor_button, 2, 0, 1, 1)
        self.fraction_calculator_button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.fraction_calculator_button.setObjectName("fraction_calculator_button")
        self.fraction_percent_calculator_home_page_layout.addWidget(self.fraction_calculator_button, 0, 0, 1, 1)
        self.percent_calculator_button = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.percent_calculator_button.setObjectName("percent_calculator_button")
        self.fraction_percent_calculator_home_page_layout.addWidget(self.percent_calculator_button, 1, 0, 1, 1)
        self.fraction_percent_calculator_widget.addWidget(self.fraction_percent_calculator_homepage)

    def draw_percent_calculator_page(self):
        self.percentage_calculator_page = QtWidgets.QWidget()
        self.percentage_calculator_page.setObjectName("percentage_calculator_page")
        self.percentage_input_2 = QtWidgets.QLineEdit(self.percentage_calculator_page)
        self.percentage_input_2.setGeometry(QtCore.QRect(100, 80, 91, 51))
        self.percentage_input_2.setObjectName("percentage_input_2")
        self.equal_symbol_2 = QtWidgets.QPushButton(self.percentage_calculator_page)
        self.equal_symbol_2.setGeometry(QtCore.QRect(200, 180, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.equal_symbol_2.setFont(font)
        self.equal_symbol_2.setObjectName("equal_symbol_2")
        self.result_label_2 = QtWidgets.QLabel(self.percentage_calculator_page)
        self.result_label_2.setGeometry(QtCore.QRect(170, 280, 261, 81))
        self.result_label_2.setFont(font)
        self.result_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.result_label_2.setObjectName("result_label_2")
        self.percentage_input = QtWidgets.QLineEdit(self.percentage_calculator_page)
        self.percentage_input.setGeometry(QtCore.QRect(380, 80, 91, 51))
        self.percentage_input.setObjectName("percentage_input")
        self.percent_of_label = QtWidgets.QLabel(self.percentage_calculator_page)
        self.percent_of_label.setGeometry(QtCore.QRect(200, 50, 150, 100))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.percent_of_label.setFont(font)
        self.percent_of_label.setObjectName("percent_of_label")
        font.setPointSize(30)
        self.percentage_input.setFont(font)
        self.percentage_input_2.setFont(font)
        self.fraction_percent_calculator_widget.addWidget(self.percentage_calculator_page)

    def draw_rational_number_convertor(self):
        self.convertor_int_page = QtWidgets.QWidget()
        self.convertor_int_page.setObjectName("convertor_int_page")
        self.input_type_cb = QtWidgets.QComboBox(self.convertor_int_page)
        self.input_type_cb.setGeometry(QtCore.QRect(50, 70, 141, 41))
        self.input_type_cb.setObjectName("input_type_cb")
        self.input_type_cb.addItem("")
        self.input_type_cb.addItem("")
        self.input_type_cb.addItem("")
        self.input_type_cb.addItem("")
        self.output_type_cb = QtWidgets.QComboBox(self.convertor_int_page)
        self.output_type_cb.setGeometry(QtCore.QRect(400, 70, 141, 41))
        self.output_type_cb.setObjectName("output_type_cb")
        self.output_type_cb.addItem("")
        self.output_type_cb.addItem("")
        self.output_type_cb.addItem("")
        self.output_type_cb.addItem("")
        self.output_type_cb.addItem("")
        self.to_label = QtWidgets.QLabel(self.convertor_int_page)
        self.to_label.setGeometry(QtCore.QRect(260, 50, 111, 81))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.to_label.setFont(font)
        self.to_label.setObjectName("to_label")

        # starts to create the widgets that receive the input

        self.input_int_cb = QtWidgets.QStackedWidget(self.convertor_int_page)
        self.input_int_cb.setGeometry(QtCore.QRect(60, 180, 120, 80))
        self.input_int_cb.setObjectName("input_int_cb")
        self.fraction_input = QtWidgets.QWidget()
        self.fraction_input.setObjectName("fraction_input")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.fraction_input)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(30, 20, 31, 60))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.fraction_input_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.fraction_input_layout.setContentsMargins(0, 0, 0, 0)
        self.fraction_input_layout.setObjectName("fraction_input_layout")
        self.nominator1_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget_7)
        self.nominator1_3.setText("")
        self.nominator1_3.setAlignment(QtCore.Qt.AlignCenter)
        self.nominator1_3.setObjectName("nominator1_3")
        self.fraction_input_layout.addWidget(self.nominator1_3)
        self.separatorline_3 = QtWidgets.QFrame(self.verticalLayoutWidget_7)
        self.separatorline_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.separatorline_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.separatorline_3.setObjectName("separatorline_3")
        self.fraction_input_layout.addWidget(self.separatorline_3)
        self.denominator_7 = QtWidgets.QLineEdit(self.verticalLayoutWidget_7)
        self.denominator_7.setText("")
        self.denominator_7.setAlignment(QtCore.Qt.AlignCenter)
        self.denominator_7.setObjectName("denominator_7")
        self.fraction_input_layout.addWidget(self.denominator_7)
        self.input_int_cb.addWidget(self.fraction_input)
        self.integer_input_page = QtWidgets.QWidget()
        self.integer_input_page.setObjectName("integer_input_page")
        self.integer_input = QtWidgets.QLineEdit(self.integer_input_page)
        self.integer_input.setGeometry(QtCore.QRect(30, 19, 41, 41))
        self.integer_input.setAlignment(QtCore.Qt.AlignCenter)
        self.integer_input.setObjectName("integer_input")
        self.input_int_cb.addWidget(self.integer_input_page)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.integer_input_2 = QtWidgets.QLineEdit(self.page)
        self.integer_input_2.setGeometry(QtCore.QRect(20, 20, 41, 41))
        self.integer_input_2.setAlignment(QtCore.Qt.AlignCenter)
        self.integer_input_2.setObjectName("integer_input_2")
        self.label = QtWidgets.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(70, 10, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.input_int_cb.addWidget(self.page)
        self.mixed_numreal_input_page = QtWidgets.QWidget()
        self.mixed_numreal_input_page.setObjectName("mixed_numreal_input_page")
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.mixed_numreal_input_page)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(60, 20, 31, 60))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.fractionlayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.fractionlayout_5.setContentsMargins(0, 0, 0, 0)
        self.fractionlayout_5.setObjectName("fractionlayout_5")
        self.nominator1_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget_8)
        self.nominator1_4.setText("")
        self.nominator1_4.setAlignment(QtCore.Qt.AlignCenter)
        self.nominator1_4.setObjectName("nominator1_4")
        self.fractionlayout_5.addWidget(self.nominator1_4)
        self.separatorline_4 = QtWidgets.QFrame(self.verticalLayoutWidget_8)
        self.separatorline_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.separatorline_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.separatorline_4.setObjectName("separatorline_4")
        self.fractionlayout_5.addWidget(self.separatorline_4)
        self.denominator_8 = QtWidgets.QLineEdit(self.verticalLayoutWidget_8)
        self.denominator_8.setText("")
        self.denominator_8.setAlignment(QtCore.Qt.AlignCenter)
        self.denominator_8.setObjectName("denominator_8")
        self.fractionlayout_5.addWidget(self.denominator_8)
        self.integer_inmixed_numeral_input = QtWidgets.QLineEdit(self.mixed_numreal_input_page)
        self.integer_inmixed_numeral_input.setGeometry(QtCore.QRect(20, 40, 31, 31))
        self.integer_inmixed_numeral_input.setObjectName("integer_inmixed_numeral_input")
        self.input_int_cb.addWidget(self.mixed_numreal_input_page)

        # starts to create the widgets that receive the output

        self.output_int_cb = QtWidgets.QStackedWidget(self.convertor_int_page)
        self.output_int_cb.setGeometry(QtCore.QRect(420, 170, 111, 91))
        self.output_int_cb.setObjectName("input_int_cb_3")
        self.fraction_input_4 = QtWidgets.QWidget()
        self.fraction_input_4.setObjectName("fraction_input_4")
        self.verticalLayoutWidget_11 = QtWidgets.QWidget(self.fraction_input_4)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(30, 20, 31, 60))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.fraction_input_layout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_11)
        self.fraction_input_layout_3.setContentsMargins(0, 0, 0, 0)
        self.fraction_input_layout_3.setObjectName("fraction_input_layout_3")
        self.nominator1_7 = QtWidgets.QLineEdit(self.verticalLayoutWidget_11)
        self.nominator1_7.setText("")
        self.nominator1_7.setAlignment(QtCore.Qt.AlignCenter)
        self.nominator1_7.setObjectName("nominator1_7")
        self.fraction_input_layout_3.addWidget(self.nominator1_7)
        self.separatorline_7 = QtWidgets.QFrame(self.verticalLayoutWidget_11)
        self.separatorline_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.separatorline_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.separatorline_7.setObjectName("separatorline_7")
        self.fraction_input_layout_3.addWidget(self.separatorline_7)
        self.denominator_11 = QtWidgets.QLineEdit(self.verticalLayoutWidget_11)
        self.denominator_11.setText("")
        self.denominator_11.setAlignment(QtCore.Qt.AlignCenter)
        self.denominator_11.setObjectName("denominator_11")
        self.fraction_input_layout_3.addWidget(self.denominator_11)
        self.output_int_cb.addWidget(self.fraction_input_4)
        self.integer_input_page_3 = QtWidgets.QWidget()
        self.integer_input_page_3.setObjectName("integer_input_page_3")
        self.integer_input_5 = QtWidgets.QLineEdit(self.integer_input_page_3)
        self.integer_input_5.setGeometry(QtCore.QRect(30, 19, 41, 41))
        self.integer_input_5.setAlignment(QtCore.Qt.AlignCenter)
        self.integer_input_5.setObjectName("integer_input_5")
        self.output_int_cb.addWidget(self.integer_input_page_3)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.integer_input_6 = QtWidgets.QLineEdit(self.page_3)
        self.integer_input_6.setGeometry(QtCore.QRect(20, 20, 41, 41))
        self.integer_input_6.setAlignment(QtCore.Qt.AlignCenter)
        self.integer_input_6.setObjectName("integer_input_6")
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setGeometry(QtCore.QRect(70, 10, 41, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.output_int_cb.addWidget(self.page_3)
        self.mixed_numreal_input_page_3 = QtWidgets.QWidget()
        self.mixed_numreal_input_page_3.setObjectName("mixed_numreal_input_page_3")
        self.verticalLayoutWidget_12 = QtWidgets.QWidget(self.mixed_numreal_input_page_3)
        self.verticalLayoutWidget_12.setGeometry(QtCore.QRect(60, 20, 31, 60))
        self.verticalLayoutWidget_12.setObjectName("verticalLayoutWidget_12")
        self.fractionlayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_12)
        self.fractionlayout_7.setContentsMargins(0, 0, 0, 0)
        self.fractionlayout_7.setObjectName("fractionlayout_7")
        self.nominator1_8 = QtWidgets.QLineEdit(self.verticalLayoutWidget_12)
        self.nominator1_8.setText("")
        self.nominator1_8.setAlignment(QtCore.Qt.AlignCenter)
        self.nominator1_8.setObjectName("nominator1_8")
        self.fractionlayout_7.addWidget(self.nominator1_8)
        self.separatorline_8 = QtWidgets.QFrame(self.verticalLayoutWidget_12)
        self.separatorline_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.separatorline_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.separatorline_8.setObjectName("separatorline_8")
        self.fractionlayout_7.addWidget(self.separatorline_8)
        self.denominator_12 = QtWidgets.QLineEdit(self.verticalLayoutWidget_12)
        self.denominator_12.setText("")
        self.denominator_12.setAlignment(QtCore.Qt.AlignCenter)
        self.denominator_12.setObjectName("denominator_12")
        self.fractionlayout_7.addWidget(self.denominator_12)
        self.integer_inmixed_numeral_input_3 = QtWidgets.QLineEdit(self.mixed_numreal_input_page_3)
        self.integer_inmixed_numeral_input_3.setGeometry(QtCore.QRect(20, 40, 31, 31))
        self.integer_inmixed_numeral_input_3.setObjectName("integer_inmixed_numeral_input_3")
        self.output_int_cb.addWidget(self.mixed_numreal_input_page_3)
        self.equal_symbol_4 = QtWidgets.QPushButton(self.convertor_int_page)
        self.equal_symbol_4.setGeometry(QtCore.QRect(230, 180, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(72)
        self.equal_symbol_4.setFont(font)
        self.equal_symbol_4.setObjectName("equal_symbol_4")
        self.fraction_percent_calculator_widget.addWidget(self.convertor_int_page)
        for widget in self.output_int_cb.findChildren(QtWidgets.QLineEdit):
            widget.setReadOnly(True)

    def draw_fraction_calculator(self):
        self.fractio_calculator_page = QtWidgets.QWidget()
        self.fractio_calculator_page.setObjectName("fractio_calculator_page")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.fractio_calculator_page)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(170, 80, 31, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.fractionlayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.fractionlayout.setContentsMargins(0, 0, 0, 0)
        self.fractionlayout.setObjectName("fractionlayout")
        self.nominator1 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.nominator1.setText("")
        self.nominator1.setAlignment(QtCore.Qt.AlignCenter)
        self.nominator1.setObjectName("nominator1")
        self.fractionlayout.addWidget(self.nominator1)
        self.separatorline_1 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.separatorline_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.separatorline_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.separatorline_1.setObjectName("separatorline_1")
        self.fractionlayout.addWidget(self.separatorline_1)
        self.denominator_1 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.denominator_1.setText("")
        self.denominator_1.setAlignment(QtCore.Qt.AlignCenter)
        self.denominator_1.setObjectName("denominator_1")
        self.fractionlayout.addWidget(self.denominator_1)
        self.fraction_operators_cb = QtWidgets.QComboBox(self.fractio_calculator_page)
        self.fraction_operators_cb.setGeometry(QtCore.QRect(250, 90, 69, 22))
        self.fraction_operators_cb.setObjectName("fraction_operators_cb")
        self.fraction_operators_cb.addItem("")
        self.fraction_operators_cb.addItem("")
        self.fraction_operators_cb.addItem("")
        self.fraction_operators_cb.addItem("")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.fractio_calculator_page)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(360, 80, 31, 51))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.fractionlayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.fractionlayout_2.setContentsMargins(0, 0, 0, 0)
        self.fractionlayout_2.setObjectName("fractionlayout_2")
        self.numerator_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.numerator_2.setText("")
        self.numerator_2.setAlignment(QtCore.Qt.AlignCenter)
        self.numerator_2.setObjectName("numerator_2")
        self.fractionlayout_2.addWidget(self.numerator_2)
        self.separator_line2 = QtWidgets.QFrame(self.verticalLayoutWidget_2)
        self.separator_line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.separator_line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.separator_line2.setObjectName("separator_line2")
        self.fractionlayout_2.addWidget(self.separator_line2)
        self.denominator_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.denominator_2.setText("")
        self.denominator_2.setAlignment(QtCore.Qt.AlignCenter)
        self.denominator_2.setObjectName("denominator_2")
        self.fractionlayout_2.addWidget(self.denominator_2)
        self.equal_sign_2 = QtWidgets.QPushButton(self.fractio_calculator_page)
        self.equal_sign_2.setGeometry(QtCore.QRect(250, 180, 75, 41))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.equal_sign_2.setFont(font)
        self.equal_sign_2.setObjectName("equal_sign_2")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.fractio_calculator_page)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(250, 270, 61, 81))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.fraction_layout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.fraction_layout_3.setContentsMargins(0, 0, 0, 0)
        self.fraction_layout_3.setObjectName("fraction_layout_3")
        self.nominator_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.nominator_3.setText("")
        self.nominator_3.setAlignment(QtCore.Qt.AlignCenter)
        self.nominator_3.setObjectName("nominator_3")
        self.fraction_layout_3.addWidget(self.nominator_3)
        self.separatorLine_3 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.separatorLine_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.separatorLine_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.separatorLine_3.setObjectName("separatorLine_3")
        self.fraction_layout_3.addWidget(self.separatorLine_3)
        self.denominator_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.denominator_3.setText("")
        self.denominator_3.setAlignment(QtCore.Qt.AlignCenter)
        self.denominator_3.setObjectName("denominator_3")
        self.denominator_3.setReadOnly(True)
        self.nominator_3.setReadOnly(True)
        self.fraction_layout_3.addWidget(self.denominator_3)
        self.reset_button = QtWidgets.QPushButton(self.fractio_calculator_page)
        self.reset_button.setText("Reset")
        self.reset_button.setGeometry(QtCore.QRect(250, 50, 85, 20))
        self.make_irreducible_fraction = QtWidgets.QPushButton(self.fractio_calculator_page)
        self.make_irreducible_fraction.setText("Convert to irreducible fraction")
        self.make_irreducible_fraction.move(350, 300)
        self.fraction_percent_calculator_widget.addWidget(self.fractio_calculator_page)
        self.tabWidget.addTab(self.fraction_percent_calculato_tabr, "")

    def connect_buttons(self):
        self.Advanced_calculator_sheet.setReadOnly(True)
        for digit_button in [self.one_button, self.two_button, self.three_button, self.four_button,
                             self.five_button, self.six_button, self.seven_button, self.eight_button,
                             self.zero_button, self.nine_button, self.dot_button, self.open_paranthesis_button,
                             self.closing_paranthesis_button]:
            digit_button.clicked.connect(lambda: self.evaluate_calculator_button("digit"))

        for operator in [self.plus_button, self.minus_button, self.power_button, self.divide_button,
                         self.multiply_button]:
            operator.clicked.connect(lambda: self.evaluate_calculator_button("operator"))

        for func in [self.cosFunc_button, self.tanFunc_button, self.logFunc_button, self.sinFunc_button,
                     self.squareRootFunc_button]:
            func.clicked.connect(lambda: self.evaluate_calculator_button("function"))

        self.clean_button.clicked.connect(lambda: self.evaluate_calculator_button("clean"))

        self.equal_button.clicked.connect(lambda: self.evaluate_calculator_button("equals"))

        self.mr_button.clicked.connect(lambda: self.evaluate_calculator_button("show_memory"))

        self.mc_button.clicked.connect(lambda: self.change_memory(0))

        self.mPlus_button.clicked.connect(lambda: self.change_memory(self.memory + int(self.result)))

        self.mMinus_button.clicked.connect(lambda: self.change_memory(self.memory - self.result))

        self.undo_button.clicked.connect(lambda: self.evaluate_calculator_button("undo"))

        self.fraction_calculator_button.clicked.connect(lambda:
                                                        self.change_fraction_percent_calculator_widget_status(True, 3))
        self.percent_calculator_button.clicked.connect(lambda:
                                                       self.change_fraction_percent_calculator_widget_status(True, 1))
        self.convertor_button.clicked.connect(lambda:
                                              self.change_fraction_percent_calculator_widget_status(True, 2))

        self.back_button.clicked.connect(lambda: self.change_fraction_percent_calculator_widget_status(False, 0))

        self.equal_sign_2.clicked.connect(self.calculate_fractions)

        self.reset_button.clicked.connect(self.reset_fraction_calculator)

        self.make_irreducible_fraction.clicked.connect(self.convert_to_irreducible_fraction)

        self.equal_symbol_2.clicked.connect(self.calculate_percentage)

        for widget, floats in {self.percentage_input: True, self.percentage_input_2: True, self.denominator_1: False,
                               self.nominator1: False, self.denominator_2: False, self.numerator_2: False,
                               self.nominator1_3: False, self.denominator_7: False, self.nominator1_4: False,
                               self.denominator_8: False, self.integer_inmixed_numeral_input: True,
                               self.integer_input: True, self.integer_input_2: True}.items():
            widget.textChanged.connect(partial(self.accept_only_numbers, floats))

        self.choose_logic_value_1_cb.currentTextChanged.connect(self.evaluate_bool_expression)
        self.choose_logic_value_2_cb.currentTextChanged.connect(self.evaluate_bool_expression)
        self.choose_logic_operator_cb.currentTextChanged.connect(self.evaluate_bool_expression)

        self.input_type_cb.currentTextChanged.connect(lambda: self.connect_combo_to_stack(self.input_int_cb))
        self.output_type_cb.currentTextChanged.connect(lambda: self.connect_combo_to_stack(self.output_int_cb))

        self.equal_symbol_4.clicked.connect(self.convert_rational_numbers)

    def evaluate_calculator_button(self, button_type="digit"):
        calculator_text = "\n".join( self.Advanced_calculator_sheet.toPlainText().split("\n")[:-1])
        calculator_text += "\n" if calculator_text != "" else ""
        calculator_text += "".join(self.Advanced_calculator_sheet.toPlainText().split("\n")[-1][:self.cursor_index])
        button_text = self.sender().text()
        negative_number = not(self.number_typed or self.sender().text() != "-")
        button_text += "  " if button_type == "operator" and not negative_number else ""
        try:
            button_text += self.Advanced_calculator_sheet.toPlainText().split("\n")[-1][self.cursor_index:]
        except IndexError as e:
            print(e)
        if button_type == "digit":
            self.cursor_index += 1
            self.number_typed = True if self.sender().text() not in ["(", ")"] else False
            text = (F"{calculator_text}{button_text}", self.cursor_index)
            self.Advanced_calculator_sheet.setText(text[0])

        elif button_type == "operator":
            if not negative_number:
                self.cursor_index += 4 + len(self.sender().text())
                text = (F"{calculator_text}  {button_text}", self.cursor_index)
                self.Advanced_calculator_sheet.setText(text[0])
            else:
                self.cursor_index += 1
                text = (F"{calculator_text}{button_text}", self.cursor_index)
                self.Advanced_calculator_sheet.setText(text[0])
            self.number_typed = False

        elif button_type == "function":
            self.cursor_index += len(self.sender().text()) - 1
            text = (F"{calculator_text}{button_text}", self.cursor_index)
            self.func_typed = True
            self.number_typed = False
            self.Advanced_calculator_sheet.setText(text[0])

        elif button_type == "equals":
            expression = ""
            is_log = False
            for symbol in self.Advanced_calculator_sheet.toPlainText().split("\n")[-1]:
                if symbol == "x":
                    expression += "*"
                elif symbol == "l":
                    expression += "log"
                    is_log = True
                else:
                    if symbol != "n" or not is_log:
                        expression += symbol
                    else:
                        is_log = False
            calculator_text += ")" if self.func_typed else ""
            result = evaluate_maths_expression(expression)
            text = (F"{calculator_text} = {result}\n", "restart")
            self.Advanced_calculator_sheet.setText(text[0])
            self.reset_calculator()
            self.result = result

        elif button_type == "clean":
            text = ("", "restart")
            self.Advanced_calculator_sheet.setText("")
            self.reset_calculator()

        elif button_type == "show_memory":
            text = (F"{self.Advanced_calculator_sheet.toPlainText()}Memory = {self.memory}\n", "restart")
            self.Advanced_calculator_sheet.setPlainText(text[0])
            self.reset_calculator()

        if button_type == "undo":
            if self.previous_calculator_changes == []:
                self.previous_calculator_changes.append(("", 0, False, False))
            print(self.previous_calculator_changes)
            self.Advanced_calculator_sheet.setPlainText(self.previous_calculator_changes[-1][0])
            cursor_info = self.previous_calculator_changes[-1][1]
            if cursor_info == "restart":
                self.reset_calculator()
            else:
                self.cursor_index = cursor_info
                self.number_typed = self.previous_calculator_changes[-1][2]
                self.func_typed = self.previous_calculator_changes[-1][3]
            self.previous_calculator_changes.pop(-1)
        else:
            self.previous_calculator_changes.append(self.previous_text)
            self.previous_text = text + (self.number_typed, self.func_typed)

    def keyPressEvent(self, key):
        if key.text() == "d":
            self.func_typed = False
            self.cursor_index += 1
            self.previous_calculator_changes.append(self.previous_text)
            self.previous_text = (self.Advanced_calculator_sheet.toPlainText(), self.cursor_index, self.number_typed, self.func_typed)

    def reset_calculator(self):
        self.func_typed = False
        self.number_typed = False
        self.cursor_index = 0

    def change_memory(self, m):
        msg = QMessageBox()
        msg.setWindowTitle("Operation completed")
        msg.setText(f"Memory changed to {m}")
        msg.setIcon(QMessageBox.Information)
        msg.setDetailedText(f"The value kept in memory by the calculator has changed to {m}, "
                            f"because you performed one of the following actions: mc(set memory to 0), "
                            f"m+(add result to memory), m-(subtract result to memory).")
        msg.exec_()
        self.memory = m

    def evaluate_bool_expression(self):
        if self.choose_logic_operator_cb.currentText() == "NOT":
            self.choose_logic_value_1_cb.setVisible(False)
            bool1 = "Invalid"
        else:
            self.choose_logic_value_1_cb.setVisible(True)
            bool1 = self.choose_logic_value_1_cb.currentText()
        self.result_label.setText(str(evaluate_logic_expression(bool1,
                                  self.choose_logic_operator_cb.currentText(),
                                  self.choose_logic_value_2_cb.currentText())))

    def change_fraction_percent_calculator_widget_status(self, can_go_back, new_index):
        self.fraction_percent_calculator_widget.setCurrentIndex(new_index)
        self.back_button.setVisible(can_go_back)

    def calculate_fractions(self): # note that this func only decides what input to sent to the backend code that is
        # the one making the calculations.It also handles the output.
        result = fractions_calculator(fraction(denominator=int(self.denominator_1.text()),
                                               nominator=int(self.nominator1.text())),
                                      fraction(denominator=int(self.denominator_2.text()),
                                               nominator=int(self.numerator_2.text())),
                                      self.fraction_operators_cb.currentText())
        self.denominator_3.setText(str(result.denominator))
        self.nominator_3.setText(str(result.nominator))

    def reset_fraction_calculator(self):
        for widget in [self.denominator_1, self.nominator1, self.denominator_2, self.numerator_2,
                       self.denominator_3, self.nominator_3]:
            widget.setText("")
        self.fraction_operators_cb.setCurrentIndex(0)

    def convert_to_irreducible_fraction(self):
        irreducible_fraction = make_irreducible_fraction(fraction(int(self.denominator_3.text()),
                                                                  int(self.nominator_3.text())))
        self.denominator_3.setText(str(irreducible_fraction.denominator))
        self.nominator_3.setText(str(irreducible_fraction.nominator))

    def calculate_percentage(self):
        self.result_label_2.setText(str(get_percentage(self.percentage_input.text(), self.percentage_input_2.text())))
        self.result_label_2.adjustSize()

    def accept_only_numbers(self, allows_floats):
        widget = self.sender()
        digit_like_numbers = [str(x) for x in range(0, 10)]
        if allows_floats:
            digit_like_numbers.append(".")
        try:
            if widget.text()[-1] not in digit_like_numbers:
                widget.setText(widget.text()[:-1])
        except IndexError:
            pass

    def connect_combo_to_stack(self, StackedWidget_to_change):
        text = self.sender().currentText()
        input_widget_dict = {"Fraction": 0, "Decimal Number": 1, "Percentage": 2, "Mixed Numeral": 3,
                             "Decimal Fraction": 0, "Irreducible Fraction": 0}
        StackedWidget_to_change.setCurrentIndex(input_widget_dict[text])
        for widget in StackedWidget_to_change.currentWidget().findChildren(QtWidgets.QLineEdit):
            widget.setText("")

    def convert_rational_numbers(self):
        input_type = self.input_type_cb.currentText()
        output_type = self.output_type_cb.currentText()
        rational_number_dict = {"Fraction": lambda: fraction(int(self.denominator_7.text()),
                                                             int(self.nominator1_3.text())),
                                "Decimal Number": self.get_decimal_number_convertor,
                                "Percentage": lambda: int(self.integer_input_2.text()),
                                "Mixed Numeral": lambda: mixed_number(int(self.integer_inmixed_numeral_input.text()),
                                                                      fraction(int(self.denominator_8.text()),
                                                                      int(self.nominator1_4.text())))}
        output = convert_rational_numbers(rational_number_dict[input_type](), input_type, output_type)
        print(output)
        if output_type in ["Irreducible Fraction", "Decimal Fraction"]:
            self.denominator_11.setText(str(output.denominator))
            self.nominator1_7.setText(str(output.nominator))

        elif output_type == "Decimal Number":
            self.integer_input_5.setText(".".join(str(x) for x in output))

        elif output_type == "Percentage":
            self.integer_input_6.setText(output)

        elif output_type == "Mixed Numeral":
            self.integer_inmixed_numeral_input_3.setText(str(output.integer_part))
            self.denominator_12.setText(str(output.fraction_part.denominator))
            self.nominator1_8.setText(str(output.fraction_part.nominator))

    def get_decimal_number_convertor(self):
        raw_decimal = self.integer_input.text().split(".")
        try:
            return decimal_number(int(raw_decimal[0]), int(raw_decimal[1]))
        except IndexError:
            return decimal_number(int(raw_decimal[0]), 0)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec_())
