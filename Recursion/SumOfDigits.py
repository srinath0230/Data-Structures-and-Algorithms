def SumOfDigits(n):
    assert n>=0 and int(n) == n, 'Enter Positive interger values only'
    #base case
    if n == 0:
        return 0
    else:
        # recursive case f(n) = n%10 + f(n//10)
        # floor division // rounds the number to nearest in interger
        return int(n%10) + SumOfDigits(int(n//10))
    
print(SumOfDigits(1111))
