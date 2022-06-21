def isValid(s):
    open = ["(", "[", "{"]
    closed = [")", "]", "}"]
    close_stack = []
    is_closed = True
    
    for i in s:
        if i not in open and i not in closed:
            continue
        elif is_closed == True and i in closed:
            return False
        elif i in open:
            is_closed = False
            close_stack.append(closed[open.index(i)])
        elif i in closed:
            popped = close_stack.pop()
            if i == popped:
                if len(close_stack) < 1:
                    is_closed = True
                continue
            else:
                return False
    print(close_stack)
    
    if len(close_stack) > 0:
        return False
    else:
        return True