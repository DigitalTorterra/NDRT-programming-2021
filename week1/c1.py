"""
Week 1, Challenge 1

Write a program to solve a quadratic equation.

Tools:
- basic operators and variables
- if/elif/else statements
- while loops

We will be solving for x in the equation: ax^2+bx+c=0
"""

# Define variables
a = 1
b = 0
c = 1

# Unbounded equation
if a == 0 and b == 0:
    print('You chose a=0 and b=0. x could be anything!')

# Really just a linear equation bx + c = 0, so x = -c/b
elif a == 0:
    x = -c / b
    print(f'In the linear equation {b}x + {c} = 0, x = {x}')

else:
    # Compute the determinant
    det = b**2 - 4 * a * c

    # Repeated root
    if det == 0:
        x = -b / (2 * a)
        print(f'The equation {a}x^2 + {b}x + {c} = 0 has a repeated root at x = {x}')

    # Standard two-root
    elif det > 0:
        x1 = (-b + det ** 0.5) / (2 * a)
        x2 = (-b - det ** 0.5) / (2 * a)
        print(f'The equation {a}x^2 + {b}x + {c} = 0 has roots at x = {x1} and x = {x2}')

    # Complex roots
    else:
        x_real = -b / (2 * a)
        x_imag = ((det * (-1)) ** 0.5) / (2 * a)
        print(f'The equation {a}x^2 + {b}x + {c} = 0 has complex roots at x = {x_real} +- {x_imag}i')
