class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_list={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in diff_list:
                return [diff_list[diff],i]
            diff_list[n]=i