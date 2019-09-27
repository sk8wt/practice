def reverse_list(new_list):
        num1 = new_list
        new_L1 = ""
        
        while(num1.next):
            new_L1 += str(num1.val)
            num1 = num1.next
        
        new_L1 += str(num1.val)
        reverse_L1 = ""
        
        for char in reversed(new_L1):
            reverse_L1 += char
        
        return reverse_L1
        

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        new_l1 = int(reverse_list(l1))
        new_l2 = int(reverse_list(l2))
        new_sum = new_l1 + new_l2
        new_list = []
        
        while (new_sum >= 10):
            remainder = new_sum % 10
            new_list.append(remainder)
            new_sum = new_sum // 10
        
        if (new_sum != 0):
            new_list.append(new_sum)
        
        node = ListNode(new_list[:-1])
        for i in range (len(new_list[:-2]), 0):
            node.next = ListNode(new_list[i])
            node.value = ListNode(i)
            
        node.next = ListNode(new_list[0])
            
        return node
        

    
        
