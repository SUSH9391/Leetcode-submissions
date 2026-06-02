class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        min_finish_time = float('inf')
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                land_end = landStartTime[i] + landDuration[i]
                water_start = max(land_end, waterStartTime[j])
                water_end = water_start + waterDuration[j]
                
                min_finish_time = min(min_finish_time, water_end)
                w_end = waterStartTime[j] + waterDuration[j]
                l_start = max(w_end, landStartTime[i])
                l_end = l_start + landDuration[i]
                
                min_finish_time = min(min_finish_time, l_end)
                
        return min_finish_time
