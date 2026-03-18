#!/urs/bin/env/ python3

class GardenManager:
    total_gardens: int = 0

    def __init__(self, owner: str) -> None:
        self.owner: str = owner
        self.plants: list = []
        GardenManager.total_gardens += 1

    @classmethod
    def create_garden_network(cls) -> list:
        return [cls("Alice"), cls("Bob")]

    def add_plant(self, plant: object) -> None:
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.set_height(plant._height + 1)
            print(f"{plant.name} grew 1cm")

    class GardenStats:
        @staticmethod
        def total_growth(plants: list) -> str:
            total_growth: int = 0
            for plant in plants:
                total_growth += plant._height
            return (f"Total growth: {total_growth}cm")

        @staticmethod
        def total_gardens() -> str:
            return (f"Total gardens managed: {GardenManager.total_gardens}")


class Plant:
    def __init__(self, name: str, height: int):
        self.name: str = name
        self.set_height(height)

    def set_height(self, value) -> None:
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = value


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color: str = color

    def bloom(self) -> str:
        return ("blooming")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, prize: int):
        super().__init__(name, height, color)
        self.prize: int = prize


def ft_garden_analytics() -> None:
    gardens_network: list = GardenManager.create_garden_network()
    alice: object = gardens_network[0]
    bob: object = gardens_network[1]
    rose: object = FloweringPlant("Rose", 26, "red")
    oak: object = Plant("Oak", 101)
    sunflower: object = PrizeFlower("Sunflower", 51, "yellow", 10)
    for owner in gardens_network:
        owner.add_plant()


if __name__ == "__main__":
    ft_garden_analytics()