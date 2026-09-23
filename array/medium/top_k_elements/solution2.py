from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return [x for x, _ in Counter(nums).most_common(k)]

## Test cases: 
nums1 = [1,1,1,2,2,3] 
k1 = 2
# Expected: [1,2]
print(Solution().topKFrequent(nums1, k1))
# Output: [1,2]

nums2 = [1]
k2 = 1
# Expected: [1]
print(Solution().topKFrequent(nums2, k2))
# Output: [1]

nums3 = [1,2,1,2,1,2,3,1,3,2]
k3 = 2
# Expected: [1,2]
print(Solution().topKFrequent(nums3, k3))
# Output: [1,2]