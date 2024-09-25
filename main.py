#queues - (fifo in the first out)
class queue:
    def __init__(self):
        self.queue = []

        #method to check if queue is empty
    def isempty(self):
            return len(self.queue) == 0
    #method to add an item to thr queue
    def enqueue(self, item):
        self.queue.append(item)
        print(f"{item} is added in the queue")
#method to remove an item from the queue
    def dequeue(self):
        if self.isempty():
            return "queue is empty"
        else:
         return self.queue.pop(0) #removes the first one out from the queue
    
    #method to know which is the first item in the queue
    def first(self) :
        if self.isempty():
            return "Queue is empty"
        else:
            return self.queue[0]    
    
    #method to know which is the last item in the queue
    def last(self) :
        if self.isempty():
            return "Queue is empty"
        else:
            return self.queue[-1] 

    #method to display the queue
    def display(self) :
        if self.isempty():
            return "Queue is empty"
        else:
            return self.queue


q=queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.display())