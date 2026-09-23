class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        for i, v in enumerate(nums): 
            if v == k and k != 0:
                total += 1
                continue
            if v == k and k == 0:
                total += 1
            if i == len(nums)-1:
                break
            for j in range(i+1, len(nums)):
                if sum(nums[i:j+1]) == k: 
                    total += 1 
        return total

# Tests: 
nums1 = [1,1,1]
k1 = 2
# expected: 2
print(Solution().subarraySum(nums1, k1))

nums2 = [1,2,3]
k2 = 3
# expected: 2
print(Solution().subarraySum(nums2, k2))