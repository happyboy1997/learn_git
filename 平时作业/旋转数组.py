class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dic = {}
        len_nums = len(nums)
        if len_nums < 2:
            return 0
        for i in range(len_nums):
            if i+k>=len_nums:
                upd_i = i+k-len_nums
                while upd_i >= len_nums:
                    upd_i -= len_nums
                dic[upd_i] = nums[i]
                
            else:
                dic[i+k] = nums[i]
        for key in dic:
            nums[key] = dic[key]