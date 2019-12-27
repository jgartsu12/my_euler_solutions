"""
Multiples of 3 and 5

Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
answer = [i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0]
print (sum(answer)) # --> 233168

'''
multiples_range = range(1,1000)

multiples_of_three_or_five = []

for num in multiples_range:
    if num % 3 == 0 or num % 5 == 0:
        multiples_of_three_or_five.append(num)


print(multiples_of_three_or_five)

sum_of_multiples = sum(multiples_of_three_or_five)
print(sum_of_multiples)
# 233168
'''





