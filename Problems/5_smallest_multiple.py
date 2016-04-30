'''
Smallest multiple
Problem 5
2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
'''
import numpy as np
import time

def find_smallest_multiple(numbers):
    '''
    Finds the smallest number by testing every integer (brute force)
    '''
    integer = 0
    while True:
        integer += 1
        # Test if multiple of every number in numbers
        for number in numbers:
            succes = True
            if integer % (number) != 0:
                succes = False
                break
        if succes:

            print('Found integer: {}'.format(integer))
            return(integer)


def find_smallest_multiple_multiplication_table(numbers):
    '''
    finds the smallest multiple by only testing multiples of the largest
    number in the list (method similar to multiplication tables)
    '''
    i = 0
    numbers_desc = np.sort(numbers)[::-1]
    while True:
        i += 1
        testable_number = numbers_desc[0]*i
        succes = True
        for number in numbers_desc[1:]:
            if testable_number % (number) != 0:
                succes = False
                break
        if succes:
            solution = testable_number
            print('Found integer: {}'.format(solution))
            return solution


def find_primes_below(N):
    list_of_primes = []
    for i in np.arange(N)+1:
        succes = True
        for prime in list_of_primes:
            if i % prime == 0 and prime != 1:
                succes = False
                break
        if succes:
            list_of_primes.append(i)
    return list_of_primes

# primes_below_10 = find_primes_below(10)
# primes_below_20 = find_primes_below(20)

# print('Primes <10: {}'.format(primes_below_10))
# print('Primes <20: {}'.format(primes_below_20))
assert(find_smallest_multiple(np.arange(10)+1) == 2520)
assert(find_smallest_multiple_multiplication_table(np.arange(10)+1) == 2520)
# assert(find_smallest_multiple(primes_below_10) == 2520)

t0 = time.time()
solution = find_smallest_multiple_multiplication_table(np.arange(20)+1)
t1 = time.time()
print('elapsed_times: {:.2f}s'.format(t1-t0))



# def is_prime():

# find_smallest_multiple(arange(20)+1)
