from unittest import TestCase, main
from fizz import fizzbuzz, fizzbuzzlist

class TestFizzBuzz(TestCase):
    '''
        Testa se é possível resolver o algoritmo do fizzbuzz
        Nele, para cada número dado deve retornar a não ser que 
        seja multiplo de 3, 5 ou ambos, nesse caso deve retornar
        fizz, buzz, fizzbuzz respectivamente.
        3x -> Fizz
        5x -> Buzz
        3x e 5x -> Fizzbuzz
    '''

    def test_1_is_1(self):
        self.assertEqual(fizzbuzz(1),'1')

    def test_is_fizz(self):
        numbers = [3,6,9,12,18]
        for number in numbers:
            with self.subTest(number=number):
                self.assertEqual(fizzbuzz(number),'Fizz')
        
    def test_5_is_buzz(self):
        numbers = [5, 10, 20, 25, 35]
        for number in numbers:
            with self.subTest(number=number):
                self.assertEqual(fizzbuzz(number),'Buzz')

    def test_15_is_fizzbuzz(self):
        numbers = [15, 30, 60, 45]
        for number in numbers:
            with self.subTest(number=number):
                self.assertEqual(fizzbuzz(number),'FizzBuzz')

    def test_fizzbuzz_list(self):
        numbers = [3, 5, 15, 1]
        self.assertEqual(fizzbuzzlist(numbers),['Fizz','Buzz','FizzBuzz','1'])

if __name__ == '__main__':
    main()