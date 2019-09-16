init python:
    class bag:
        def __init__(self, name, items = []):
            self.name = name
            self.items = items
        
        def add(self, x, q): # x = item, q = Quantity
            if len(self.items):
                for i in self.items:
                    if i.item == x:
                        i.qtt += q
                        break
                else:
                    self.items.append(stack(x, q))
            else:
                self.items.append(stack(x, q))
        
        def rem(self, x, q):
            if len(self.items):
                for i in self.items:
                    if i.item == x and i.qtt >= q:
                        if i.qtt > q:
                            i.qtt -= q
                        elif i.qtt == q:
                            self.items.remove(i)
                        return True
                        break
                else:
                    return False
            else:
                return False
        
        def exist(self, x, q):
            if len(self.items):
                for i in self.items:
                    if i.item == x and i.qtt >= q:
                        return True
                        break
                else:
                    return False
            else:
                return False