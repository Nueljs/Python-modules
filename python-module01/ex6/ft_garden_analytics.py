#!/usr/bin/env/ python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name
        self.height: float = height
        self._age: int = age
        self.stats: Plant.Stats = self.Stats()

    def grow(self, value: float = 0.8) -> None:
        self.height += value
        self.stats.count_grow += 1

    def age(self, value: int) -> None:
        self._age += value
        self.stats.count_age += 1

    def show(self) -> None:
        self.stats.count_show += 1
        print(f"{self.name}: {self.height:.1f}cm, {self._age} days old")

    @staticmethod
    def check_age(age: int) -> None:
        if age < 365:
            print(f"Is {age} days more than a year? -> False")
        else:
            print(f"Is {age} days more than a year? -> True")

    @classmethod
    def create_one(cls) -> 'Plant':
        return (cls("Unknown plant", 0.0, 0))

    class Stats:
        def __init__(self):
            self.count_grow = 0
            self.count_age = 0
            self.count_show = 0
            self.count_shade = 0

        def show_stats(self) -> None:
            print(f"Stats: {self.count_grow} grow, {self.count_age} age,"
                  f" {self.count_show} show")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self.is_blooming: bool = False

    def bloom(self) -> None:
        self.is_blooming = True

    def show(self) -> None:
        if not self.is_blooming:
            super().show()
            print(f" Color: {self.color}")
            print(f" {self.name} has not bloomed yet")
        elif self.is_blooming:
            super().show()
            print(f" Color: {self.color}\n"
                  f" {self.name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter
        self.stats: Tree.TreeStats = self.TreeStats()

    def produce_shade(self) -> None:
        self.stats.count_shade += 1
        print(f"{self.__class__.__name__} {self.name} now produces a shade"
              " of 200.0cm long and 5.0cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")

    class TreeStats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self.count_shade = 0

        def show_stats(self) -> None:
            super().show_stats()
            print(f" {self.count_shade} shade")


class Seed(Flower):
    def __init__(self, name: str, height: int, age: int, color: str,
                 seeds: int) -> None:
        super().__init__(name, height, age, color)
        self.seeds: float = seeds

    def grow_and_age_and_bloom(self, days: int) -> None:
        self.grow(30.0)
        print(f"[make {self.name} grow, age and bloom]")
        self.age(days)
        self.bloom()

    def show(self) -> None:
        super().show()
        if self.is_blooming:
            print(f" Seeds: {self.seeds}")
        else:
            print(" Seeds: 0")


def display_plant_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    plant.stats.show_stats()


def ft_garden_analytics() -> None:
    rose = Flower("Rose", 15, 10, "red")
    oak = Tree("Oak", 200, 365, 5)
    sunflower = Seed("Sunflower", 80, 45, "yellow", 42)
    unknown = Plant.create_one()
    print("=== Check year-old")
    Plant.check_age(30)
    Plant.check_age(400)
    print("")
    print(f"=== {rose.__class__.__name__}")
    rose.show()
    display_plant_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_plant_stats(rose)
    print(f"\n=== {oak.__class__.__name__}")
    oak.show()
    display_plant_stats(oak)
    print(f"[asking the {oak.name} to produce shade]")
    oak.produce_shade()
    display_plant_stats(oak)
    print(f"\n=== {sunflower.__class__.__name__}")
    sunflower.show()
    sunflower.grow_and_age_and_bloom(20)
    sunflower.show()
    display_plant_stats(sunflower)
    print("")
    print("=== Anonymous")
    unknown.show()
    display_plant_stats(unknown)


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    ft_garden_analytics()
