class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.index = k - 1 # convert to python indexing
        self.stream = list(nums) # save stream to class

    def add(self, val: int) -> int:
        self.stream.append(val)
        self.stream.sort(reverse = True)
        return self.stream[self.index]
    
# Testcase: 
# ["KthLargest","add","add","add","add","add"]
# [[3,[4,5,8,2]],[3],[5],[10],[9],[4]]

obj = KthLargest(3, [4,5,8,2])
obj.add(3) # should be 4
obj.add(5) # should be 5
obj.add(10) # should be 5
obj.add(9) # should be 8
obj.add(4) # should be 8