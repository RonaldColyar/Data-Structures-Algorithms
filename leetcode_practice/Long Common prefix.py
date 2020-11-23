"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

 

Constraints:

    0 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lower-case English letters.

"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        words = strs

        if len(words) == 0:
        	return ""
        elif len(words) == 1:
        	return words[0]
        else:
        	prefix = words[0]
        	prefix_size = len(starting_prefix)
        	for string in words[1:]: # start at 2nd string since we already have the first string as prefix
        		while prefix != string[0:prefix_size]:
        			prefix = prefix[0:(prefix_size-1)]
        			prefix_size = prefix_size -1

        			if prefix_size == 0 :
        				return ""

        	return prefix
