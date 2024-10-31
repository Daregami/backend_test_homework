"""Эта программа складывает два числа."""


def add(local_num1, local_num2) -> int:
    """Функция складывает два числа."""
    return local_num1 + local_num2


NUM1: int = 10
NUM2: int = 5

print('Сумма чисел:', add(NUM1, NUM2))
# print(__annotations__)
