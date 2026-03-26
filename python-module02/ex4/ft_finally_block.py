class PlantError(Exception):
    def __init__(self, name: str) -> None:
        super().__init__(f"Invalid plant name to water: '{name}'")


def water_plant(plant_name: str) -> None:
    if plant_name == str.capitalize(plant_name):
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(plant_name)


def test_watering_system() -> None:
    valid_plants: list = [
        "Tomato",
        "Lettuce",
        "Carrots"
    ]
    invalid_plants: list = [
        "Tomato",
        "lettuce"
    ]
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        for plant in valid_plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
    finally:
        print("Closing watering system")
    print("")
    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        for plant in invalid_plants:
            water_plant(plant)
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
    finally:
        print(".. ending tests and returning to main")
        print("Closing watering system")
    print("")
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    print("=== Garden Watering System ===\n")
    test_watering_system()
