from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (BattleStrategy, NormalStrategy, AggressiveStrategy,
                 DefensiveStrategy, InvalidStrategyError)


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    try:
        for i in range(len(opponents)):
            for j in range(i + 1, len(opponents)):
                factory_a, strategy_a = opponents[i]
                factory_b, strategy_b = opponents[j]
                a = factory_a.create_base()
                b = factory_b.create_base()
                print("\n* Battle *")
                print(a.describe())
                print(" vs.")
                print(b.describe())
                print(" now fight!")
                for line in strategy_a.act(a):
                    print(line)
                for line in strategy_b.act(b):
                    print(line)
    except InvalidStrategyError as e:
        print(f"Battle error, aborting tournament: {e}")


def main() -> None:
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()
    healing_factory = HealingCreatureFactory()
    transform_factory = TransformCreatureFactory()

    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Healing+Defensive) ]")
    opponents_0 = [(flame_factory, normal), (healing_factory, defensive)]
    battle(opponents_0)
    print("\nTournament 1 (error)")
    print(" [ (Flameling+Aggressive), (Healing+Defensive) ]")
    opponents_1 = [(flame_factory, aggressive), (healing_factory, defensive)]
    battle(opponents_1)
    print("\nTournament 2 (multiple)")
    print(" [ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    opponents_2 = [(aqua_factory, normal), (healing_factory, defensive),
                   (transform_factory, aggressive)]
    battle(opponents_2)


if __name__ == "__main__":
    main()
