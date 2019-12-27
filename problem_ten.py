"""
Summation of primes

Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

sieve = [True] * 2000000                                 
def mark(sieve, x):                                        
    for i in range(x + x, len(sieve), x):                     
        sieve[i] = False                                    

for x in range(2, int(len(sieve) ** 0.5) + 1):              
    if sieve[x] == True:                                     
        mark(sieve, x)                                     

print (sum(i for i in range(2, len(sieve)) if sieve[i]))
# 142913828922

'''
prime_list = []

def prime_find_sum():
    prime_range = range(2, int(2e6))
    for x in prime_range:
        if x > 1:
            for num in range(2, x):
                if (x % num) == 0:
                    break
            else:
                prime_list.append(x)
    print(prime_list)
    # print(sum(prime_list))


prime_find_sum() # 142913828922

'''

'''
# case example

prime_list = []

def prime_find_sum():
    prime_range_ten = range(2,10)
    for x in prime_range_ten:
        if x > 1:
            for num in range(2, x):
                if (x % num) == 0:
                    break
            else:
                prime_list.append(x)

    print(sum(prime_list))


prime_find_sum() # 17
'''

