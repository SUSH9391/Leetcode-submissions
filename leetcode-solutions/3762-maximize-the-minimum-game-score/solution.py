from typing import List

class Solution:
    def maxScore(self, points: List[int], m: int) -> int:

        def is_possible(target: int) -> bool:
            moves = 0
            prev = 0

            for i, p in enumerate(points):
                # Minimum visits still needed at this index
                need = (target + p - 1) // p
                need = max(0, need - prev)

                if need > 0:
                    moves += 2 * need - 1
                    prev = need - 1
                elif i != len(points) - 1:
                    moves += 1
                    prev = 0

                if moves > m:
                    return False

            return True

        left = 0
        right = ((m + 1) // 2) * points[0] + 1

        while left < right:
            mid = (left + right + 1) // 2

            if is_possible(mid):
                left = mid
            else:
                right = mid - 1

        return left
