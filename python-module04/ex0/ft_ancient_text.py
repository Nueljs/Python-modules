def ft_ancient_text() -> None:
    try:
        with open('./anciente_fragment.txt', "r") as vault:
            content = vault.read()
    except FileNotFoundError as e:
        print(e)


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    ft_ancient_text()
