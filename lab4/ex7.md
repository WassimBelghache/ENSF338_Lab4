**1. Give an expression for the time complexity of the reverse()
implementation. Explain how you reached the conclusion
describing your step-by-step reasoning. [0.3 pts]**

The `reverse()` function exhibits a time complexity of O(n^2). The initial loop iterates through the linked list from the end, traversing each element once, resulting in an O(n) complexity. Inside the loop, the line "currNode = self.get_element_at_pos(i)" accesses elements in a reverse order (n-1, n-2, ..., 1, 0), following a quadratic pattern and resulting in an O(n^2) complexity. The "if" statements are constant and independent of the list's size. Consequently, the predominant time complexity is O(n^2).


**2. Design an optimized implementation of the same function with
better performance. Discuss which changes you made and how
they should be expected to result in a better function [0.3 pts]**
