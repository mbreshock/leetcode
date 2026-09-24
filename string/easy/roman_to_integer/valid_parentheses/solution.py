class Solution:
    def isValid(self, s: str) -> bool:
        def p_match(open, close) -> bool: 
            if open == '(' and close == ')':
                return True
            elif open == '{' and close == '}':
                return True
            elif open == '[' and close == ']':
                return True
            else:
                return False

        stack = list()
        for p in s: 
            if p in [')', '}', ']']:
                if len(stack) == 0:
                    return False
                else: 
                    opener = stack.pop()
                    if not p_match(opener, p):
                        return False
            else: 
                stack.append(p)
        outcome = len(stack) == 0
        return outcome

# Tests
s1 = "()"
# Expected: true
print(Solution().isValid(s1))
# Output: true

s2 = "()[]{}"
# Expected: true
print(Solution().isValid(s2))
# Output: true

s3 = "(]"
# Expected: false
print(Solution().isValid(s3))
# Output: false

s4 = "([])"
# Expected: true
print(Solution().isValid(s4))
# Output: true

s5 = "([)]"
# Expected: false
print(Solution().isValid(s5))
# Output: false