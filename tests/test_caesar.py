import pytest

from  caesar_cipher.caesar import CaesarCipher


class TestCaesar:

    def test_three(self):
        expected = ['d', 'e', 'f', 'g']
        actual = CaesarCipher.encrypt('abcd', 3)
        assert expected == actual 

    def test_neg_three(self):
        expected = ['x', 'y', 'z', 'a']
        actual = CaesarCipher.encrypt('abcd', -3)
        assert expected == actual 

    def test_cap_three(self):
        expected = ['D', 'E', 'F', 'G']
        actual = CaesarCipher.encrypt('ABCD', 3)
        assert expected == actual 

    def test_cap_neg_three(self):
        expected = ['X', 'Y', 'Z', 'A']
        actual = CaesarCipher.encrypt('ABCD', -3)
        assert expected == actual 
    
