class Solution(object):
    def runningSum(self, nums):
        sum = 0
        P_A = []
        for i in range(len(nums)):
            sum += nums[i]
            P_A.append(sum)
        return P_A
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        