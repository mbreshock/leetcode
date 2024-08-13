class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = [] # list to store valid combinations 
        test_combs = [] # list to store possible combination
        candidates.sort() # sort to avoid duplicates

        # define function to find combinations from candidates list recursively
        def find_combs(ind, target): 
            # elements from candidates will be recursively subtracted from target
            # so if target has reached zero, than we have a valid combination
            if target == 0: 
                ans.append(test_combs[:]) # append combination list to final answer
                return 
            
            for i in range(ind, len(candidates)):
                # if the current element is the same as the previous, skip
                if i > ind and candidates[i] == candidates[i - 1]:
                    continue

                # if the current element is larger than the target,
                # then no combination can be summed to the target. 
                # since we sorted candidates in ascending order, all future
                # elements will also be too large. Break
                if candidates[i] > target:
                    break

                test_combs.append(candidates[i])
                find_combs(i + 1, target - candidates[i])
                test_combs.pop()
        
        # begin recursive loop, starting at ind = 0:
        find_combs(0, target)
        return ans    
    
# Test case 1:
candidates1 = [2,5,2,1,2]
target1 = 5
# Expected: [[1,2,2],[5]]
Solution().combinationSum2(candidates1, target1)
# Output: [[1, 2, 2], [5]]

# Test case 2: 
candidates2 = [10,1,2,7,6,1,5]
target2 = 8
# Expected: [[1,1,6],[1,2,5],[1,7],[2,6]]
Solution().combinationSum2(candidates2, target2)
# Output: [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]