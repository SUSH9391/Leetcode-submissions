class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        seen = set()
        for H in range(n):
            if digits[H] == 0:
                continue
            for T in range(n):
                if T == H:
                    continue
                for U in range(n):
                    if U==T or U == H:
                        continue
                    if digits[U] % 2 != 0:
                        continue
                    num = digits[H]*100 + digits[T]*10 + digits[U]
                    seen.add(num)
        return len(seen)
