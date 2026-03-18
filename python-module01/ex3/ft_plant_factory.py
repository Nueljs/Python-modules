#!/usr/bin/env/ python3

class Plant:
    def __init__(self, name: str, starting_height: int,
                 starting_age: int) -> None:
        self.name: str = name
        self.starting_height: int = starting_height
        self.starting_age: int = starting_age

    def get_info(self) -> str:
        return (f"{self.name} ({self.starting_height}cm,"
                f" {self.starting_age} days)")


def ft_plant_factory() -> None:
    plants_data: list = [
        ["Rose", 25, 30],
        ["Oak", 200, 365],
        ["Cactus", 5, 90],
        ["Sunflower", 280, 45],
        ["Fern", 15, 120]
    ]
    garden: list = []
    for i in range(5):
        garden.append(Plant(*plants_data[i]))
    for i in range(5):
        print(f"Created: {garden[i].get_info()}")
    print("\n")
    print(f"Total plants created: {i + 1}")


if __name__ == "__main__":
    ft_plant_factory()
