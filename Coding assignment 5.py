'''
Sum of even & odd: 
Write a program to input an integer N and print the sum of all its even digits and sum of all its odd digits separately. (With a single space)
Digits mean numbers, not the places! That is, if the given integer is "1 3 2 4 5", even digits are 2 & 4 and odd digits are 1, 3 & 5. 
Constraints : 0 <= N <= 10^8
-Sample Input 1: 1234 -
-Sample Output 1: 6 4
-Sample Input 2: 552245
-Sample Output 2: 8 15
'''
n=int(input())
even_sum=0
odd_sum=0
while n>0:
    digit=n%10
    if digit%2==0:
        even_sum+=digit
    else:
        odd_sum+=digit
    n//=10
print(even_sum,odd_sum)
