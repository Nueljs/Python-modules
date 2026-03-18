#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name: str, height: int, age: int):
        self.name: str = name
        self._height: int = 0
        self._age: int = 0
        print(f"Plant created: {self.name}")
        self.set_height(height)
        self.set_age(age)

    def set_height(self, value) -> None:
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height: int = value
            print(f"Height updated: {value}cm [OK]")

    def set_age(self, value) -> None:
        if value < 0:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age: int = value
            print(f"Age updated: {value} days [OK]")

    def get_height(self) -> int:
        return (self._height)

    def get_age(self) -> int:
        return (self._age)


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 25, 30)
    rose.set_height(-5)
    print("\n")
    print(f"Current plant: {rose.name} ({rose.get_height()}cm, "
          f"{rose.get_age()} days)")


if __name__ == "__main__":
    ft_garden_security()
