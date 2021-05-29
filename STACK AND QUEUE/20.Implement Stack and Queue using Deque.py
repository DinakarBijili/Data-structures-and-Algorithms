"""=============EXPLAINED ABOUT STACK AND QUEUE============="""

"""
Implement Stack and Queue using Deque

Deque also known as double eneded queue, as name suggests is a special kind of queue in which insertions and deletions can be done at the last as well as at the beginning.

A link-list representation of deque is such that each node points to the next node as well as the previous node. So that insertion and deletions take constant time at both the beginning and the last.

Head            Tail
    \          / 
    A -> B -> C -> D-
      <-   <-   <-

Now, deque can be used to implement a stack and queue. One simply needs to understand how deque can made to work as a stack or a queue.
The functions of deque to tweak them to work as stack and queue are list below.

DEQUE           STACK(LIFO) QUEUE(FIFO)   
size()          size()      size()
isEmpty()       isEmpty()   isEmpty()
InsertFirst()       -           -
Inser_Last()    push()       Enqueue()
Remove_First()      -        Dequeue()  
Remove_Last()   pop()           -    

Examples: Stack:-
Input : Stack : 1 2 3
        Push(4)
Output : Stack : 1 2 3 4

Input : Stack : 1 2 3
        Pop()
Output : Stack : 1 2

------------------------------
Examples: Queue:-
Input: Queue : 1 2 3
       Enqueue(4)
Output: Queue : 1 2 3 4

Input: Queue : 1 2 3
       Dequeue()
Output: Queue : 2 3

"""


