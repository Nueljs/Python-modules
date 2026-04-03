import sys
import typing


def ft_stream_management() -> None:
    argc: int = len(sys.argv)
    if argc == 1:
        sys.stdout.write(f"Usage: {sys.argv[0]} <file>")
        return
    try:
        sys.stdout.write("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
        sys.stdout.write(f"Accesing file '{sys.argv[1]}'\n")
        sys.stdout.flush()
        file: typing.IO = open(sys.argv[1], 'r')
        file_list: list = [line.strip() for line in file]
        sys.stdout.write("---\n\n")
        for line in file_list:
            sys.stdout.write(line + "\n")
        print("\n---")
        sys.stdout.flush()
        file.close()
        sys.stdout.write(f"File '{sys.argv[1]}' closed.\n")
        sys.stdout.write("\nTransform data:\n")
        sys.stdout.write("---\n\n")
        for line in file_list:
            sys.stdout.write(line + "#\n")
        sys.stdout.write("\n---\n")
    except OSError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{sys.argv[1]}': {e}\n")
        sys.stderr.flush()
        return
    try:
        sys.stdout.write("Enter new file name (or empty): ")
        sys.stdout.flush()
        name: str = sys.stdin.readline().strip()
        if not name:
            sys.stdout.write("Not saving data\n")
            sys.stdout.flush()
            return
        else:
            sys.stdout.write(f"Saving data to '{name}'\n")
            sys.stdout.flush()
            file = open(name, 'w')
            for line in file_list:
                file.writelines(line + "#\n")
            sys.stdout.write(f"Data saved in file '{name}'.\n")
            sys.stdout.flush()
    except OSError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{name}': {e}\n")
        sys.stderr.flush()
        print("Data not saved.")


if __name__ == "__main__":
    ft_stream_management()
