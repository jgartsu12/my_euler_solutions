"""
Largest palindrome product

Problem 4
A palindromic number reads the same both ways. The largest palindrome made 
from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers
"""
# palindromes = []
# for x in range(100, 1000): # range of all 3 digit numbers
#     for i in range(100, 1000): # same range for other multiple in x * i (100 to 999 since 1000 not included)
#         num = str(i*x).split()[0]
#         if len(num) == 6:
#             if num[0] == num[-1] and num[1] == num[-2] and num[2] == num[-3]:
#                 palindromes.append(i * x)
# print(max(palindromes))

four_dig_palis = []
for y in range(1000, 9999):
    for z in range(1000, 9999):
        n = str(y*z).split()[0]
        if len(n) == 8:
            if n[0] == [-1] and n[1] == n[-2] and n[2] == n[-3] and n[3] == n[-4]:
                four_dig_palis.append(y * z)
print(max(four_dig_palis))
