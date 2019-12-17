import cipher
import unittest


class test_cipher_methods(unittest.TestCase):
    def test_hasNumbers(self):
        self.assertFalse(cipher.Caesar('test').hasNumbers())
        self.assertTrue(cipher.Caesar('te1st').hasNumbers())

    def test_caesarCipherKey(self):
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        one_to_one = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D',
                      'E': 'E', 'F': 'F', 'G': 'G', 'H': 'H', 'I': 'I',
                      'J': 'J', 'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N',
                      'O': 'O', 'P': 'P', 'Q': 'Q', 'R': 'R', 'S': 'S',
                      'T': 'T', 'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X',
                      'Y': 'Y', 'Z': 'Z'}
        one_ahead = {'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E',
                     'E': 'F', 'F': 'G', 'G': 'H', 'H': 'I', 'I': 'J',
                     'J': 'K', 'K': 'L', 'L': 'M', 'M': 'N', 'N': 'O',
                     'O': 'P', 'P': 'Q', 'Q': 'R', 'R': 'S', 'S': 'T',
                     'T': 'U', 'U': 'V', 'V': 'W', 'W': 'X', 'X': 'Y',
                     'Y': 'Z', 'Z': 'A'}
        self.assertEqual(cipher.Caesar(alphabet).caesarCipherKey(),
                         one_to_one)
        self.assertEqual(cipher.Caesar(alphabet).caesarCipherKey(1),
                         one_ahead)

    def test_Encrypt(self):
        self.assertEqual(cipher.Caesar('abcz').encrypt(1), ' BCDA')

    def test_Decrypt(self):

        encrypted = cipher.Caesar('abc').encrypt(1)
        self.assertEqual(' ABC', cipher.Caesar('abc').decrypt(encrypted, 1))


if __name__ == '__main__':
    unittest.main()
