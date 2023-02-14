"""Fibonacci sequence is a sequence of numbers in which each number is the sum of the two
preceding ones and the sequence starts from 0 and 1
Example: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89…"""

def fibonacci(n):
    assert n>= 0 and int(n) == n, 'fibonacci is a positive interger only'
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci (n-2)

print(fibonacci(9))

#output: 34

