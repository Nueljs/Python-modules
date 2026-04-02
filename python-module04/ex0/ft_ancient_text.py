def ft_ancient_text() -> None:
    try:
        print("Accesing Storage Vault: ancient_fragment.txt")
        with open('ancient_fragment.txt', "r") as vault:
            print("Connection established...\n")
            for content in vault:
                print(content, end="")
        print("\nData recovery complete. Storage unit disconnected")
    except FileNotFoundError:
        print("Error: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    ft_ancient_text()
