#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int, rhythm: int) -> None:
        self.plant_name: str = name
        self.plant_height: int = height
        self.plant_age: int = age
        self.rhythm: int = rhythm

    def grow(self) -> None:
        self.plant_height += self.rhythm

    def age(self) -> None:
        self.plant_age += 1
        self.grow()

    def get_info(self) -> None: 
        print(
            f"{self.plant_name}: "
            f"{self.plant_height}cm, {self.plant_age} days old"
            )


def ft_plant_growth() -> None:
    rose = Plant("Rose", 25, 30, 10)
    sunflower = Plant("Sunflower", 80, 45, 7)
    cactus = Plant("Cactus", 15, 120, 1)
    garden: list = [rose, sunflower, cactus]
    for i in range(3):
        print("=== Day 1 ===")
        garden[i].get_info()
        for j in range(7):
            garden[i].age()
        print("=== Day 7 ===")
        garden[i].get_info()
        print(f"Growth this week: +{garden[i].rhythm * 7}cm")


if __name__ == "__main__":
    ft_plant_growth()
