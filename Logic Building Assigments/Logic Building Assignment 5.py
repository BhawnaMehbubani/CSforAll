#https://codeforces.com/problemset/problem/339/A




"""A. Helpful Maths
time limit per test2 seconds
memory limit per test256 megabytes
Xenia the beginner mathematician is a third year student at elementary school. She is now learning the addition operation.

The teacher has written down the sum of multiple numbers. Pupils should calculate the sum. To make the calculation easier, the sum only contains numbers 1, 2 and 3. Still, that isn't enough for Xenia. She is only beginning to count, so she can calculate a sum only if the summands follow in non-decreasing order. For example, she can't calculate sum 1+3+2+1 but she can calculate sums 1+1+2 and 3+3.

You've got the sum that was written on the board. Rearrange the summans and print the sum in such a way that Xenia can calculate the sum.

Input
The first line contains a non-empty string s — the sum Xenia needs to count. String s contains no spaces. It only contains digits and characters "+". Besides, string s is a correct sum of numbers 1, 2 and 3. String s is at most 100 characters long.

Output
Print the new sum that Xenia can count.

Examples

Input
3+2+1
Output
1+2+3

Input
1+1+3+1+3
Output
1+1+1+3+3

Input
2
Output
2
"""

'''

Short Explanation
The task is to rearrange the summands in a given mathematical expression (containing the numbers 1, 2, and 3 separated by '+') into non-decreasing order, while keeping the '+' symbols intact. This ensures that Xenia, who only understands sums in non-decreasing order, can easily calculate the sum.

Steps
Split the input string s by the '+' character to get individual numbers.
Sort the resulting list of numbers.
Join the sorted numbers back into a string with '+' between them.
Output the result.
Time and Space Complexity
Time Complexity: O(n log n) (due to sorting the numbers, where n is the number of summands).
Space Complexity: O(n) (to store the numbers after splitting the input string).
'''
