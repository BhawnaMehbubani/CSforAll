'''
Code : Array Sum
Given an array of length N, you need to find and print the sum of all elements of the array. 
Constraints : 1 <= N <= 10^6
Input Format : 
Line 1 : An Integer N i.e. size of array Line 2 : N integers which are elements of the array, separated by spaces
Sample Input : 
3
9 8 9
Sample Output : 26
'''

n=int(input())
arr=list(map(int,input().split()))
result=sum(arr)
print(result)
