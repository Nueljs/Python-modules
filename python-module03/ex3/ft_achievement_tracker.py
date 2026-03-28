import random


def gen_player_achievements() -> set:
    achievements: list = [
        'Crafting Genious', 'World Savior', 'Master Explorer',
        'Collector Supreme', 'Untouchable', 'Boss Slayer', 'Strategist',
        'Speed Runner', 'Survivor', 'Treasure Hunter', 'Unstoppable',
        'Hidden Path Finder', 'First Steps', 'Sharp Mind']
    num_of_achivements: int = random.randint(1, len(achievements))
    player_achiev: list = random.sample(achievements, num_of_achivements)
    return (set(player_achiev))


def ft_achievements_tracker() -> None:
    Alice: set = gen_player_achievements()
    Bob: set = gen_player_achievements()
    Charlie: set = gen_player_achievements()
    Dylan: set = gen_player_achievements()
    total_achievements: set = {
        'Crafting Genious', 'World Savior', 'Master Explorer',
        'Collector Supreme', 'Untouchable', 'Boss Slayer', 'Strategist',
        'Speed Runner', 'Survivor', 'Treasure Hunter', 'Unstoppable',
        'Hidden Path Finder', 'First Steps', 'Sharp Mind'
    }
    print(f"Player Alice: {Alice}")
    print(f"Player Bob: {Bob}")
    print(f"Player Charlie: {Charlie}")
    print(f"Player Dylan: {Dylan}\n")
    print("Common achievements: "
          f"{set.intersection(Alice, Bob, Charlie, Dylan)}\n")
    print(f"Only Alice has: {Alice.difference(Bob, Charlie, Dylan)}")
    print(f"Only Bob has: {Bob.difference(Alice, Charlie, Dylan)}")
    print(f"Only Charlie has: {Charlie.difference(Bob, Alice, Dylan)}")
    print(f"Only Dylan has: {Dylan.difference(Bob, Charlie, Alice)}\n")
    print(f"Alice is missing: {total_achievements.difference(Alice)}")
    print(f"Bob is missing: {total_achievements.difference(Bob)}")
    print(f"Charlie is missing: {total_achievements.difference(Charlie)}")
    print(f"Dylan is missing: {total_achievements.difference(Dylan)}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    ft_achievements_tracker()
