#!/usr/bin/env/ python3

class Plant:
    def __init__(self, name: str, starting_height: float,
                 starting_age: int) -> None:
        self.name: str = name
        self.starting_height: float = starting_height
        self.starting_age: int = starting_age

    def get_info(self) -> str:
        return (f"{self.name}: {round(self.starting_height):.1f}cm,"
                f" {self.starting_age} days old")


def ft_plant_factory() -> None:
    plants_data: list = [
        ["Rose", 25, 30],
        ["Oak", 200, 365],
        ["Cactus", 5, 90],
        ["Sunflower", 80, 45],
        ["Fern", 15, 120]
    ]
    garden: list = []
    for plant in plants_data:
        garden.append(Plant(*plant))
    for plant in garden:
        print(f"Created: {plant.get_info()}")


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    ft_plant_factory()
