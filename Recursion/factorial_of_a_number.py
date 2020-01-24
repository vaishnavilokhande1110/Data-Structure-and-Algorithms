'''
The program is implemented to calculate factorial of entered number using recursion
'''
def Fact(n):
    if n==0:
        return 1
    return n * Fact(n-1)

n = int(input('N= '))
print(Fact(n))
