class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        # if starting bill is not 5, return false
        if bills[0] != 5:
            return False
        
        # initialize variables to store five and ten dollars
        fives = 0
        tens = 0

        for bill in bills:
            # if 5, no change required, add to fives
            if bill == 5:
                fives += 1
            # if 10, 5 change required, add to tens
            elif bill == 10: 
                if fives > 0:
                    fives -= 1
                else: # if no fives to give change, return false
                    return False
                tens += 1
            else: # twenty dollar bill
                # if a five and ten are available
                if fives > 0 and tens > 0: 
                    fives -= 1
                    tens -= 1
                # or if 3 fives are available
                elif fives > 2:
                    fives -= 3
                else: # otherwise, return false
                    return False
            print(fives, tens)
        return True
    
# Test case 1: 
bills1 = [5,5,5,10,20]
# expected: True
Solution().lemonadeChange(bills1)
# output: True

# Test case 2: 
bills2 = [5,5,10,10,20]
# expected: False
Solution().lemonadeChange(bills2)
# output: False