def containsDuplicate(nums):
    uniqueNums = {}

    for num in nums:
        if num in uniqueNums:
            return True
        else:
            uniqueNums[num] = num

    return False
