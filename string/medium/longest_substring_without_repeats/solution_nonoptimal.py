class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        best = 0
        for right in range(len(s)):
            while len(set(s[left:right+1])) < right+1 - left:
                left += 1
            best = max(best, len(s[left:right+1]))
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