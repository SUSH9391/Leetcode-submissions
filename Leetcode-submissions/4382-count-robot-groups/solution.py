class Solution:
    def countGroups(self, position: list[int], speed: list[int], distance: int) -> int:
        n = len(position)
        inital_groups_speeds = []
        for i in range(n):
            if i == n-1 or position[i+1] - position[i] > distance:
                inital_groups_speeds.append(speed[i])
        final_groups_count = 0
        current_min_speed = float('inf')
        for s in reversed(inital_groups_speeds):
            if s <= current_min_speed:
                final_groups_count += 1
                current_min_speed = s
        return final_groups_count
