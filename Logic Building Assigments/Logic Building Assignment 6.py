#https://codeforces.com/problemset/problem/160/A
def min_coins_for_split(n, coins):
    total_sum = sum(coins)  # Total sum of all coins
    coins.sort(reverse=True)  # Sort coins in descending order
    current_sum = 0
    count = 0
    for coin in coins:
        current_sum += coin
        count += 1
        if current_sum > total_sum - current_sum:  # Condition met when your sum is greater
            break
    return count

# Input
n = int(input())
coins = list(map(int, input().split()))

# Output
print(min_coins_for_split(n, coins))

"""
A. Twins
time limit per test2 seconds
memory limit per test256 megabytes
Imagine that you have a twin brother or sister. Having another person that looks exactly like you seems very unusual. It's hard to say if having something of an alter ego is good or bad. And if you do have a twin, then you very well know what it's like.

Now let's imagine a typical morning in your family. You haven't woken up yet, and Mom is already going to work. She has been so hasty that she has nearly forgotten to leave the two of her darling children some money to buy lunches in the school cafeteria. She fished in the purse and found some number of coins, or to be exact, n coins of arbitrary values a1, a2, ..., an. But as Mom was running out of time, she didn't split the coins for you two. So she scribbled a note asking you to split the money equally.

As you woke up, you found Mom's coins and read her note. "But why split the money equally?" — you thought. After all, your twin is sleeping and he won't know anything. So you decided to act like that: pick for yourself some subset of coins so that the sum of values of your coins is strictly larger than the sum of values of the remaining coins that your twin will have. However, you correctly thought that if you take too many coins, the twin will suspect the deception. So, you've decided to stick to the following strategy to avoid suspicions: you take the minimum number of coins, whose sum of values is strictly more than the sum of values of the remaining coins. On this basis, determine what minimum number of coins you need to take to divide them in the described manner.

Input
The first line contains integer n (1 ≤ n ≤ 100) — the number of coins. The second line contains a sequence of n integers a1, a2, ..., an (1 ≤ ai ≤ 100) — the coins' values. All numbers are separated with spaces.

Output
In the single line print the single number — the minimum needed number of coins.

Examples
Input
2
3 3
Output
2
Input
3
2 1 2
Output
2
"""

'''
You need to select the minimum number of coins such that their total value is strictly greater than the remaining coins' total value. 
The strategy is to choose coins starting from the largest value, which ensures that you reach the required sum with the fewest coins.

Steps
Sort the coins in descending order to pick the largest ones first.
Iterate through the sorted list, keep a running sum of selected coins.
Stop when the sum of selected coins exceeds half of the total sum of all coins.
Count and print the number of coins needed.

Time and Space Complexity
Time Complexity: O(n log n) (due to sorting the coins, where n is the number of coins).
Space Complexity: O(n) (to store the coins and their sum).
'''
