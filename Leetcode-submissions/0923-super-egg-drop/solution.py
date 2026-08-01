class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        #construct an tabulation array of k identical eggs
        a = [0] * (k+1)
        e = 0
        while a[k] < n:
            e += 1
            for eg in range(k, 0, -1):
                a[eg] = a[eg] + a[eg - 1] + 1
        return e
