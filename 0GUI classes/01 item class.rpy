init python:
    class item:
        def __init__(self,
                name, val, icon,
                inf = "", type = None, use = None
            ):
            self.name = name
            self.val = val
            self.inf = inf
            self.icon = icon
            self.type = type
            self.use = use
