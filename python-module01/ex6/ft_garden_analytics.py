#!/urs/bin/env/ python3

class GardenManager:
    def __init__(self, owner: str) -> None:
        self.owner: str = owner
        self.plants: list = []

    @classmethod
    def create_garden_network(cls) -> list:
        return [cls("Alice"), cls("Robert")]
    
    @staticmethod
    def add_plant(Plant: object) -> None:
        plants[0] = 

    class GardenStats:
        @staticmethod
        def total_growth(plants: list) -> str:
            total_growth: int = 0
            for plant in plants:
                total_growth += plant.height
            return (f"Total growth: {total_growth}cm")


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
