import pytest
from palindrome import longest_palindromic_substring

def test_empty_string():
    assert longest_palindromic_substring("") == ""

def test_single_character():
    assert longest_palindromic_substring("e") == "e"

def test_full_string_palindrome():
    assert longest_palindromic_substring("racecar") == "racecar"

def test_partial_palindrome():
    assert longest_palindromic_substring("llama") == "ama"

def test_no_palindromes():
    assert longest_palindromic_substring("abcde123") == "a"

def test_long_string():
    assert longest_palindromic_substring("abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890amanaplanacanalpanamaabcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnopqrstuvwxyz1234567890") == "amanaplanacanalpanama"