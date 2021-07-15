# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(next=head)
        curr = dummy
        total = 0
        mydict = {}
        while curr:
            total = total + curr.val
            if total in mydict.keys():
                to_remove = mydict[total].next
                temp_total = total
                # Remove the elements from the dict
                while to_remove != curr:
                    temp_total += to_remove.val
                    del mydict[temp_total]
                    to_remove = to_remove.next
                # Update the pointer
                mydict[total].next = curr.next
            else:
                mydict[total] = curr
            curr = curr.next
        return dummy.next