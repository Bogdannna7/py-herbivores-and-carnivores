from __future__ import annotations


class Animal:

    alive = []

    def __init__(self, name: str, health: int = 100,
                 hidden: bool = False) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        if self.health > 0:
            if self not in Animal.alive:
                Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: {self.health}, "
                f"Hidden: {self.hidden}}}")


class Herbivore(Animal):

    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):

    @staticmethod
    def bite(herbivore: Herbivore) -> None:
        if isinstance(herbivore, Herbivore):
            if herbivore.hidden is False:
                herbivore.health -= 50
            if herbivore.health <= 0:
                Animal.alive.remove(herbivore)


lion = Carnivore("King Lion")
pantera = Carnivore("Bagira")
rabbit = Herbivore("Susan")
print(Animal.alive)
# output = "[{Name: King Lion, Health: 100, Hidden: False}, " \
#          "{Name: Bagira, Health: 100, Hidden: False}, " \
#          "{Name: Susan, Health: 100, Hidden: False}]\n"
