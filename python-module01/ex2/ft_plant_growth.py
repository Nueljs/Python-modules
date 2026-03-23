#!/usr/bin/env python3

class Plant:
    total_growth: float = 0

    def __init__(self, name: str, height: float, age: int,
                 rhythm: float) -> None:
        self.plant_name: str = name
        self.plant_height: float = height
        self.plant_age: int = age
        self.rhythm: float = rhythm

    def grow(self) -> None:
        self.plant_height += self.rhythm

    def age(self) -> None:
        self.plant_age += 1
        self.grow()

    def get_info(self) -> None:
        print(
            f"{self.plant_name}: "
            f"{round(self.plant_height, 2):.1f}cm, {self.plant_age} days old"
            )


def ft_plant_growth() -> None:
    rose = Plant("Rose", 25, 30, 0.8)
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.get_info()
        rose.age()

    print(f"Growth this week: {round(rose.rhythm * 7)}cm")


if __name__ == "__main__":
    print("=== Garden Plant Growth ===")
    ft_plant_growth()
