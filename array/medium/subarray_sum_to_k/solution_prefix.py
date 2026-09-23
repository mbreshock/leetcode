class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        prefix = 0
        seen = {0: 1}
        for x in nums: 
            prefix += x
            total += seen.get(prefix - k, 0)
            seen[prefix] = seen.get(prefix, 0) + 1
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