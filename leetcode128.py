def longestConsecutive(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return 1

    minHeap = nums
    heapq.heapify(minHeap)

    prev = heapq.heappop(minHeap)
    longest = 1
    currentLength = 1

    while len(minHeap) > 0:
        prevprev = prev
        prev = heapq.heappop(minHeap)

        if prev == prevprev + 1:
            currentLength += 1
        elif prev == prevprev:
            pass
        else:
            if currentLength > longest:
                longest = currentLength
            currentLength = 1

    return max(longest, currentLength)


def longestConsecutive(nums):
    nums = set(nums)  # eliminates duplicates in nums
    longest = 0

    for num in nums:
        if num - 1 not in nums:  # we aren't at the start of a streak
            y = num + 1  # start stepping one by one through nums
            while y in nums:  # exit once we end the streak
                y += 1

            longest = max(
                longest, y - num
            )  # y - num is equal to the amount of steps we took
    return longest
