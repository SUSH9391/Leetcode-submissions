class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        #so the problem here is to make sure how can we give the customer the change 
        five =0 
        ten = 0
        for b in bills:
            if b == 5:
                five += 1
            if b ==10:
                ten += 1
            change = b - 5
            if change == 5:
                if five > 0:
                    five -= 1
                else:
                    return False
            elif change == 15:
                if five > 0 and ten > 0:
                    five, ten = five - 1 , ten - 1
                elif five >= 3:
                    five -= 3
                else :
                    return False
        return True
