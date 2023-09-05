# Возьмите 1-3 задачи из тех, что были на прошлых
# семинарах или в домашних заданиях.
# Напишите к ним тесты.
# 2-5 тестов на задачу в трёх вариантах:
# ○ doctest,
# ○ unittest,
# ○ pytest.


import doctest
import unittest
import pytest
def calculation(num):
    '''
    calculation all...
    >>> calculation(5)
    25
    >>> calculation(21)
    2
    >>> calculation(153)
    351
    >>> calculation(0)
    'num должно быть > 0'
    >>> calculation(1000)
    'num должно быть < 999'
    >>> calculation(3.6)
    'num должно быть целым числом'
    >>> calculation('33')
    'num должно быть числом'
    '''

    if not isinstance(num, (int, float)):
        return 'num должно быть числом'
    if num <= 0:
        return 'num должно быть > 0'
    if num > 999:
        return 'num должно быть < 999'
    if num != int(num):
        return 'num должно быть целым числом'

    if num < 10:
        return num ** 2
    elif 10 <= num <= 99:
        first_number = num // 10
        second_number = num % 10
        result = first_number * second_number
    else:
        first_number = num // 100
        second_number = (num // 10) % 10
        third_number = num % 10
        result = third_number * 100 + second_number * 10 + first_number

    return result
#
# if __name__ == '__main__':
#     doctest.testmod(verbose=True)



def test_square():
    assert calculation(5) == 25

def test_works():
    assert calculation(21) == 2

def test_mirror():
    assert calculation(153) == 351

def test_less_zero():
    assert calculation(0) == 'num должно быть > 0'

def test_less_thousandr():
    assert calculation(1001) == 'num должно быть < 999'

def test_float():
    assert calculation(1.8) == 'num должно быть целым числом'

def test_int():
    assert calculation('45') == 'num должно быть числом'

# if __name__ == '__main__':
#     pytest.main(['-v'])



class TestUnit(unittest.TestCase):
    def test_square(self):
        self.assertEqual(calculation(5), 25)

    def test_works(self):
        self.assertEqual(calculation(21), 2)

    def test_mirror(self):
        self.assertEqual(calculation(153), 351)

    def test_less_zero(self):
        self.assertEqual(calculation(0), 'num должно быть > 0')

    def test_less_thousand(self):
        self.assertEqual(calculation(1001), 'num должно быть < 999')

    def test_float(self):
        self.assertEqual(calculation(1.8), 'num должно быть целым числом')

    def test_int(self):
        self.assertEqual(calculation('45'), 'num должно быть числом')


# if __name__ == '__main__':
#     unittest.main(verbosity=2)