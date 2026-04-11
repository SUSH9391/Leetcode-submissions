class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        # Dictionary to store the last two indices seen for each number
        # Key: number, Value: [second_to_last_idx, last_idx]
        history = {}
        min_dist = float('inf')

        for current_idx, num in enumerate(nums):
            if num in history:
                prev_indices = history[num]
                
                # If we've seen this number at least twice before
                if prev_indices[0] != -1:
                    # dist = k - i
                    dist = current_idx - prev_indices[0]
                    if dist < min_dist:
                        min_dist = dist
                
                # Shift indices: [last] becomes [second_to_last], [current] becomes [last]
                history[num] = [prev_indices[1], current_idx]
            else:
                # First time seeing the number
                history[num] = [-1, current_idx]

        return 2 * min_dist if min_dist != float('inf') else -1
