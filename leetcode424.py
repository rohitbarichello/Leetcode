def characterReplacement(s, k):
    maxCharFreq = longestSubstrLen = 0
    count = collections.Counter()
    
    for i in range(len(s)):
        print(s, k, maxCharFreq, longestSubstrLen, count)
        count[s[i]] += 1
        
        maxCharFreq = max(maxCharFreq, count[s[i]])
        
        if longestSubstrLen - maxCharFreq < k:
            longestSubstrLen += 1
        else:
            count[s[i - longestSubstrLen]] -= 1
            
    return longestSubstrLen