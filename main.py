class MyStack(object):

    def __init__(self):
      self.queue = []
      return None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if x == int(x):
          self.queue.insert(0, x)
          return x
        else: None

    def pop(self):
        """
        :rtype: int
        """
        for element in self.queue:
          if element:
            self.queue.remove(element)
            return element


    def top(self):
        """
        :rtype: int
        """
        for element in reversed(self.queue):
          if element:
            self.queue.remove(element)
            if len(self.queue) > 0:
              for position in self.queue:
                if position:
                  self.queue.insert(0, element)
                  return element
            else:
              self.queue.append(element)
              return element

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.queue) > 0: return False
        else: return True

# Apply with Colab or Jupyter
stack = MyStack()

stack.push(1)   # 1

stack.push(2)   # 2

stack.top()     # 2

stack.pop()     # 2

stack.empty()   # False