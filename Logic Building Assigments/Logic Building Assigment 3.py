#https://codeforces.com/problemset/problem/118/A
def process_string(s):
    vowels = {'a', 'o', 'y', 'e', 'u', 'i'}  # Set of vowels (lowercase)
    s = s.lower()  # Convert entire string to lowercase
    result = []

    for char in s:
        if char not in vowels:  # Ignore vowels
            result.append('.' + char)  # Add '.' before consonant

    return ''.join(result)  # Join list into a string

# Read input and process
s = input().strip()
print(process_string(s))

"""
A. String Task
time limit per test2 seconds
memory limit per test256 megabytes
Petya started to attend programming lessons. On the first lesson his task was to write a simple program. The program was supposed to do the following: in the given string, consisting if uppercase and lowercase Latin letters, it:

deletes all the vowels,
inserts a character "." before each consonant,
replaces all uppercase consonants with corresponding lowercase ones.
Vowels are letters "A", "O", "Y", "E", "U", "I", and the rest are consonants. The program's input is exactly one string, it should return the output as a single string, resulting after the program's processing the initial string.

Help Petya cope with this easy task.

Input
The first line represents input string of Petya's program. This string only consists of uppercase and lowercase Latin letters and its length is from 1 to 100, inclusive.

Output
Print the resulting string. It is guaranteed that this string is not empty.
"""


'''
Optimizations & Explanation:
Convert to Lowercase First

Since we treat both uppercase and lowercase vowels the same, we first convert the entire string to lowercase using s.lower().
Use a Set for Vowel Lookup

A set { 'a', 'o', 'y', 'e', 'u', 'i' } allows O(1) average-time lookup for checking vowels.
Use List for Efficient String Manipulation

Instead of appending characters directly to a string (which is inefficient in Python), we build a list and use ''.join(result) at the end.
Efficient Iteration

The loop ignores vowels and adds "." + consonant" to the list.
Complexity Analysis:
O(n) → Iterates over n characters exactly once.
O(n) Space Complexity → Stores consonants in a list.

'''
