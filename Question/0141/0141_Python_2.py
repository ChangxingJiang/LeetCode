from toolkit import ListNode,build_ListNode_with_pos


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False


if __name__ == "__main__":
    print(Solution().hasCycle(build_ListNode_with_pos([3, 2, 0, -4], pos=1)))  # True
    print(Solution().hasCycle(build_ListNode_with_pos([1, 2], pos=0)))  # True
    print(Solution().hasCycle(build_ListNode_with_pos([1], pos=-1)))  # False
