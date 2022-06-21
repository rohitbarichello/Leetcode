def twoSum(nums, target):
    complements = {}

    for i in range(len(nums)):
        num = nums[i]
        complement = target - num

        if complement in complements:
            return [i, complements[complement]]
        complements[num] = i
