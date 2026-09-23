class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        left = 0
        best = 0
        for right, ch in enumerate(s):
            if ch in last and last[ch] >= left:
                left = last[ch] + 1
            last[ch] = right
            best = max(best, right+1-left)
        return best

## Test cases: 
s1 = "abcabcbb"
# Expected: 3
print(Solution().lengthOfLongestSubstring(s1))
# Output: 3

s2 = "bbbbb"
# Expected: 1
print(Solution().lengthOfLongestSubstring(s2))
# Output: 1

s3 = "pwwkew"
# Expected: 3
print(Solution().lengthOfLongestSubstring(s3))
# Output: 3