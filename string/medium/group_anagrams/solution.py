from collections import defaultdict

class Solution: 
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for s in strs: 
            key = tuple(sorted(s))
            groups[key].append(s)
        return list(groups.values())

# Test case 1:
strs1 = ["eat","tea","tan","ate","nat","bat"]
# Expected: [["bat"],["nat","tan"],["ate","eat","tea"]]
print(Solution().groupAnagrams(strs1))
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

# Test case 2: 
strs2 = [""]
# Expected: [[""]]
print(Solution().groupAnagrams(strs2))
# Output: [['']]

# Test case 2: 
strs3 = ["a"]
# Expected: [["a"]]
print(Solution().groupAnagrams(strs3))
# Output: [['a']]