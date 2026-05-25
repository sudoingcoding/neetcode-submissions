class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check=set(nums)
        longest=0

        for l in nums:
            if (l-1) not in check:
                length=0
                while (l+length) in check:
                    length+=1
                longest=max(longest,length)
        return longest