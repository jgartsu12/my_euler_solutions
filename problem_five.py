"""
Smallest multiple

Problem 5
2520 is the smallest number that can be divided 
by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
"""

def greatest_common_denom(a,b):
    return b and greatest_common_denom(b, a % b) or a

def least_common_mult(a,b):
    return a * b / greatest_common_denom(a,b)

sol =  1
for num in range(1,21):
    sol = least_common_mult(sol, num)

print(sol)

