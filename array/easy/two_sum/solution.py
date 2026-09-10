class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = [0,0]
        for i, v in enumerate(nums):
            for j in range(i+1, len(nums)):
                if v + nums[j] == target:
                    ans[0], ans[1] = i, j
        return ans

# Test case 1:
nums1 = [2,7,11,15]
target1 = 9
# Expected: [0,1]
print(Solution().twoSum(nums1, target1))
# Output: [0, 1]

# Test case 2: 
nums2 = [3,2,4]
target2 = 6
# Expected: [1,2]
print(Solution().twoSum(nums2, target2))
# Output: [1, 2]

# Test case 3: 
nums3 = [3,3]
target3 = 6
# Expected: [0,1]
print(Solution().twoSum(nums3, target3))
# Output: [0, 1]