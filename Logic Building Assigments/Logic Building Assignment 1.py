#https://codeforces.com/problemset/problem/4/A

def can_divide_watermelon(w):
    print("YES" if w > 2 and w % 2 == 0 else "NO")

# Read input
w = int(input())
can_divide_watermelon(w)

"""
A. Watermelon
time limit per test1 second
memory limit per test64 megabytes
One hot summer day Pete and his friend Billy decided to buy a watermelon. They chose the biggest and the ripest one, in their opinion. After that the watermelon was weighed, and the scales showed w kilos. They rushed home, dying of thirst, and decided to divide the berry, however they faced a hard problem.

Pete and Billy are great fans of even numbers, that's why they want to divide the watermelon in such a way that each of the two parts weighs even number of kilos, at the same time it is not obligatory that the parts are equal. The boys are extremely tired and want to start their meal as soon as possible, that's why you should help them and find out, if they can divide the watermelon in the way they want. For sure, each of them should get a part of positive weight.

Input
The first (and the only) input line contains integer number w (1 ≤ w ≤ 100) — the weight of the watermelon bought by the boys.

Output
Print YES, if the boys can divide the watermelon into two parts, each of them weighing even number of kilos; and NO in the opposite case.
"""

'''
Simple Conditional Check:
w > 2: Ensures the weight is more than 2 (since 2 can only be split into 1+1, which is not even).
w % 2 == 0: Ensures the weight is even.
One-Liner Print Statement: Reduces unnecessary if-else block.
Time Complexity: 𝑂(1)(constant time check).
'''
