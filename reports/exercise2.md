# Bug reports for exercise2.py

Line: 3  
Problem: The function `is_passing` should return `True` if the grade is 5 or more, but the condition `grade > 5` excludes grades exactly equal to 5. This violates the docstring which specifies "5 or more".  
Example: `is_passing(5)` returns `False`, but it should return `True`.  
Fix: `return grade >= 5`

Line: 8  
Problem: The function `is_valid_password` requires "at least 8 characters", but the condition `len(password) > 8` means the password must have more than 8 characters, which excludes exactly 8 characters. This violates the docstring.  
Example: `is_valid_password("abcdefgh")` returns `False`, but it should return `True` since it has exactly 8 characters.  
Fix: `return len(password) >= 8 and any(c.isdigit() for c in password)`

Line: 13  
Problem: The `clamp` function incorrectly uses `max(low, min(x, low))`, which simplifies to `low` regardless of `x`. The correct clamping should bound `x` between `low` and `high`, but here `min(x, low)` is used instead of `min(x, high)`.  
Example: `clamp(10, 5, 15)` returns `5`, but it should return `10` since 10 is within [5,15].  
Fix: `return max(low, min(x, high))`
