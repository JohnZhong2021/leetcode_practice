class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        length_of_nums = len(nums)
        j = 1
        i = 0
        for i in range(0, length_of_nums):
            while j <= length_of_nums - 1:
                result = nums[i] + nums[j]
                if result == target:
                    return [i, j]
                else:
                    pass
                j += 1
            i += 1
            j = i +1


output = Solution.twoSum(Solution,[2, 9, 5, 7, 9], 16)
print(output)
