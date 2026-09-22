class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi: 
            mid = (lo + hi) // 2
            if nums[mid] == target: 
                return mid
            elif nums[mid] < target: 
                lo = mid+1
            else: 
                hi = mid
        return lo

# Why this is O(log n) runtime complexity: 
# Halving the space every step means the number of iterations is proportional to log₂(n)

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