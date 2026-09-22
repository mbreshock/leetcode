class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        is_prefix = True 
        i = 0
        while is_prefix: 
            letters = [s[i] for s in strs]
            if len(set(letters)) > 1:
                is_prefix = False
                break
            prefix += letters[0]
            i += 1
        return prefix

# problem: s[i] breaks when i reaches values out of range when strings are of unequal lengths.
# provided test cases below do not present this failure. 
# fix: use zip(*strs) to automatically handle unequal lengths, and return the indivudal letters
# of each array in order and place them in their own touples. 

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

