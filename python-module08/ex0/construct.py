import sys
import os
import site


def is_virtual_env() -> bool:
    return sys.prefix != sys.base_prefix


if __name__ == "__main__":
    if is_virtual_env():
        print()
        print("MATRIX STATUS: Welcome to the construct")
        print()

        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Enviroment Path: {sys.prefix}")

        path: list[str] = site.getsitepackages()
        print("Package installation path:")
        print(path[0])
    else:
        print()
        print("MATRIX STATUS: You're still plugged in")
        print()

        print(f"Current Python: {sys.executable}")
        print("Virtual Enviroment: None detected")
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate  # On Windows")
        print()
        print("Then run this program again.")
