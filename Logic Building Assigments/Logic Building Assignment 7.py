#https://codeforces.com/problemset/problem/58/A
def can_say_hello(s):
    target = "hello"
    index = 0
    for char in s:
        if char == target[index]:
            index += 1
        if index == len(target):
            return "YES"
    return "NO"

# Input
s = input().strip()

# Output
print(can_say_hello(s))

"""
A. Chat room
time limit per test1 second
memory limit per test256 megabytes
Vasya has recently learned to type and log on to the Internet. He immediately entered a chat room and decided to say hello to everybody. Vasya typed the word s. It is considered that Vasya managed to say hello if several letters can be deleted from the typed word so that it resulted in the word "hello". For example, if Vasya types the word "ahhellllloou", it will be considered that he said hello, and if he types "hlelo", it will be considered that Vasya got misunderstood and he didn't manage to say hello. Determine whether Vasya managed to say hello by the given word s.

Input
The first and only line contains the word s, which Vasya typed. This word consisits of small Latin letters, its length is no less that 1 and no more than 100 letters.

Output
If Vasya managed to say hello, print "YES", otherwise print "NO".
"""

'''
Vasya needs to form the word "hello" by deleting some characters from the given string s while maintaining the order of characters. If it is possible, print "YES", otherwise print "NO".

Steps
Initialize a pointer to the string "hello".
Traverse through the string s and check if each character matches the current character in "hello".
If it matches, move the pointer to the next character in "hello".
If all characters of "hello" are found in order, print "YES". If not, print "NO".
Time and Space Complexity
Time Complexity: O(n), where n is the length of the string s. We iterate through the string once.
Space Complexity: O(1), as we are only using a fixed amount of extra space (a few variables).
'''
