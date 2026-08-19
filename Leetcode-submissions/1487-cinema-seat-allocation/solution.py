class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reserved_map = collections.defaultdict(set) #hashset
        for row, seat in reservedSeats:
            if 2 <= seat <=9:
                reserved_map[row].add(seat)
        max_families = n*2
        for row , seats in reserved_map.items():
            left_free = not {2, 3, 4,5}.intersection(seats)
            right_free = not {6, 7, 8, 9}.intersection(seats)
            middle_free = not {4, 5, 6, 7}.intersection(seats)
            
            # If both left and right are free, it fits 2 families (no deduction needed)
            if left_free and right_free:
                continue
            # If we can fit at least one block (left, right, OR middle), deduct 1 from our max
            elif left_free or right_free or middle_free:
                max_families -= 1
            # If no blocks can fit, deduct 2
            else:
                max_families -= 2
                
        return max_families

