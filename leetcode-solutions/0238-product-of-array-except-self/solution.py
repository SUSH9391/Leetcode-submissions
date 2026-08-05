class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #since we are talking about the product we are supposed to initalize the array in such a way that its pre element places are supposed to be initalized to 1 coz 0* anything is zero
        res = [1] * len(nums)
        prevProd = 1
        postProd = 1
        for i in range(len(nums)):
            res[i] *= prevProd # we need to keep updated the prefix initally the prefix is 1 coz the 1st element has no prefix element 
            prevProd *= nums[i] #[1, 2, 3] 1*1, 1*2(for nums(1)) 2*3(for nums(2))
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postProd
            postProd *= nums[i]
        return res
       
