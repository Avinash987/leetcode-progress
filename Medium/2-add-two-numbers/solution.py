# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Add two numbers represented as linked lists.
        
        Args:
            l1: First linked list (digits in reverse order)
            l2: Second linked list (digits in reverse order)
            
        Returns:
            New linked list representing the sum
        """
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Process both lists
        while l1 or l2 or carry:
            # Get values from current nodes (0 if node is None)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and new carry
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            # Create new node with the digit
            current.next = ListNode(digit)
            current = current.next
            
            # Move to next nodes
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next


# Helper functions for testing
def create_linked_list(arr):
    """Create a linked list from an array."""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_array(head):
    """Convert a linked list to an array."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# Example usage
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: 342 + 465 = 807
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])
    result = solution.addTwoNumbers(l1, l2)
    print(f"Input: l1 = [2,4,3], l2 = [5,6,4]")
    print(f"Output: {linked_list_to_array(result)}")
    print(f"Expected: [7,0,8]\n")
    
    # Test case 2: 0 + 0 = 0
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    result = solution.addTwoNumbers(l1, l2)
    print(f"Input: l1 = [0], l2 = [0]")
    print(f"Output: {linked_list_to_array(result)}")
    print(f"Expected: [0]")
