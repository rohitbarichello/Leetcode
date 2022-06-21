# SOLUTION 1, Recursive DFS
def maxDepth(root):
    if root:
        return max(maxDepth(root.right) + 1, maxDepth(root.left) + 1)
    else:
        return 0


# SOLUTION 2, Level Order BFS with queue
def maxDepth(root):
    depth = 0

    if root:
        queue = [root]

        while len(queue) > 0:
            nextLevel = []

            while len(queue) > 0:
                front = queue.pop()

                if front.left:
                    nextLevel.insert(0, front.left)
                if front.right:
                    nextLevel.insert(0, front.right)

            queue = nextLevel
            depth += 1

    return depth
