import unittest
from happy import is_happy, is_happy_list

class TestHappyNumbers(unittest.TestCase):
    '''
        Testa Happy Numbers.
        Suponto um número X, chamaremos cada um de seus algarismos de x_0, x_1... x_n,...
        onde x_0 é o algarismo menos significatívo.
        Define-se a função f(X) = (x_0)²+(x_1)²+...+(x_n)²
        Um número feliz é do numero que aplicada a função f(X) sucessivas vezes
        chega ao número 1.
        Caso o número não seja happy, ele repetirá uma sequencia indefinidamente
        são conhecidos happy numbers: 1, 7, 10, 13
    '''

    def test_is_happy(self):
        happy = [1, 7, 10, 13, 7839]
        expected = [True for i in range(len(happy))]
        self.assertEqual(is_happy_list(happy),expected)

    def test_is_unhappy(self):
        unhappy = [2, 4, 6, 8, 9, 11]
        expected = [False for i in range(len(unhappy))]
        self.assertEqual(is_happy_list(unhappy),expected)

    def test_is_1_a_happy_number(self):
        self.assertTrue(is_happy(1))

    def test_is_7_a_happy_number(self):
        self.assertTrue(is_happy(7))

    def test_is_4_not_happy(self):
        self.assertFalse(is_happy(4))



if __name__ == '__main__':
    unittest.main()