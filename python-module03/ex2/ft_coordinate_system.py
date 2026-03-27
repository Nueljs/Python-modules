import math


def get_player_pos() -> tuple:
    new_input: str = input("Enter new coordinates as floats in format:"
                           "'x,y,z': ")
    try:
        coordinates: list = new_input.split(",")
        x: str = coordinates[0]
        y: str = coordinates[1]
        z: str = coordinates[2]
        current: str = x
        xf: float = float(x)
        current = y
        yf: float = float(y)
        current = z
        zf: float = float(z)
        final_coor: tuple = (xf, yf, zf)
    except IndexError:
        print("Invalid syntax")
        return get_player_pos()
    except ValueError as e:
        print(f"Error on parameter '{current}': {e}")
        return get_player_pos()
    return (final_coor)


def ft_coordinate_system() -> None:
    first_tuple: tuple = get_player_pos()
    x1: float = first_tuple[0]
    y1: float = first_tuple[1]
    z1: float = first_tuple[2]
    print(f"Got a first tuple: ({x1}, {y1}, {z1})")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    distance_center: float = math.sqrt((0-x1) ** 2 + (0-y1) ** 2 + (0-z1) ** 2)
    print(f"Distance to center: {distance_center:.4f}\n")
    print("Get a second coordinates")
    second_tuple: tuple = get_player_pos()
    x2: float = second_tuple[0]
    y2: float = second_tuple[1]
    z2: float = second_tuple[2]
    distance_points: float = math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2 +
                                       (z2-z1) ** 2)
    print(f"Distance between the 2 sets of coordinates: {distance_points:.4f}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    ft_coordinate_system()
