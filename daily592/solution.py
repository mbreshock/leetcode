import re
import math
class Solution:
    def fractionAddition(self, expression: str) -> str:
        nums = list(map(int, re.findall(r'[+-]?\d+', expression)))
        numerator = 0
        denominator = 1
        
        for i in range(0, len(nums), 2):
            num, den = nums[i], nums[i + 1]
            numerator = numerator * den + num * denominator
            denominator *= den
        
        common_divisor = math.gcd(numerator, denominator)
        return f"{numerator // common_divisor}/{denominator // common_divisor}"
        
# Test case 1:
expression1 = "-1/2+1/2"
# expected "0/1"
Solution().fractionAddition(expression1)

# Test case 2: 
expression2 = "-1/2+1/2+1/3"
# expected "1/3"
Solution().fractionAddition(expression2)

# Test case 3: 
expression3 = "1/3-1/2"
# expected "-1/6"
Solution().fractionAddition(expression3)
