def firstUniqChar(s):
    chars = {}

    # first pass to count character occurences
    for i in range(len(s)):
        char = s[i]

        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1

    # second pass to find first char with one occurence
    for i in range(len(s)):
        char = s[i]
        if chars[char] == 1:
            return i

    # if one isn't found, then return -1
    return -1
