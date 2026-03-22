#!/usr/bin/env/ python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self._age: int = age

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self._age} days old")


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
            print(" Rose has not bloomed yet")
        elif self.is_blooming:
            super().show()
            print(f" Color: {self.color}\n"
                  f" {self.name} is bloomign beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self) -> None:
        print(f"{self.__class__.__name__} {self.name} now produces a shade"
              " of 200.0cm long and 5.0cm wide.")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: int = nutritional_value

    def grow_and_age(self, days: int) -> None:
        print(f"[make {self.name} grow and age for {days} days]")
        for _ in range(days):
            self._age += 1
            self.height += 2.1
            self.nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")


def ft_plant_types() -> None:
    rose = Flower("Rose", 15, 10, "red")
    oak = Tree("Oak", 200, 365, 5)
    tomato = Vegetable("Tomato", 5, 10, "April", 0)
    print(f"=== {rose.__class__.__name__}")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print(f"\n=== {oak.__class__.__name__}")
    oak.show()
    print(f"[asking the {oak.name} to produce shade]")
    oak.produce_shade()
    print(f"\n=== {tomato.__class__.__name__}")
    tomato.show()
    tomato.grow_and_age(20)
    tomato.show()


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    ft_plant_types()
