# init python:
#     class equip:
#         def __init__(self, cloths, dir):
#             self.dir = dir
#             self.cloths = cloths

#         # Equip
#         def equip(self, x):
#             if self.remove_from(x, 1, s):
#                 self.equipped[self.equipslot] = x

#         def unequip(self, x, s, t):
#             if self.equipped[s] is not None:
#                 self.add_to(self.equipped[s], 1, x)
#                 self.equipped[s] = None
#             self.equiptype = t
#             self.equipslot = s
