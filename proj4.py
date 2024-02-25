# Integer exponent example
base = 2
exponent = 3
result = base ** exponent
print(f"{base} raised to the power of {exponent} is {result}")
# Output: 2 raised to the power of 3 is 8

# Rational exponent example
base = 4
exponent = 0.5
result = base ** exponent
print(f"{base} raised to the power of {exponent} is {result}")
# Output: 4 raised to the power of 0.5 is 2.0

import math

# Square root example
number = 25
square_root = math.sqrt(number)
print(f"The square root of {number} is {square_root}")
# Output: The square root of 25 is 5.0

import math

# Square root example
number = 25
square_root = math.sqrt(number)
print(f"The square root of {number} is {square_root}")
# Output: The square root of 25 is 5.0


# Example polynomial: 3x^2 + 2x - 5
coefficients = [3, 2, -5]
x_value = 2
result = sum(coeff * (x_value ** i) for i, coeff in enumerate(coefficients))
print(f"Result of the polynomial at x = {x_value} is {result}")
# Output: Result of the polynomial at x = 2 is 11


from sympy import symbols, factor

x = symbols('x')
expression = 3*x**2 + 6*x + 3
factored_expression = factor(expression)
print(f"Factored expression: {factored_expression}")
# Output: Factored expression: 3*(x + 1)**2


# Example: (x^2 - 4) / (x + 2)
numerator = x**2 - 4
denominator = x + 2
rational_expression = numerator / denominator
print(f"Rational expression: {rational_expression}")
# Output: Rational expression: (x - 2)*(x + 2)/(x + 2)


# Example: (3 + 4i) + (1 - 2i)
complex1 = complex(3, 4)
complex2 = complex(1, -2)
result = complex1 + complex2
print(f"Sum of complex numbers: {result}")
# Output: Sum of complex numbers: (4+2j)
