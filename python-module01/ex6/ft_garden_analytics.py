#!/urs/bin/env/ python3

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

    @classmethod
    def create_anonymous(cls) -> object:
        return (cls("Unknown", 0))

    @staticmethod
    def check_age(age: int) -> bool:
        if age > 365:
            return (True)
        else:
            return (False)

    class Stats:
        def __init__(self, name: str, height: int):
            super().__init__(name, height)
            self._grow_count: int = 0
            self._age_count: int = 0
            self._show_count: int = 0


class Flower(Plant):
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color: str = color

    def bloom(self) -> str:
        return ("blooming")

    def get_info(self) -> str:
        super_info: str = super().get_info()
        return (f"{super_info}, {self.color} flowers ({self.bloom()})")


class Seed(Flower):
    def __init__(self, name: str, height: int, color: str, seed_n: int):
        super().__init__(name, height, color)
        self.seed_n: int = seed_n

    def get_info(self) -> str:
        super_info: str = super().get_info()
        return (f"{super_info}, Prize points: {self.prize}")


def ft_garden_analytics() -> None:
    pass


if __name__ == "__main__":
    print("=== Garden Mangement System Demo ===\n")
    ft_garden_analytics()
