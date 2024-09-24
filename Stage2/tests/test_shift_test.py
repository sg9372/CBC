import unittest

# Import the function you want to test
from Stage2.cipher2 import test_shift

class TestShiftCipher(unittest.TestCase):

    def test_shift_positive(self):
        ciphertext = "KHOOR"
        shift = 3
        # Decrypt with a shift of 3 should give "HELLO"
        expected_output = "HELLO"
        self.assertEqual(test_shift(ciphertext, shift), expected_output)

    def test_shift_negative(self):
        ciphertext = "HELLO"
        shift = -3
        # Shifting backward by -3 should give "KHOOR"
        expected_output = "KHOOR"
        self.assertEqual(test_shift(ciphertext, shift), expected_output)

    def test_shift_wraparound(self):
        ciphertext = "ABC"
        shift = 1
        # With shift 1, 'A' becomes 'Z' and 'B' becomes 'A'
        expected_output = "ZAB"
        self.assertEqual(test_shift(ciphertext, shift), expected_output)

    def test_shift_non_alpha(self):
        ciphertext = "HELLO WORLD!"
        shift = 3
        # Non-alphabetical characters should stay the same
        expected_output = "EBIIL TLOIA!"
        self.assertEqual(test_shift(ciphertext, shift), expected_output)

if __name__ == "__main__":
    unittest.main()
