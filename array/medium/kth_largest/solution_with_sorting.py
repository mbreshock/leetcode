class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums.sort(reverse = True)
        return nums[k-1]

## Test cases: 
nums1 = [3,2,1,5,6,4]
k1 = 2
# Expected: 5
print(Solution().findKthLargest(nums1, k1))
# Output: 4

nums2 = [3,2,3,1,2,4,5,5,6]
k2 = 4
# Expected: 4
print(Solution().findKthLargest(nums2, k2))
# Output: 4