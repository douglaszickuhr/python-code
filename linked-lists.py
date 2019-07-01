class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = ''
        while l1.next is not None:
            num1 += str(l1.val)

        while l2.next is not None:
            num2 += str(l2.val)

        my_sum = int(num1[::-1]) - int(num2[::-1])
        return my_sum