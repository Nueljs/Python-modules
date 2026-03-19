#!/urs/bin/env/ python3

class GardenManager:
    total_gardens: int = 0

    def __init__(self, owner: str) -> None:
        self.owner: str = owner
        self.plants: list = []
        self.total_growth: int = 0
        self.total_plants: int = 0
        GardenManager.total_gardens += 1

    @classmethod
    def create_garden_network(cls) -> list:
        return [cls("Alice"), cls("Bob")]

    def add_plant(self, plant: object) -> None:
        self.plants.append(plant)
        self.total_plants += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            self.total_growth += 1
            plant.set_height(plant._height + 1)
            print(f"{plant.name} grew 1cm")

    def get_info(self) -> str:
        return (f"{self.GardenStats.plants_added(self.total_plants)}, "
                f"{self.GardenStats.total_growth(self.total_growth)}"
                f"\n{self.GardenStats.total_types(self.plants)}")

    class GardenStats:
        @staticmethod
        def plants_added(value: int) -> str:
            return (f"Plants added: {value}")

        @staticmethod
        def total_growth(value: int) -> str:
            return (f"Total growth: {value}cm")

        @staticmethod
        def total_gardens() -> str:
            return (f"Total gardens managed: {GardenManager.total_gardens}")
        
        @staticmethod
        def total_types(plants: list) -> str:
            reg, flow, priz = 0, 0, 0
            for plant in plants:
                if plant.__class__.__name__ == "PrizeFlower":
                    priz += 1
                elif plant.__class__.__name__ == "FloweringPlant":
                    flow += 1
                elif plant.__class__.__name__ == "Plant":
                    reg += 1
            return (f"Plant typpes: {reg} regular, {flow} flowering, {priz}"
                    " prize flowers")


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

    def get_info(self) -> str:
        return (f"{self.name}: {self._height}cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color: str = color

    def bloom(self) -> str:
        return ("blooming")

    def get_info(self) -> str:
        super_info: str = super().get_info()
        return (f"{super_info}, {self.color} flowers ({self.bloom()})")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, prize: int):
        super().__init__(name, height, color)
        self.prize: int = prize

    def get_info(self) -> str:
        super_info: str = super().get_info()
        return (f"{super_info}, Prize points: {self.prize}")


def ft_garden_analytics() -> None:
    gardens_network: list = GardenManager.create_garden_network()
    rose: object = FloweringPlant("Rose", 25, "red")
    oak: object = Plant("Oak Tree", 100)
    sunflower: object = PrizeFlower("Sunflower", 50, "yellow", 10)
    gardens_network[0].add_plant(oak)
    gardens_network[0].add_plant(rose)
    gardens_network[0].add_plant(sunflower)
    print("\n")
    gardens_network[0].grow_all()
    print(f"\n==={gardens_network[0].owner}'s Garden Report ===\n"
          "Plants in garden:")
    for plant in gardens_network[0].plants:
        print(f"- {plant.get_info()}")
    print(f"\n{gardens_network[0].get_info()}")
    print(f"Total garden managed: {GardenManager.total_gardens}")


if __name__ == "__main__":
    print("=== Garden Mangement System Demo ===\n")
    ft_garden_analytics()
