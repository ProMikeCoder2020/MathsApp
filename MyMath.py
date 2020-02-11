from math import sin, cos, log, tan, sqrt
from PyQt5.QtWidgets import QMessageBox
import operator


def evaluate_maths_expression(expression):
    error = False
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setWindowTitle("Something went wrong...")
    try:
        return eval(expression)
    except ZeroDivisionError:
        error = True
        msg.setText("You tried to divide something by 0")
        msg.setDetailedText("In maths you cannot divide something by 0, so this calculation is not permitable.")
        return " ZeroDivisionError"

    except ValueError:
        error = True
        msg.setText("You tried to perform and invalid operation!Pls try again with valid numbers.")
        msg.setDetailedText("You probably got this error, because you cannot pass a negative number to the logarithm "
                            "or the square root functions.")
        return " Maths Error"

    except SyntaxError:
        error = True
        msg.setText("Your calculation has an invalid syntax! Pls double check it and do it again.")
        msg.setDetailedText("You got this error, because you put two operators or functions one after the other, "
                            "you did not close paranthesis or you used an operator or function without "
                            "sufficient numbers!!!")
        return " Syntax Error"

    finally:
        if error:
            msg.exec_()


def evaluate_logic_expression(bool1, boolean_operator, bool2):
    logic_operations = {"AND": operator.and_, "OR": operator.or_, "XOR": operator.xor,
                        "NAND": (lambda x, y: not(x and y))}
    bool2 = True if bool2 == "True" else False
    if bool1 != "Invalid":
        bool1 = True if bool1 == "True" else False
        return logic_operations[boolean_operator](bool1, bool2)
    else:
        return not bool2


def fractions_calculator(fraction1, fraction2, fraction_operator):
    # each fraction should be received in a form of a tuple with len 2-first item is denominator and second is nominator
    base_operations = {"+": (lambda fraction1_param, fraction2_param: (fraction1_param[0],
                                                                       fraction1_param[1] + fraction2_param[1])),
                       "-": (lambda fraction1_param, fraction2_param: (fraction1_param[0],
                                                                       fraction1_param[1] - fraction2_param[1])),
                       "X": (lambda fraction1_param, fraction2_param: (fraction1_param[0] * fraction2_param[0],
                                                                       fraction1_param[1] * fraction2_param[1])),
                       "/": (lambda fraction1_param, fraction2_param: (fraction1_param[0] * fraction2_param[1],
                                                                       fraction1_param[1] * fraction2_param[0]))}
    fraction1, fraction2 = reduce_to_the_same_denominator(fraction1, fraction2) \
        if fraction_operator in ["+", "-"] else (fraction1, fraction2)
    # will only reduce to the same denominator if it is doing sums or subs
    return base_operations[fraction_operator](fraction1, fraction2)


def reduce_to_the_same_denominator(fraction1, fraction2):
    d_1, n_1 = fraction1
    d_2, n_2 = fraction2
    common_denominator = int(d_2) * int(d_1)
    second_denominator = int(d_2)
    d_2 = common_denominator
    n_2 = int(n_2) * int(d_1)
    d_1 = common_denominator
    n_1 = int(n_1) * int(second_denominator)
    return ((d_1, n_1), (d_2, n_2))


if __name__ == "__main__":  # only for testing purposes
    while True:
        first_fraction = tuple(input("first fraction").split(" "))
        second_fraction = tuple(input("second fraction").split(" "))
        operator = input("Choose an operator")
        print(fractions_calculator(first_fraction, second_fraction, operator))
