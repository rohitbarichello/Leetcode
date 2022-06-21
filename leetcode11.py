def maxArea(heights) -> int:
    left = 0
    right = len(heights) - 1
    maxArea = 0

    while left < right:
        width = right - left
        height = min(heights[left], heights[right])
        area = width * height

        if area > maxArea:
            maxArea = area

        if heights[left] > heights[right]:
            right -= 1
        else:
            left += 1

    return maxArea
