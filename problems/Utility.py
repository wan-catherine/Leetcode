class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linklist_from_list(vals):
    head = ListNode(vals[0])
    current = head
    for i in vals[1:]:
        current.next = ListNode(i)
        current = current.next
    return head

def create_list_from_linklist(head):
    vars = []
    while head:
        vars.append(head.val)
        head = head.next
    return vars