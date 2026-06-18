class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h_angle = (hour % 12 + minutes / 60) * 30
        m_angle = minutes *6
        angle = abs(h_angle - m_angle)
        return min(angle, 360 - angle)
