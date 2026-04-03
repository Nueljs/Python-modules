import sys
import typing


def ft_ancient_text() -> None:
    argc: int = len(sys.argv)
    if argc == 1:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    try:
        print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
        print(f"Accesing file: {sys.argv[1]}")
        file: typing.IO = open(sys.argv[1], 'r')
        print("---\n")
        print(file.read())
        print("\n---")
        file.close()
        print(f"File'{sys.argv[1]}' closed.")
    except OSError as e:
        print(f"Error opening file {sys.argv[1]}: {e}")


if __name__ == "__main__":
    ft_ancient_text()
