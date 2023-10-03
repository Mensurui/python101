class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode()
    p, q, current = l1, l2, dummy
    carry = 0

    while p or q:
        x = p.val if p else 0
        y = q.val if q else 0
        _sum = x + y + carry
        carry = _sum // 10

        current.next = ListNode(_sum % 10)
        current = current.next

        if p:
            p = p.next
        if q:
            q = q.next

    if carry:
        current.next = ListNode(carry)

    return dummy.next

def list_str_to_linkedlist(list_str):
    values = list_str.strip("[]").split(",")
    
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(int(val))
        current = current.next
    return dummy.next

list1_str = input("Enter the first list as [2,4,3]: ")
list2_str = input("Enter the second list as [5,6,4]: ")

l1 = list_str_to_linkedlist(list1_str)
l2 = list_str_to_linkedlist(list2_str)

result = addTwoNumbers(l1, l2)

while result:
    print(result.val, end="")
    result = result.next

