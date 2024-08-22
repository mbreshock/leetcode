class Solution:
    def findComplement(self, num: int) -> int:
        # get the bit length required to represent the decimal number in binary
        bit_length = num.bit_length()
        
        # create a mask that is a binary number of all 1s the length of bit_length
        mask = (1 << bit_length) - 1
        #    = 2**bit_lenth - 1
        #    = 1[0]bit_length - 1 
        #    = [1]bit_length

        # return XOR between num and mask 
        # effectivley flipping all 1s to 0s and all 0s to 1s
        return num ^ mask
    
# Test case 1:
num1 = 5
Solution().findComplement(num1)

#Test case 2:
num2 = 1
Solution().findComplement(num2)