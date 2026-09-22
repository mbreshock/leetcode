class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target > max(nums):
            return len(nums)
        elif target == max(nums):
            return len(nums) - 1
        elif target <= min(nums):
            return 0
        else: 
            for i, v in enumerate(nums): 
                if v >= target: 
                    return i

# problem: does not satisfy the O(log n) runtime complexity requirement.
# why: 
# 1. max(nums) and min(nums) each scan the entire array 
#    — that's O(n) just to check those conditions, called at the top of every invocation.
# 2. The for loop in the else branch walks through nums one element at a time until it 
# finds the insertion point — that's O(n) in the worst case (e.g., target belongs near the end).

# Test case 1:
nums1 = [1,3,5,6]
target1 = 5
# Expected: 2
print(Solution().searchInsert(nums1, target1))
# Output: 2

# Test case 2: 
nums2 = [1,3,5,6]
target2 = 2
# Expected: 1
print(Solution().searchInsert(nums2, target2))
# Output: 1

# Test case 3: 
nums3 = [1,3,5,6]
target3 = 7
# Expected: 4
print(Solution().searchInsert(nums3, target3))
# Output: 4