"""Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:

Input: s = "leetcode"

Output: 0

Explanation:

The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:

Input: s = "loveleetcode"

Output: 2

Example 3:

Input: s = "aabb"

Output: -1
"""
from collections import defaultdict
def first_non_repeating_char(s: str):
    count = defaultdict(int)
    for char in s:
        count[char] += 1
    
    print(count)
    for key, val in count.items():
        if val == 1:
            return s.index(key)
    return -1

print(first_non_repeating_char('leetcode'))
print(first_non_repeating_char('loveleetcode'))
print(first_non_repeating_char('aabb'))