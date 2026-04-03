import sys
import typing


def ft_archive_creation() -> None:
    argc: int = len(sys.argv)
    if argc == 1:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    try:
        print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
        print(f"Accesing file: {sys.argv[1]}")
        file: typing.IO = open(sys.argv[1], 'r')
        file_list: list = [line.strip() for line in file]
        print("---\n")
        print(file.read())
        print("\n---")
        file.close()
        print(f"File'{sys.argv[1]}' closed.")
        print("\nTransform data:")
        print("---\n")
        for line in file_list:
            print(line + "#")
        print("\n---")
        name: str = input("Enter new file name (or empty): ")
        if not name:
            print("Not saving data")
            return
        else:
            print(f"Saving data to '{name}'")
            file = open(name, 'w')
            for line in file_list:
                file.writelines(line + "#\n")
            print(f"Data saved in file '{name}'.")
    except OSError as e:
        print(f"Error opening file {sys.argv[1]}: {e}")


if __name__ == "__main__":
    ft_archive_creation()
