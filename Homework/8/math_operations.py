from custom_exceptions import UnknownOperationError


def addition(number_one: float, number_two: float) -> float:
    """Выполняет сложение двух чисел."""
    return number_one + number_two


def subtraction(number_one: float, number_two: float) -> float:
    """Выполняет вычитание двух чисел."""
    return number_one - number_two


def multiplication(number_one: float, number_two: float) -> float:
    """Выполняет умножение двух чисел."""
    return number_one * number_two


def division(number_one: float, number_two: float) -> float:
    """Выполняет деление двух чисел."""
    return number_one / number_two


def power(number_one: float, number_two: float) -> float:
    """Выполняет возведение числа в степень."""
    return number_one ** number_two


def calculate(number_one: float,  operations: str, number_two: float) -> float:
    """Выполняет, базовые арифметические опреации над двумя числами."""
    match operations:
        case '+':
            return addition(number_one, number_two)
        case '-':
            return subtraction(number_one, number_two)
        case '*':
            return multiplication(number_one, number_two)
        case '/':
            return division(number_one, number_two)
        case '**':
            return power(number_one, number_two)
        case _:
            raise UnknownOperationError(operations)
