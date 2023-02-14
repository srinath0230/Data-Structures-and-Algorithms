def pot(n):
    if n == 0:
        return 1
    else:
        power = powerOfTwo(n-1)
        return power * 2
print(pot(4))

"""
output: 16

explantion : n = 4, else statement gets excuted.
power = powerOfTwo(4-1)
return powerOfTwo(3) * 2
           ^
       (powerOfTwo(2) * 2)
           ^
        (powerOfTwo(1) * 2)
           ^
        (powerOfTwo(0) * 2)
           ^
        (1 * 2 * 2 * 2 * 2) = 16
"""
