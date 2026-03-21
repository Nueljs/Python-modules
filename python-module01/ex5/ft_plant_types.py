#!/usr/bin/env/ python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self._age: int = age

    def show(self) -> None:
        type: str = self.__class__.__name__
        print(f"{self.name} ({type}): {self.height}cm, {self._age} days")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color
        self.is_blooming: bool = False

    def bloom(self) -> str:
        self.is_blooming = True
        return (f"{self.name} is blooming beautifully!")

    def show(self) -> None:
        if not self.is_blooming:
            print(f"{self.name}: {self.height:.1f}cm, {self._age} days old\n"
                  f"Color: {self.color}")
            print("Rose has not bloomed yet")
            print("[asking the rose to bloom]")
            self.bloom()
            self.show()
        elif self.is_blooming:
            print(f"{self.name}: {self.height:.1f}cm, {self._age} days old\n"
                  f"Color: {self.color}\n"
                  f"{self.name} is bloomign beautifully!")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self) -> str:
        return (f"[asking the {self.name} to produce shade]\n"
                f"{self.__class__.__name__} {self.name} now produces a shade"
                " of 200.0cm long and 5.0cm wide.\n")

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self._age} days old\n"
              f" Trunk diameter: {self.trunk_diameter:.1f}cm")
        print(self.produce_shade())


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: int) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: int = 0

    def age(self) -> None:
        pass

    def grow(self) -> None:
        pass

    def show(self) -> None:
        print(f"{super().show()}\n"
              f" Harvest season: {self.harvest_season}\n"
              f" Nutrtional value: {self.nutritional_value}"
              f"{self.name} is rich in {self.nutritional_value}")
        print(f"[make {self.name} grow and age for 20 days]")


def ft_plant_types() -> None:
    rose = Flower("Rose", 15, 10, "red")
    oak = Tree("Oak", 200, 365, 5)
    tomato = Vegetable("Tomato", 5, 10, "April", 0)
    plants: list = [rose, oak, tomato]
    for plant in plants:
        print(f"=== {plant.__class__.__name__}")
        plant.show()
        print("\n")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    ft_plant_types()
