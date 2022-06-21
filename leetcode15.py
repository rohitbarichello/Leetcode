def threeSum(nums):
    # for each element in the array, check every element in the rest of the array
    threeSums = []
    nums.sort()

    for i in range(len(nums) - 2):
        # continue if we're on the first element or if the current element isn't equal to the previous
        # this kills duplicates
        if i == 0 or nums[i] != nums[i - 1]:
            left = i + 1
            right = len(nums) - 1

            while left < right:
                threeSum = nums[i] + nums[left] + nums[right]

                if threeSum < 0:
                    left += 1
                elif threeSum > 0:
                    right -= 1
                else:
                    threeSums.append([nums[i], nums[left], nums[right]])

                    # killing duplicates again
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

    return threeSums
