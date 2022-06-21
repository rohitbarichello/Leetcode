def reverseList(head):
    current = head
    reversedList = None

    while current != None:
        tempNode = ListNode(current.val, reversedList)
        reversedList = tempNode

        current = current.next

    return reversedList


# In Place Solution
def reverseList(head):
    newHead = None

    while head:
        nextNode = head.next
        head.next = newHead
        newHead = head
        head = nextNode

    return newHead
