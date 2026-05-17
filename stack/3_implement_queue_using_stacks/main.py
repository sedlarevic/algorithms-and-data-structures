from collections import deque

class MyQueue(object):
#double ended queue
    def __init__(self):
        self.elements=deque()

#dodajemo element desno
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.elements.append(x)
        
#izbaucjemo sa leve strane
    def pop(self):
        """
        :rtype: int
        """
        return self.elements.popleft()
        
#peekujemo sa leve strane
    def peek(self):
        """
        :rtype: int
        """
        return self.elements[0]

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.elements) == 0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
