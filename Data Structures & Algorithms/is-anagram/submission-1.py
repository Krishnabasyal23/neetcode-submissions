
#Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

#An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if Counter(s.lower())==Counter(t.lower()):
            return True
        return False