class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        
        charCount = {}
        currentRunningLen = globalMaxLen = 0
        leftWindow = rightWindow = 0
        charCount[s[0]] = 1

        while rightWindow < len(s):
            if s[rightWindow] in charCount and charCount[s[rightWindow]] > 1:
                charCount[s[leftWindow]] -= 1 
                leftWindow += 1
                currentRunningLen -= 1
            else:
                currentRunningLen += 1
                rightWindow += 1
                if rightWindow < len(s):
                    if s[rightWindow] in charCount:
                        charCount[s[rightWindow]] += 1
                    else:
                        charCount[s[rightWindow]] = 1
                    
            if currentRunningLen > globalMaxLen:
                globalMaxLen = currentRunningLen
         
        return globalMaxLen

import unittest

class lengthOfLongestSubstringCase(unittest.TestCase):
    def test_lengthOfLongestSubstring(self):
        func = Solution().lengthOfLongestSubstring
        self.assertEqual(func("abcabcbb"), 3)
        self.assertEqual(func("bbbbb"), 1)
        self.assertEqual(func("pwwkew"), 3)

if __name__ == "__main__":
    unittest.main()