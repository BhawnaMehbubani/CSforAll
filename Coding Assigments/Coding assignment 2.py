'''
Sum of Even Numbers till N: 
Given a number N, print sum of all even numbers from 1 to N.  
- Sample Input 1 : 6
- Sample Output 1 : 12
'''

n=int(input().strip())
even_sum=0
for i in range(2, n+1, 2):
    even_sum+=i
print(even_sum)
