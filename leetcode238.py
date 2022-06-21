def productExceptSelf(nums):
    cProduct = 1
    output = []

    for i in range(len(nums)):
        output.append(cProduct)
        cProduct = cProduct * nums[i]

    cProduct = 1

    for i in range(len(nums) - 1, -1, -1):
        output[i] = output[i] * cProduct
        cProduct = cProduct * nums[i]

    return output
