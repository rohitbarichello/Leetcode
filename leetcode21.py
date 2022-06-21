def mergeTwoLists(list1, list2):
    mergedList = ListNode()
    current = mergedList

    while list1 and list2:
        if list1.val < list2.val:
            current.next = ListNode(list1.val)
            list1 = list1.next
        else:
            current.next = ListNode(list2.val)
            list2 = list2.next

        current = current.next

    if list1:
        current.next = list1
    else:
        current.next = list2

    return mergedList.next
