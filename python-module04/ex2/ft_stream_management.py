import sys


def ft_stream_management() -> None:
    sys.stdout.write("Input Stream active. Entre archivist ID: ")
    sys.stdout.flush()
    user_id: str = sys.stdin.readline().strip()
    sys.stdout.write("Input Stream. Enter status report: ")
    sys.stdout.flush()
    status: str = sys.stdin.readline().strip()
    sys.stdout.write(f"\n[STANDARD] Archive status from {user_id}: {status}\n")
    sys.stderr.write("[ALERT] System diagnostic: Communication channels"
                     " verified\n")
    sys.stdout.write("[STANDARD] Data  transmission complete\n\n")
    sys.stdout.write("Three-channel communication test succesful.\n")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    ft_stream_management()
