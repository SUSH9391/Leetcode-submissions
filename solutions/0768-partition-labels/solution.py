class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_last_Seen = {} #"chat : count"
        #so we need to partion the given word such that the unique char appere atmost in one string the charater is not supposed to be split
        
        for i, c in enumerate(s):
            char_last_Seen[c] = i
        size , end = 0,0
        res = []
        for i , c in enumerate(s):
            size += 1 
            end = max(end, char_last_Seen[c])
            if i == end :
                res.append(size)
                size =0
        return res
