'''
Check  Fibonacci Number 
Given a number N, figure out if it is a member of fibonacci series or not. Return true if the number is member of fibonacci series else false.
Fibonacci Series is defined by the recurrence : F(n) = F(n-1) + F(n-2) where F(0) = 0 and F(1) = 1,  F(3) = 1+1=2, F(4) = 1+2=3, F(5) = 2+3=5, ....
Constraints :
0 <= n <= 10^4
Sample Input 1 : 5
Sample Output 1 : true
Sample Input 2 : 14
Sample Output 2 : false
'''

import math
def is_perfect_square(x):
    s=int(math.sqrt(x))
    return s*s==x
def is_fibonacci(n):
    return is_perfect_square(5*n*n+4) or is_perfect_square(5*n*n-4)
n=int(input())
if is_fibonacci(n):
    print("true")
else:
    print("false")

'''
A number `n` is considered a Fibonacci number if and only if one (or both) of the following conditions is true:

1. `5 * n^2 + 4` is a perfect square, or
2. `5 * n^2 - 4` is a perfect square.
'''
  
