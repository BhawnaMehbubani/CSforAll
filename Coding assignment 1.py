'''
Write a program that takes a character as input and prints either 1, 0 or -1 according to the following rules. 1, if the character is an uppercase alphabet (A - Z). 0, if the character is a lowercase alphabet (a - z). -1, if the character is not an alphabet. 

- Input format :Single Character
- Output format :1 or 0 or -1
- Sample Input 1 :  e
- Sample Output 1 : 0
- Sample Input 2 :  E
- Sample Output 2 : 1
- Sample Input 3 : #
- Sample Output 3 : -1
'''

char=input().strip()
if 'A' <=char<='Z':
    print(1)
elif 'a' <=char<='z':
    print(0)
else:
    print(-1)
