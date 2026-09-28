from ex0 import CreatureFactory, FlameFactory, AquaFactory


def test_battle(factory0: CreatureFactory, factory1: CreatureFactory) -> None:
    base_0 = factory0.create_base()
    base_1 = factory1.create_base()
    print(base_0.describe())
    print(" vs.")
    print(base_1.describe())
    print(" fight!")
    print(base_0.attack())
    print(base_1.attack())


def test_factory(factory: CreatureFactory) -> None:
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def main() -> None:
    print("Testing factory")
    flame = FlameFactory()
    test_factory(flame)
    print("\nTesting factory")
    aqua = AquaFactory()
    test_factory(aqua)
    print("\nTesting battle")
    test_battle(flame, aqua)


if __name__ == "__main__":
    main()
