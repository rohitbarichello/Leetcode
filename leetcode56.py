def merge(intervals):
    # sort intervals by first number in list
    intervals.sort(key = lambda interval: interval[0])
    
    # create return array
    mergedIntervals = [intervals[0]]
    
    # start comparing and merging
    for start, end in intervals[1:]:
        lastEnd = mergedIntervals[-1][1]
        
        if start <= lastEnd:
            mergedIntervals[-1][1] = max(lastEnd, end)
        else:
            mergedIntervals.append([start, end])
    
    # return merged intervals
    return mergedIntervals
        