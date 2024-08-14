class Solution:
    def smallestDistancePair(self, nums: list[int], k: int) -> int:
        nums.sort() # sort to avoid duplicates

        # define function to calculate distances recursively 
        # and store them in list
        def calc_distances(ind, nums):
            distances = [] # list to store distances between all possible combinations in nums
            for i in range(ind, len(nums)-1):
                for j in range(i+1, len(nums)):
                    # calculate distance
                    dist = abs(nums[j] - nums[i])
                    distances.append(dist)
            return distances
        # return the k-th smallest distance:
        d = calc_distances(0, nums)
        d.sort()
        return d[k-1]


# Test case 1: 
nums1 = [1,3,1]
k1 = 1
Solution().smallestDistancePair(nums1, k1) # 0

# Test case 2: 
nums2 = [1,1,1]
k2 = 2
Solution().smallestDistancePair(nums2, k2) # 0

# Test case 3: 
nums3 = [1,6,1]
k3 = 3
Solution().smallestDistancePair(nums3, k3) # 5