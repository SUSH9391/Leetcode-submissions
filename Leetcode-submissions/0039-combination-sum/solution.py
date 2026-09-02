class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return
        combination = []
        #cur is the list of values you mantain by taking current values
        #total is the sub obtained my the current combination
        def dfs(i,cur,total):
            if total == target:
                combination.append(cur[:])
                return 
            if i >= len(candidates) or total > target:
                return
            cur.append(candidates[i])
            dfs(i, cur, total+candidates[i])

            cur.pop()
            dfs(i+1, cur, total)
        dfs(0,[],0)
        return combination
