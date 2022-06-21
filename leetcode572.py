def treesAreEqual(a, b):
    if not a and not b:
        return True

    if (not a and b) or (a and not b):
        return False

    if a.val == b.val:
        return treesAreEqual(a.left, b.left) and treesAreEqual(a.right, b.right)
    else:
        return False


def compareTrees(a, b):
    if not a:
        return False

    if a.val == b.val:
        if treesAreEqual(a, b):
            return True

    return compareTrees(a.left, b) or compareTrees(a.right, b)


def isSubtree(root, subRoot):
    return compareTrees(root, subRoot)
