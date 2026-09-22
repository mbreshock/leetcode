class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        for letters in zip(*strs):
            if len(set(letters)) > 1:
                break
            prefix += letters[0]
        return prefix

# Test case 1:
strs1 = ["flower","flow","flight"]
# Expected: "fl"
print(Solution().longestCommonPrefix(strs1))
# Output: "fl"

# Test case 2: 
strs2 = ["dog","racecar","car"]
# Expected: ""
print(Solution().longestCommonPrefix(strs2))
# Output: ""

