class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dic = {}
        i = 0
        j = 0
        len_nums = len(nums)
        while j < len_nums:
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                nums.pop(i)
                i-=1
            i+=1
            j+=1
        return len(nums)