def topKFrequent(nums, k):
    # create a hashmap for occurences of each number in nums
    element_freqs = Counter(nums)

    # min heap to store our occurrences
    minHeap = []

    # place items in heap of size k until all elements have passed through
    for key in element_freqs.keys():
        if len(minHeap) == k:
            if element_freqs[key] > minHeap[0][0]:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, (element_freqs[key], key))
        else:
            heapq.heappush(minHeap, (element_freqs[key], key))

    # turn tuple array back into array of numbers
    k_most_frequent = []
    for element in list(minHeap):
        k_most_frequent.append(element[1])

    return k_most_frequent
