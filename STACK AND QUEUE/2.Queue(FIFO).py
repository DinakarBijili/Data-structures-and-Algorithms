"""
Queue (First<-In First->Out )

Like Stack, Queue is a linear structure which follows a particular order in which the operations are performed. The order is First In First Out (FIFO).  A good example of queue is any queue of consumers for a resource where the consumer that came first is served first. 
The difference between stacks and queues is in removing. In a stack we remove the item the most recently added; in a queue, we remove the item the least recently added.
Operations on Queue: 
Mainly the following four basic operations are performed on queue:
Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition. 
Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition. 
Front: Get the front item from queue. 
Rear: Get the last item from queue.
    
(deleting and inserting)  Enqueue(adds)-> | | | | | -> Dequeue(remove)
                                         /         \
                                        Rear       Front 
"""
class Queue(object):
    def __init__(self,limit=10):
        self.queue = []
        self.limit = limit
        self.size = 0

    def __str__(self) -> str:
        return " ".join([str(i) for i in self.queue])


    def isEmpty(self):
        return self.size <= 0 

    def isFull(self):
        return self.size == self.limit

        # to add an element from the rear end of the queue
    def enqueue(self, data):
        if self.isFull():
            print("queue overflow")
            return         # queue overflow
        else:
            self.queue.append(data)
            self.size += 1
    
    # to pop an element from the front end of the queue
    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
            return           # queue underflow
        else:
            self.queue.pop(0)
            self.size -= 1
    
    def getSize(self):
        return self.size

    def getFront(self):
        if self.isEmpty():
            print("Queue is Empty")
            return 
        else:
            return self.queue[0]

    def getRear(self):
        if self.isEmpty():
            print("Queue is Empty ")
            return
        else:
            return self.queue[-1]

    
if __name__ == "__main__":
    #FIFO
    myQueue = Queue()
    myQueue.enqueue(1)
    myQueue.enqueue(2)
    myQueue.enqueue(3)
    myQueue.enqueue(4)
    myQueue.enqueue(5)
    print("Enqueue(INSERT):-", myQueue)
    print('Queue Size:',myQueue.getSize() ,'\n')
    myQueue.dequeue() # remove from 1st 
    myQueue.dequeue() # remove from 2nd 
    print("dequeue(DELETE):-", myQueue)
    print('Queue Size:',myQueue.getSize())
    print("Front item is:",myQueue.getFront())
    print("Rear item is:",myQueue.getRear())
    