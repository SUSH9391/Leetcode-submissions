class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * n
        stack = []
        prev_time = 0
        for log in logs:
            idd, typ, time = log.split(":")
            idd = int(idd)
            time = int(time)
            if typ == "start":
                if stack:
                    result[stack[-1]] += time - prev_time 
                stack.append(idd)
                prev_time = time
            else:
                result[stack.pop()] += time - prev_time +1
                prev_time = time +1
        return result

