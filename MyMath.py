from math import sin, cos, log, tan, sqrt, ceil
from PyQt5.QtWidgets import QMessageBox
import operator
from collections import namedtuple

fraction = namedtuple("fraction", ["denominator", "nominator"])
decimal_number = namedtuple("decimal_number", ["integer_part", "float_part"])
mixed_number = namedtuple("mixed_number", ["integer_part", "fraction_part"])


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
                        "NAND": (lambda x, y: not (x and y))}
    bool2 = True if bool2 == "True" else False
    if bool1 != "Invalid":
        bool1 = True if bool1 == "True" else False
        return logic_operations[boolean_operator](bool1, bool2)
    else:
        return not bool2


def fractions_calculator(fraction1, fraction2, fraction_operator):
    # each fraction should be received in a form of a tuple with len 2-first item is denominator and second is nominator
    base_operations = {"+": (lambda fraction1_param, fraction2_param: fraction(fraction1_param.denominator,
                                                                               fraction1_param.nominator +
                                                                               fraction2_param.nominator)),
                       "-": (lambda fraction1_param, fraction2_param: fraction(fraction1_param.denominator,
                                                                               fraction1_param.nominator -
                                                                               fraction2_param.nominator)),
                       "x": (lambda fraction1_param, fraction2_param: fraction(fraction1_param.denominator *
                                                                               fraction2_param.denominator,
                                                                               fraction1_param.nominator *
                                                                               fraction2_param.nominator)),
                       "/": (lambda fraction1_param, fraction2_param: fraction(fraction1_param.denominator *
                                                                               fraction2_param.nominator,
                                                                               fraction1_param.nominator *
                                                                               fraction2_param.denominator))}
    fraction1, fraction2 = reduce_to_the_same_denominator(fraction1, fraction2) \
        if fraction_operator in ["+", "-"] else (fraction1, fraction2)
    # will only reduce to the same denominator if it is doing sums or subs

    return base_operations[fraction_operator](fraction1, fraction2)


def reduce_to_the_same_denominator(fraction1, fraction2):
    new_fraction_1 = fraction1
    new_fraction_2 = fraction2

    common_denominator = fraction1.denominator * fraction2.denominator

    new_fraction_1 = new_fraction_1._replace(denominator=common_denominator)
    new_fraction_2 = new_fraction_2._replace(denominator=common_denominator)

    new_fraction_1 = new_fraction_1._replace(nominator=(fraction1.nominator * fraction2.denominator))
    new_fraction_2 = new_fraction_2._replace(nominator=(fraction1.denominator * fraction2.nominator))
    return new_fraction_1, new_fraction_2


def make_irreducible_fraction(fraction_to_be_reduced):
    smaller_number, bigger_number = (fraction_to_be_reduced.denominator, fraction_to_be_reduced.nominator) \
        if fraction_to_be_reduced.denominator < \
           fraction_to_be_reduced.nominator else \
        (fraction_to_be_reduced.nominator,
         fraction_to_be_reduced.denominator)

    for divisor in reversed(range(1, smaller_number+1)):
        if smaller_number % divisor == 0 and bigger_number % divisor == 0:
            fraction_to_be_reduced = fraction_to_be_reduced._replace(denominator=int(fraction_to_be_reduced.denominator
                                                                                 / divisor),
                                                                     nominator=int(fraction_to_be_reduced.nominator
                                                                               / divisor))
            break

    return fraction_to_be_reduced


def get_percentage(number, percent):
    return float(percent) / 100 * float(number)


def decimal_number_to_fraction(decimal):
    fraction_denominator = int("1" + "0" * len(str(decimal.float_part)))
    fraction_that_represents_float_part = fraction(denominator=fraction_denominator, nominator=decimal.float_part)
    fraction_that_represents_integer_part = fraction(fraction_denominator, decimal.integer_part *
                                                     fraction_denominator)
    return fraction(denominator=fraction_that_represents_float_part.denominator, 
                    nominator=fraction_that_represents_float_part.nominator + 
                    fraction_that_represents_integer_part.nominator)


def fraction_to_decimal_number(fraction_to_be_converted):
    raw_decimal_number = fraction_to_be_converted.nominator / fraction_to_be_converted.denominator
    raw_decimal_number = str(raw_decimal_number).split(".")
    raw_decimal_number = [int(i) for i in raw_decimal_number]
    return decimal_number(*raw_decimal_number)


def fraction_to_decimal_fraction(fraction_to_be_converted):
    return decimal_number_to_fraction(fraction_to_decimal_number(fraction_to_be_converted))


if __name__ == "__main__":  # only for testing purposes
    while True:
        input_from_user = input("fraction").split("/")
        fraction_input = fraction(int(input_from_user[1]), int(input_from_user[0]))
        print(fraction_to_decimal_fraction(fraction_input))

