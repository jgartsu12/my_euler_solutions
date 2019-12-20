"""
Sum square difference

Problem 6
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and 
the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers 
and the square of the sum.
"""
import math 
sum_of_squares_between_one_and_hundred = list(x**2 for x in range(1, 101))

sum_of_sqs = sum(sum_of_squares_between_one_and_hundred)
# print(sum_of_sqs) # --> 338350
    
sum_btwn_one_and_hundred = sum(range(1,101))
# # print(sum_btwn_one_and_hundred) # 5050
# # sq_of_sum = (sum_btwn_one_and_hundred)**2
sq_of_sum = math.pow(sum_btwn_one_and_hundred, 2)

# print(int(sq_of_sum)) # 25502500

sum_sq_diff = sq_of_sum - sum_of_sqs

print(int(sum_sq_diff)) # 25164150
                          