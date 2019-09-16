init python:
    class spell:
        def __init__(self, name, inf, icon = "spells/empty.png",
                        hp = 0, mp = 0, stm = 0,
                        mpc = 0, stmc = 0,
                        effect = None, pdbm = [0,0,0,0],
                        pwr = 0, agl = 0, dur = 0
                        ):
            self.name = name
            self.inf = inf
            self.icon = icon

            self.dur = dur

            self.hp = hp
            self.mp = mp
            self.stm = stm

            self.pwr = pwr
            self.agl = agl

            self.mpc = mpc # Mana cost
            self.stmc = stmc # stamina cost

            self.effect = effect
            self.pdbm = pdbm # [parry, dodge, block, miss]
