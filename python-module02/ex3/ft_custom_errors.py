class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, name: str | None = None) -> None:
        if name:
            message: str = f"The {name} plant is wilting!"
        else:
            message = "Unknown plant error"
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Not enough water in the tank!") -> None:
        super().__init__(message)


def check_plant_health(leaf_color: str, name: str) -> None:
    if leaf_color == "yellow":
        raise (PlantError(name))


def check_water_tank(l_water: int) -> None:
    if l_water < 10:
        raise (WaterError())


def ft_custom_errors() -> None:
    try:
        print("Testing PlantError...")
        check_plant_health("yellow", "tomato")
    except PlantError as e:
        print(F"Caught {e.__class__.__name__}: {e}\n")
    try:
        print("Testing WaterError...")
        check_water_tank(5)
    except WaterError as e:
        print(f"Caught {e.__class__.__name__}: {e}\n")
    try:
        print("Testing catching all garden errors...")
        tests: list = [
            lambda: check_plant_health("yellow", "tomato"),
            lambda: check_water_tank(5)
        ]
        for test in tests:
            try:
                test()
            except GardenError as e:
                print(f"Caught GardenError; {e}")
    except GardenError as e:
        print(f"Caught {e.__class__.__name__}: {e}\n")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    ft_custom_errors()
    print("")
    print("All custom error types work correctly!")
