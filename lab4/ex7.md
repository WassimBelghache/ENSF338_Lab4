**1. Give an expression for the time complexity of the reverse()
implementation. Explain how you reached the conclusion
describing your step-by-step reasoning. [0.3 pts]**

The `reverse()` function exhibits a time complexity of O(n^2). The initial loop iterates through the linked list from the end, traversing each element once, resulting in an O(n) complexity. Inside the loop, the line "currNode = self.get_element_at_pos(i)" accesses elements in a reverse order (n-1, n-2, ..., 1, 0), following a quadratic pattern and resulting in an O(n^2) complexity. The "if" statements are constant and independent of the list's size. Consequently, the predominant time complexity is O(n^2).


**2. Design an optimized implementation of the same function with
better performance. Discuss which changes you made and how
they should be expected to result in a better function [0.3 pts]**

In the optimized version, we temporarily store the next node while reversing the pointer of the current node to point to the previous node. We then move the previous node to the current node and the current node to the next node. This approach removes the need to access elements by position within the loop. As a result, the time complexity is linear, O(n), instead of quadratic, O(n^2).