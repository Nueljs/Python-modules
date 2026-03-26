import sys


def ft_score_analytics() -> None:
    argc: int = len(sys.argv)
    if argc == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
    elif argc > 1:
        score: list = []
        for arg in sys.argv[1:]:
            try:
                score.append(int(arg))
            except ValueError:
                print(f"Invalid parameter: '{arg}'")
        if not score:
            print("No scores provided. Usage: python3 ft_score_analytics.py "
                  "<score1> <score2> ...")
            return
        print(f"Scores processed: {score}")
        print(f"Total player: {len(score)}")
        print(f"Total score: {sum(score)}")
        print(f"Average score: {sum(score)/len(score):.1f}")
        print(f"High score: {max(score)}")
        print(f"Low score: {min(score)}")
        print(f"Score range: {max(score) - min(score)}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    ft_score_analytics()
