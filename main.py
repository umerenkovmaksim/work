class Armor:
    def __init__(self, *armor):
        self.armor = dict(armor)

    def add(self, key):
        if key in self.armor:
            self.armor[key] += 1
        else:
            self.armor[key] = 1


class GhostInArmor(Armor):
    pass



ar = Armor(("helmet", 1), ("glove", 2))
ar.add("bib")
ar.add("bib")
print(ar.armor)
