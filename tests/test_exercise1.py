import os
import sqlite3
import subprocess

import pytest

import exercise1
from exercise1 import *


# bug report 1
def test_r1_is_even():
    # Test that even numbers return True
    assert is_even(4) == True, "Even number 4 should return True"
    assert is_even(0) == True, "Even number 0 should return True"
    assert is_even(2) == True, "Even number 2 should return True"
    
    # Test that odd numbers return False
    assert is_even(3) == False, "Odd number 3 should return False"
    assert is_even(1) == False, "Odd number 1 should return False"
    assert is_even(5) == False, "Odd number 5 should return False"


# bug report 2
def test_r2_rectangle_area():
    # Test case where width=5 and height=3
    # Expected area is 5 * 3 = 15, but current function returns 5 + 3 = 8
    assert rectangle_area(5, 3) == 15, "Function should return the area (width * height), not sum"


# bug report 3
def test_r3_double_function():
    assert double(5) == 10, "double(5) should return 10, but returns 7"
    assert double(0) == 0, "double(0) should return 0"
    assert double(3) == 6, "double(3) should return 6"
    assert double(10) == 20, "double(10) should return 20"
