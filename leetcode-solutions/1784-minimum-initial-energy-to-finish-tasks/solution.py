class Solution:
    def minimumEffort(self, tasks):
        # Sort by (minimum - actual) descending
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)

        ans = 0
        energy = 0

        for actual, minimum in tasks:

            # Need more energy to start this task
            if energy < minimum:
                ans += minimum - energy
                energy = minimum

            # Finish task
            energy -= actual

        return ans
