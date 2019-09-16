init python:
    class stack:
        def __init__(self, item, qtt):
            self.item = item
            self.qtt = qtt # Quantity
        
        def sum(self): # Returns the total value for the items in this stack
            return self.item.val*self.qtt