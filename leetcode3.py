def lengthOfLongestSubstring(s):
    charsUsed = {} # stores the chars that have shown up in s and their most recent indices
    longest = 0
    substrStart = 0
    
    for i, char in enumerate(s):
        if char in charsUsed and substrStart <= charsUsed[char]:
            substrStart = charsUsed[char] + 1
        else:
            longest = max(longest, i - substrStart + 1)
        
        charsUsed[char] = i
    
    return longest

