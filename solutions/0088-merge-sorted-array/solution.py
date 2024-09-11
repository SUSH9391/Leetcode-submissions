class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1, n2, i = m-1, n-1, m+n-1
        while n2 >= 0:
            if n1 >=0 and nums1[n1] > nums2[n2]:
                nums1[i] = nums1[n1]
                n1 -= 1
            else:
                nums1[i] = nums2[n2]
                n2 -= 1
            i -= 1
        
        
