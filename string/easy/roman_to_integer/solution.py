class Solution:
    def romanToInt(self, s: str) -> int:
        symbs = {
            'I':1,
            'V':5,
            'X':10,
            'L':50, 
            'C':100, 
            'D':500, 
            'M':1000
        }
        v = 0
        subtract = False
        for i, c in enumerate(s): 
            if subtract: 
                v += symbs[c] - symbs[s[i-1]]
                subtract = False
            elif i < len(s) - 1 and symbs[s[i+1]] > symbs[c]:
                subtract = True
                continue
            else: 
                v += symbs[c]
        return v

# Test case 1:
s1 = "III"
# Expected: 3
print(Solution().romanToInt(s1))
# Output: 3

# Test case 2:
s2 = "LVIII"
# Expected: 58
print(Solution().romanToInt(s2))
# Output: 58

# Test case 3:
s3 = "MCMXCIV"
# Expected: 1994
print(Solution().romanToInt(s3))
# Output: 1994