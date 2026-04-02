def ft_archive_creation() -> None:
    try:
        print("Initializing new storage unit: new_discovery.txt")
        with open('new_discovery.txt', 'w') as my_file:
            text: list = [
                "[ENTRY 001] New quantum algorithm discovered",
                "[ENTRY 002] Efficiency increased by 347%",
                "[ENTRY 003] Archived by Data Archivist trainee"
            ]
            print("Storage unit created succesfully...\n")
            print("Inscribing preservation data...")
            for line in text:
                my_file.write(line + "\n")
                print(line)
        print("\nData inscription complete. Storage unit sealed.")
        print("Archive 'new_discovery.txt' ready for long-term preservation.")
    except OSError as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    ft_archive_creation()
