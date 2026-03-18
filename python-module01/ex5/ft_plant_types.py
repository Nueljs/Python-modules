#!/usr/bin/env/ python3

class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def get_info(self) -> str:
        type: str = self.__class__.__name__
        return (f"{self.name} ({type}): {self.height}cm, {self.age} days")


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> str:
        return (f"{self.name} is blooming beautifully!")

    def get_info(self) -> str:
        return (f"{super().get_info()}, {self.color} color \n"
                f"{self.bloom()}")


class Tree(Plant):
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self) -> str:
        return (f"{self.name} provide 78 square meters of shade")

    def get_info(self) -> str:
        return (f"{super().get_info()} {self.trunk_diameter}cm diameter \n"
                f"{self.produce_shade()}")


class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str,
                 nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value

    def get_info(self) -> str:
        return (f"{super().get_info()}, {self.harvest_season} harvest \n"
                f"{self.name} is rich in {self.nutritional_value}")


def ft_plant_types() -> None:
    rose = Flower("Rose", 25, 30, "red")
    daisy = Flower("Daisy", 18, 15, "white")
    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 700, 1345, 48)
    tomato = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    carrot = Vegetable("Carrot", 45, 60, "autum", "vitamin K")
    plants: list = [rose, daisy, oak, pine, tomato, carrot]
    for i in range(6):
        print(f"{plants[i].get_info()} \n")


if __name__ == "__main__":
    print(" === Garden Plant Types === \n")
    ft_plant_types()
