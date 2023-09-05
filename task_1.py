# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях.
# Напишите к ним тесты.
# 2-5 тестов на задачу в трёх вариантах:
# ○ doctest,
# ○ unittest,
# ○ pytest.

import unittest
import pytest
import doctest

# Функция получает целое число, систему исчисления и возвращает его  строковое представление.
def get_number(number: int, mod: int = 10) -> str:
    """
    :param number: само число
    :param mod: система исчисления
    :return: строковое представление
    >>> get_number(365, 2)
    '101101101'
    >>> get_number(365, 3)
    '111112'
    >>> get_number(365, 4)
    '11231'
    >>> get_number(365, 5)
    '2430'
    >>> get_number(365, 6)
    '1405'
    >>> get_number(365, 7)
    '1031'
    >>> get_number(365, 8)
    '555'
    >>> get_number(365, 9)
    '445'
    """
    result = ''
    while number != 0:
        result = str(number % mod) + result
        number //= mod
    return result


class TestCaseNumbers(unittest.TestCase):
    def test_2(self):
        self.assertEqual(get_number(123, 2), '101101101', msg='Test failed')

    def test_3(self):
        self.assertEqual(get_number(123, 3), '111112', msg='Test failed')

    def test_4(self):
        self.assertEqual(get_number(123, 4), '11231', msg='Test failed')

    def test_5(self):
        self.assertEqual(get_number(123, 5), '2430', msg='Test failed')

    def test_6(self):
        self.assertEqual(get_number(123, 6), '1405', msg='Test failed')

    def test_7(self):
        self.assertEqual(get_number(123, 7), '1031', msg='Test failed')

    def test_8(self):
        self.assertEqual(get_number(123, 8), '555', msg='Test failed')

    def test_9(self):
        self.assertEqual(get_number(123, 9), '445', msg='Test failed')


def test_2():
    assert get_number(123, 2) == '101101101', 'Test failed'


def test_3():
    assert get_number(123, 3) == '111112', 'Test failed'


def test_4():
    assert get_number(123, 4) == '11231', 'Test failed'


def test_5():
    assert get_number(123, 5) == '2430', 'Test failed'


def test_6():
    assert get_number(123, 6) == '1405', 'Test failed'


def test_7():
    assert get_number(123, 7) == '1031', 'Test failed'


def test_8():
    assert get_number(123, 8) == '555', 'Test failed'


def test_9():
    assert get_number(123, 9) == '445', 'Test failed'


if __name__ == '__main__':

    doctest.testmod(verbose=True)
    unittest.main()
    pytest.main()