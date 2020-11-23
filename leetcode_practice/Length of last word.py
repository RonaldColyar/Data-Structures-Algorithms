

"""
Given a string s consists of some words separated by spaces, 
return the length of the last word in the string. If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5

Example 2:

Input: s = " "
Output: 0

 

Constraints:

    1 <= s.length <= 104
    s consists of only English letters and spaces '
"""

#time complexity = O(n) due to .split method



#easy problem



class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
    
        if len(words) == 1:
            return len(words[0])
        elif len(words) == 0:
            return 0
        else:
            last_word = words[len(words)-1]
            return len(last_word)
          
            