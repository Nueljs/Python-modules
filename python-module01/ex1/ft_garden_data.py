#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.plant_name: str = name
        self.plant_height: int = height
        self.plant_age: int = age


def ft_garden_data() -> None:
    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 80, 45)
    cactus = Plant("Cactus", 15, 120)
    garden = [rose, sunflower, cactus]
    for i in range(3):
        print(
            f"{garden[i].plant_name}: {garden[i].plant_height}cm, "
            f"{garden[i].plant_age} days old"
            )


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    ft_garden_data()
