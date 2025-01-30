'''
WRITE CODE : Nth Fibonacci Number (using Loop)
Nth term of Fibonacci series F(n), where F(n) is a function, is calculated using the following formula -
F(n) = F(n-1) + F(n-2), Where, F(1) = 1, F(2) = 1, F(3) = 1+1=2, F(4) = 1+2=3, F(5) = 2+3=5, ....  Provided N you have to find out the Nth Fibonacci Number.
Constraints:
1 <= N <= 10000 Where ‘N’ represents the number for which we have to find its equivalent Fibonacci number.
Time Limit: 1 second
Sample Input 1: 6
Sample Output 1: 8
Explanation : 
Now the number is ‘6’ so we have to find the “6th” Fibonacci number So by using the property of the Fibonacci series i.e [ 1, 1, 2, 3, 5, 8, 13, 21] So the “6th” element is “8” hence we get the output.
'''
n=int(input())
if n==1 or n==2:
    print(1)
else:
    a,b=1,1
    for i in range(3, n+1):
        a,b=b,a+b
        a=a+b
        
    print(b)


'''
Right-hand side (b, a + b):
This part first evaluates b and a + b.
b is the current second Fibonacci number.
a + b is the sum of the two most recent Fibonacci numbers, which is the next Fibonacci number.

Left-hand side (a, b):
This part expects two values (on the right-hand side of the equation) to be assigned to a and b.
Tuple unpacking:

Python takes the two values on the right-hand side (i.e., b and a + b) and assigns them to the left-hand side variables a and b, respectively.
This allows a to take the old value of b (the previous Fibonacci number), and b to take the sum of the old a and b (the next Fibonacci number).
'''
