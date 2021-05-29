"""
Queue using two Stacks 

Implement a Queue using 2 stacks s1 and s2 .
A Query Q is of 2 Types
(i) 1 x (a query of this type means  pushing 'x' into the queue)
(ii) 2   (a query of this type means to pop element from queue and print the poped element)

Example 1:

Input:
5
1 2 1 3 2 1 4 2

Output: 
2 3

Explanation: 
In the first testcase
1 2 the queue will be {2}
1 3 the queue will be {2 3}
2   poped element will be 2 the queue 
    will be {3}
1 4 the queue will be {3 4}
2   poped element will be 3.
Example 2:

Input:
4
1 2 2 2 1 4

Output: 
2 -1

Explanation: 
In the second testcase 
1 2 the queue will be {2}
2   poped element will be 2 and 
    then the queue will be empty
2   the queue is empty and hence -1
1 4 the queue will be {4}.

"""
class Queue:
    pass
    # def __init__(self):
    #     self.stack1 = []
    #     self.stack2 = []
    # def __repr__(self) -> str:
    #     return " ".join([str(i) for i in self.stack2])

    # def isEmpty(self):
    #     return self.stack1 == []

    # def enqueue(self,data):
    #     if data == 1:
    #         self.stack1.append(data)
    #     else:
    #         self.stack2.append(data)

    # def dequeue(self,data):
    #     if self.isEmpty():
    #         return -1
    #     if data == 2:
    #         self.stack1.append(data)
    #     else:
    #         self.stack2.pop(0)
    

if __name__ == "__main__":
    myQueue = Queue()
    data = [1, 2, 3, 4, 5]
    res = myQueue.enqueue(data)
    print(res)
    # for key in keys:
    #     myQueue.enqueue(key)
 
    # print(myQueue.dequeue(key))        # 1
    # print(myQueue.dequeue(key)) 

