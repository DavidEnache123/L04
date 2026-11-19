import os
import sqlite3
import subprocess

import pytest

import exercise2
from exercise2 import *


# bug report 1
def test_r1_is_passing():
    assert is_passing(5) == True
    assert is_passing(6) == True
    assert is_passing(4) == False


# bug report 2
def test_r2_is_valid_password_exact_length():
    # Test that a password with exactly 8 characters and at least one digit is valid
    assert is_valid_password("abcdefgh1") is True


# bug report 3
def test_r3_clamp_function():
    assert clamp(10, 5, 15) == 10
    assert clamp(3, 5, 15) == 5
    assert clamp(20, 5, 15) == 15
    assert clamp(5, 5, 15) == 5
    assert clamp(15, 5, 15) == 15
