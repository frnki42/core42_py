from ex0 import CreatureFactory
from .creature import (HealingCreature, TransformingCreature, Sproutling,
                       Bloomelle, Shiftling, Morphagon)


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> HealingCreature:
        return Sproutling()

    def create_evolved(self) -> HealingCreature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> TransformingCreature:
        return Shiftling()

    def create_evolved(self) -> TransformingCreature:
        return Morphagon()
