def isValid(s):
    stack = []
    dict = {
        "(":")",
        "{":"}",
        "[":"]"
    }
    
    for char in s:
        if char in dict.keys():
            stack.append(char)
        else:
            if len(stack) > 0:
                if dict[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
            else:
                return False
    
    return len(stack) == 0