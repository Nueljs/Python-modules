#!/usr/bin/env python3

class SecurePlant:
    def __init__(self, name: str, height: float, age: int):
        self.name: str = name
        self._height: float = 0
        self._age: int = 0
        self.set_height(height)
        self.set_age(age)
        print(f"Plant created: {self.name}: {self._height:.1f}cm, {self._age}"
              f" days old\n")

    def set_height(self, value) -> None:
        if value < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            if not self._height:
                self._height = value
            else:
                print(f"Height updated: {value}cm")
                self._height = value

    def set_age(self, value) -> None:
        if value < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            if not self._age:
                self._age = value
            else:
                print(f"Age updated: {value} days")
                self._age = value

    def get_height(self) -> float:
        return (self._height)

    def get_age(self) -> int:
        return (self._age)


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 15, 10)
    rose.set_height(25)
    rose.set_age(30)
    print("\n")
    rose.set_height(-3)
    rose.set_age(-19)
    print("\n")
    print(f"Current state: {rose.name}: {rose.get_height():.1f}cm, "
          f"{rose.get_age()} days old")


if __name__ == "__main__":
    ft_garden_security()
