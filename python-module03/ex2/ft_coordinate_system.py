import math


def get_player_pos() -> None:
    new_input: str = input("Enter new coordinates as floats in format:"
                           "'x,y,z': ")
    coordinates: list = [float(n) for n in new_input.split(",")]
    final_coor: tuple = tuple(coordinates)

def ft_coordinate_system() -> None:
    get_player_pos()


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    ft_coordinate_system()
