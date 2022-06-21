# DFS solution. Could do BFS by using a queue instead


def invertTree(root):
    stack = [root]

    while stack:
        current = stack.pop()

        if current:
            temp = current.left
            current.left = current.right
            current.right = temp

            stack.append(current.left)
            stack.append(current.right)

    return root
