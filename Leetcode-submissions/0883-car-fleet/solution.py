class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack= []
        pair = [[p,s] for p,s in zip(position,speed)]
        for p,s in sorted(pair)[::-1]: #we are supposed to sort the pair and take them in revese order as the cars eventually depend on the fastest car if they encounter a fastest car then the slower cars are gonna slower down and evolve into a fleet
            #we are evnetually gonna calculate the time at which the cars at each poistion are gonna reach the target as if there is a fleet at the destination then there is a chance we consider that fleet
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
