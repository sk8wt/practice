class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        cur, next_val = 0, 0
        
        while(cur < len(nums) -1): 
            next_val += 1
            
            for i in range(next_val, len(nums)):
                if (nums[i] + nums[cur] == target):
                    return [cur, i]
            
            cur += 1
        
