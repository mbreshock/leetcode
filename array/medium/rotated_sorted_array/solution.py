class Solution:
    def search(self, nums: list[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        while lo <= hi: 
            med = (hi + lo) // 2
            if nums[med] == target: 
                return med
            if nums[lo] <= nums[med]: 
                if nums[lo] <= target < nums[med]: 
                    hi = med - 1
                else:
                    lo = med + 1
            else: 
                if nums[med] < target <= nums[hi]:
                    lo = med + 1
                else: 
                    hi = med - 1
        return -1

# Tests
nums1 = [4,5,6,7,0,1,2]
target1 = 0
# Expected: 4
print(Solution().search(nums1, target1))
# Output: 4

nums2 = [4,5,6,7,0,1,2]
target2 = 3
# Expected: -1
print(Solution().search(nums2, target2))
# Output: -1

nums3 = [1]
target3 = 0
# Expected: -1
print(Solution().search(nums3, target3))
# Output: -1