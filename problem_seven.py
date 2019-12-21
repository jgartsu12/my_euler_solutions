"""
10001st prime

Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

def is_prime(n):
    # look for factors of 2 first
    if n % 2 == 0: return False
    # now look for odd factors
    p = 3
    while p < n**0.5+1:
        if n % p == 0: return False
        p += 2
    return True
 
def nth_prime(n):
    prime = 2
    count = 1
    iter = 3
    while count < n:
        if is_prime(iter):
            prime = iter
            count += 1
        iter += 2
    return prime
 
prime = nth_prime(10001)

print(prime) # 104743




# def factors(n):
#     factors = []
#     # remove any factors of 2 first
#     while n % 2 == 0:
#         factors.append(2)
#         n = n/2
#     # now look for odd factors
#     p = 3
#     while n != 1:
#         while n % p == 0:
#             factors.append(p)
#             n = n/p
#         p += 2
#     return factors
 
# def nth_prime(n):
#     prime = 2 # last prime
#     count = 1 # number of primes
#     num = 3 # next number to check
#     while count < n:
#         if len(factors(num)) == 1:
#             prime = num
#             count += 1
#         num += 2 # only check odd numbers
#     return prime


# prime = nth_prime(10001)

# print(prime)





# def prime_find():
#     nth_prime_to_find = 10001
#     x = 2
#     prime_nums_list = []
#     while(len(prime_nums_list) < nth_prime_to_find):
#         if all(x % prime for prime in prime_nums_list):
#             prime_nums_list.append(x)
#         x += 1

#         print(prime_nums_list[-1])

# prime_find()
 
 
  
