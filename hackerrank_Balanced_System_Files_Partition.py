# def mostBalancedPartition(parent, files_size):
#     n = len(parent)
#     children = [[] for _ in range(n)]
#     for i in range(1, n):
#         children[parent[i]].append(i)
#     size_sums = [None for _ in range(n)]
    
#     def size_sums_rec(i):
#         size_sums[i] = files_size[i] + sum(size_sums_rec(c) for c in children[i])
#         return size_sums[i]
        
#     size_sums_rec(0)
#     return min(abs(size_sums[0] - 2 * ss) for ss in size_sums[1:])


def branch_sum(parent, files_size, children, branch_sums, i):
    if not children[i]:
        print("not children", i)
        branch_sums[i] += files_size[i]
        return files_size[i]

    else:
        for child in children[i]:
            print("children", i, child)
            branch_sums[i] += files_size[i] + branch_sum(parent, files_size, children, branch_sums, child)



def mostBalancedPartition(parent, files_size):
    smallestDiff = 0

    children = [[] for i in range(len(parent))]

    for i in range(1, len(parent)):
        children[parent[i]].append(i)
    
    branch_sums = [0 for i in range(len(parent))]

    print(children)
    print(branch_sums)

    branch_sum(parent, files_size, children, branch_sums, 0)
    print(branch_sums)

    return smallestDiff


# testing
parent = [-1, 0,0,1,1,2]
files_size = [1,2,2,1,1,1]

print("\n", mostBalancedPartition(parent, files_size))



