"""
Largest prime factor

Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def get_largest_prime_factor(n):  # n = number looking for largest factor of
    pf = 1  # pf = initial prime
    i = 2               # i figure out if it can be broken down into more prime numbers

    while i <= n / i:                                  
        if n % i == 0:                                 
            pf = i 
            n /= i                                         
        else:
            i += 1                            

    if pf < n:            
        pf = n                

    return pf
  
print(get_largest_prime_factor(600851475143))
    # --> 6857.0
