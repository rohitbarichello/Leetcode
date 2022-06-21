def findMin(nums):
    left = 0
    right = len(nums) - 1

    if nums[left] <= nums[right]:
        return nums[left]

    while (right - left) > 1:
        mid = (right + left) // 2

        print(nums[left], nums[mid], nums[right])

        if nums[left] < nums[mid]:
            left = mid
        else:
            right = mid

    return min(nums[left], nums[right])
