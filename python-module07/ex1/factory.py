from ex0 import CreatureFactory, Creature
from .creature import Sproutling, Bloomelle, Shiftling, Morphagon

class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        