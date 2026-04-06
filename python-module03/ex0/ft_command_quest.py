import sys


def ft_command_quest() -> None:
    argc: int = len(sys.argv)
    i: int = 0
    print(f"Program name: {sys.argv[0]}")
    if argc == 1:
        print("No arguments provided!")
    elif argc > 1:
        print(f"Argument received: {argc - 1}")
        for arg in sys.argv[1:]:
            i += 1
            print(f"Argument {i}: {arg}")
    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    ft_command_quest()
