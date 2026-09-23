import heapq as hq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        h = []
        for x in nums: 
            hq.heappush(h, x)
            if len(h) > k: 
                hq.heappop(h)
        return h[0]

## Test cases: 
nums1 = [3,2,1,5,6,4]
k1 = 2
# Expected: 5
print(Solution().findKthLargest(nums1, k1))
# Output: 5

nums2 = [3,2,3,1,2,4,5,5,6]
k2 = 4
# Expected: 4
print(Solution().findKthLargest(nums2, k2))
# Output: 4