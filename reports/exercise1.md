# Bug reports for exercise1.py

Line: 3
Problem: The condition `n % 2 == 1` checks if a number is odd, not even. For even numbers, the remainder when divided by 2 should be 0, not 1. The function should return `n % 2 == 0` to correctly identify even numbers.
Example: is_even(4) returns False, but it should return True (since 4 is even).
Fix: return n % 2 == 0

Line: 8
Problem: The function calculates the sum of width and height, not the area of a rectangle. The area of a rectangle is width multiplied by height, not added.
Example: rectangle_area(5, 3) returns 8, but it should return 15.
Fix: return width * height

Line: 13
Problem: The function `double(n)` should return twice the number, i.e., `n * 2`, but it incorrectly adds 2 instead.
Example: double(5) returns 7, but it should return 10.
Fix: return n * 2
