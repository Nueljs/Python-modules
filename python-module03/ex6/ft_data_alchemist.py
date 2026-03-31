import random


def ft_data_alchemist() -> None:
    initial_names: list = [
        'Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kebin',
        'Liam'
        ]
    names_capitalized: list = [name.capitalize() for name in initial_names]
    alredy_capitalized: list = [name for name in initial_names
                                if name == name.capitalize()]
    print(f"Initial list of players {initial_names}")
    print(f"New list with all names capitalized: {names_capitalized}")
    print(f"New list of capitalized names only: {alredy_capitalized}")
    print("")
    score_dict: dict = {name: random.randint(1, 1000)
                        for name in names_capitalized}
    print(f"Score dict: {score_dict}")
    avg_score: float = sum(score_dict.values())/len(score_dict)
    print(f"Score average is {(avg_score):.2f}")
    high_score: dict = {name: score_dict[name] for name in score_dict.keys()
                        if score_dict[name] > avg_score}
    print(f"High scores: {high_score}")


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    ft_data_alchemist()
