from unittest import main, TestCase
from vigenere import vigenere, position, extend_string, encode_letter

class TestVigenere(TestCase):
    '''
        Vigenere works by rotating the letters by the corresponding letter in the passfrase
        plaintext: ATTACKATDAWN
        key:       LEMONLEMONLE
        ciphertext:LXFOPVEFRNHR
    '''

    def test_vigenere(self):
        inp = "attackatdawn"
        password = 'lemon'
        expected = 'lxfopvefrnhr'
        self.assertEqual(vigenere(inp, password), expected)

    def test_encode(self):
        inp = "attac"
        password = 'lemon'
        expected = 'lxfop'
        for letter in zip(list(inp), list(password), list(expected)):
            with self.subTest(input=letter[0]):
                self.assertEqual(encode_letter(letter[0], letter[1]), letter[2])
    
    def test_extend_string(self):
        inputs = ['teste', 'teste', 'teste']
        lengths = [2, 10, 7]
        outputs = ['te', 'testeteste', 'testete']
        for item in zip(inputs,  lengths ,outputs):
            with self.subTest(input=item[0]):
                self.assertEqual(extend_string(item[0], item[1]), item[2])        
    
    def test_position(self):
        inputs = ['a', 'b', 'z']
        outputs = [0, 1, 25]
        for item in zip(inputs, outputs):
            with self.subTest(input=item[0]):
                self.assertEqual(position(item[0]), item[1])

if __name__ == '__main__':
    main()