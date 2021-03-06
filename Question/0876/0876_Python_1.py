from toolkit import ListNode


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


if __name__ == "__main__":
    print(Solution().middleNode(ListNode([1, 2, 3, 4, 5])).val)  # 3
    print(Solution().middleNode(ListNode([1, 2, 3, 4, 5, 6])).val)  # 4
