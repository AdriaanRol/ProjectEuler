'''
Largest prime factor
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
import numpy as np
import time


# Attempt 1, brute forcing the problem
def find_primes_below_N_brute(N, list_of_primes=[1]):
    '''
    Brute force calculates primes, can be used to extend a list of primes
    by handing a list of known primes

    '''
    for i in np.arange(N)+1:
        if i >= max(list_of_primes):
            succes = True
            for prime in list_of_primes:
                if i % prime == 0 and prime != 1:
                    succes = False
                    break
            if succes:
                list_of_primes.append(i)
    return list_of_primes

N = int(1e4)

t0 = time.time()

max_prime = max(find_primes_below_N_brute(N))
print('Max prime below {} {}'.format(N, max_prime))
t1 = time.time()
print('took: {:.2f}s'.format(t1-t0))
# Note brute forcing works up to about 1e5 (~15s)


def factorize(N):
    '''
    Factorize using a tree method
    '''

    return N

print(factorize(10))
