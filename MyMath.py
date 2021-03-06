from math import sin, cos, log, tan, sqrt, ceil
from PyQt5.QtWidgets import QMessageBox
import operator
from collections import namedtuple, OrderedDict

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
    # we know that this func could be reduced in size but for readability we decide to keep it this way


def fraction_to_decimal_number(fraction_to_be_converted):
    raw_decimal_number = fraction_to_be_converted.nominator / fraction_to_be_converted.denominator
    raw_decimal_number = str(raw_decimal_number).split(".")
    raw_decimal_number = [int(i) for i in raw_decimal_number]
    return decimal_number(*raw_decimal_number)


def fraction_to_decimal_fraction(fraction_to_be_converted):
    return decimal_number_to_fraction(fraction_to_decimal_number(fraction_to_be_converted))


def mixed_number_to_fraction(mixed_number_to_be_converted):
    return fraction(denominator=mixed_number_to_be_converted.fraction_part.denominator,
                    nominator=mixed_number_to_be_converted.fraction_part.denominator *
                    mixed_number_to_be_converted.integer_part + mixed_number_to_be_converted.fraction_part.nominator)


def fraction_to_mixed_number(fraction_to_be_converted):
    integer_part = int(fraction_to_be_converted.nominator / fraction_to_be_converted.denominator)
    fraction_part = fraction(denominator=fraction_to_be_converted.denominator,
                             nominator=fraction_to_be_converted.nominator - integer_part *
                             fraction_to_be_converted.denominator)
    return mixed_number(integer_part=integer_part, fraction_part=fraction_part)


def percentage_to_fraction(percentage):
    return fraction(denominator=100, nominator=percentage)


def fraction_to_percentage(fraction_to_be_converted):
    constant = 100 / fraction_to_be_converted.denominator
    return fraction_to_be_converted.nominator * constant


"""""
 input/output_types:
 -Fraction
 -Decimal Number
 -Mixed Numeral
 -Percentage
 output_types:
 -Irreducible Fraction
 -Decimal Fraction
"""


def convert_rational_numbers(rational_number, input_type, output_type):
    convert_to_fraction_dict = {"Decimal Number": decimal_number_to_fraction, "Mixed Numeral": mixed_number_to_fraction,
                                "Percentage": percentage_to_fraction, "Fraction":
                                lambda rational_number_param: rational_number_param}
    rational_number = convert_to_fraction_dict[input_type](rational_number)
    fraction_to_output_dict = {"Decimal Number": fraction_to_decimal_number, "Mixed Numeral": fraction_to_mixed_number,
                               "Percentage": fraction_to_percentage, "Irreducible Fraction": make_irreducible_fraction,
                               "Decimal Fraction": fraction_to_decimal_fraction}
    return fraction_to_output_dict[output_type](rational_number)


class ThingsThatCanBeMeasured:
    def __init__(self, different_units_correspondence):
        # saves what is the correspondence between the secondary units and the si_unit
        self.different_units_correspondence = different_units_correspondence
        """"
        note that in this dict like in the units dict the value is how many si_units / main_units there are in that 
        multiple / unit
        """

    def convert_between_different_units(self, input_unit, input_quantity, input_multiple, output_unit, output_multiple):
        input_unit_object = self.different_units_correspondence[input_unit][1]
        output_unit_object = self.different_units_correspondence[output_unit][1]
        input_quantity_in_main_unit = input_unit_object.convert_multiples(input_multiple, input_quantity,
                                                                          input_unit_object.main_multiple)
        quantity_in_si_unit = input_quantity_in_main_unit * self.different_units_correspondence[input_unit][0]
        output = quantity_in_si_unit / self.different_units_correspondence[output_unit][0]
        output_quantity_in_passed_multiple = output_unit_object.convert_multiples(output_unit_object.main_multiple,
                                                                                  output, output_multiple)
        print(output_quantity_in_passed_multiple)
        return output_quantity_in_passed_multiple


class Unit:
    def __init__(self, main_unit, unit_dict):
        self.multiples_dict = unit_dict  # ordered dict that stores the multiples and sub-multiples of a unit
        self.main_multiple = main_unit  # the main unit(the one used to convert to other units and multiples)

    def convert_multiples(self, input_multiple, input_quantity, output_multiple):  # it is working, don´t change
        # function that converts between multiples of the same unit. Ex: m - cm
        quantity_in_metres = input_quantity * self.multiples_dict[input_multiple]
        return quantity_in_metres / self.multiples_dict[output_multiple]

    @staticmethod
    def generate_si_unit_dict(main_unit, abbreviation):
        # function that helps generate SI unit dicts(See above for more info).
        base_dict = OrderedDict()

        expressions = [10 ** (-24 + n * 3) for n in range(0, 18) if n != 8]
        expressions.insert(8, 1 / 100)
        expressions.insert(9, 1 / 10)
        expressions.insert(10, 1)
        expressions.insert(11, 10)
        expressions.insert(12, 100)

        multiples = ["y", "z", "a", "f", "p", "n", "micro", "m", "c", "d", main_unit, "da", "h", "k", "M", "G", "T",
                     "P", "E", "Z", "Y"]

        for x, expression in zip(multiples, expressions):

            if multiples.index(x) == 10:
                base_dict[main_unit] = expression
            else:
                base_dict[x + abbreviation] = expression
        return base_dict


# defines units that measure length
metres_unit = Unit("metre", Unit.generate_si_unit_dict("metre", "m"))
miles = Unit("English Mile", OrderedDict([("English Mile", 1), ("Roman Mile", 0.92), ("Nautical Mile", 1.1508),
                                          ("Welsh Mile", 3), ("Irish Mile", 1.27), ("Scots Mile", 1.123),
                                          ("Arabic Mile", 1.18061)]))
inches = Unit("Inches", OrderedDict([("Inch", 1), ("Foot", 12), ("Yard", 36)]))

length = ThingsThatCanBeMeasured({"Miles": (1609.34, miles), "Metres": (1, metres_unit), "Inches": (0.0254, inches)})


if __name__ == "__main__":  # only for testing purposes
    while True:
        input_from_user = input("fraction").split("/")
        fraction_input = fraction(denominator=int(input_from_user[0]), nominator=int(input_from_user[1]))
        print(fraction_to_percentage(fraction_input))

