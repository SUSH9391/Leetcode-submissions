class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec1[0] == rec1[2] or rec1[1] == rec1[3] or \
           rec2[0] == rec2[2] or rec2[1] == rec2[3]:
            return False
        
        # Conditions for NOT overlapping:
        # rec1 is to the left of rec2 OR
        # rec1 is to the right of rec2 OR
        # rec1 is below rec2 OR
        # rec1 is above rec2
        if (rec1[2] <= rec2[0] or  # left
            rec1[0] >= rec2[2] or  # right
            rec1[3] <= rec2[1] or  # below
            rec1[1] >= rec2[3]):   # above
            return False
            
        return True
