def findMax(space, x):
    segment = 1

    stack = (
        []
    )  # holds indices of computers in "space" that are the smallest in their segment
    stack.append(0)

    # loop through the indices of space starting at 1 because 0 is already added to the stack
    for i in range(1, len(space)):
        print(stack)
        top = stack[-1]

        if i < x:  # we're in the first segment, segment is 1
            if (
                space[i] < space[top]
            ):  # if the computer at this index is smaller that the current smallest on the stack
                stack.pop()
                stack.append(i)

        else:  # we're past the first segment
            if (
                top >= segment
            ):  # if top of stack is a member of the current chunk we just need to compare current number with it
                if space[i] < space[top]:
                    stack.append(i)
                else:
                    stack.append(top)

            else:  # we have to loop through current chunk to find minimum number
                stack.append(i)

                j = segment
                count = 0

                while count < x:
                    if space[j] < space[stack[-1]]:
                        stack.pop()
                        stack.append(j)

                    j += 1
                    count += 1

            segment += 1

    # Find max of our mins
    max = -1

    for index in stack:
        if space[index] > max:
            max = space[index]

    return max


print(findMax([2, 5, 4, 6, 8], 3))
