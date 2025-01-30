'''
Find power of a number : 
Write a program to find x to the power n (i.e. x^n). Take x and n from the user. You need to print the answer.
Note : For this question, you can assume that 0 raised to the power of 0 is 1
Constraints:
0 <= x <= 8 0 <= n <= 9
Sample Input 1 : 3 4
Sample Output 1 : 81
Sample Input 2 : 2 5
Sample Output 2 : 32
'''
x,n=map(int,input().split())
if x==0 and n==0:
    print(1)
else:
    print(x**n)
