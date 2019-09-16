init python:
    class recipe:
        def __init__(self,
                item, qtt, ing,
                tools =  None, req = None
            ):
            self.item = item
            self.qtt = qtt
            self.ing = ing
            self.tools = tools
            self.req = req #requirements
