import sys


def ft_score_analytics() -> None:
    argc: int = len(sys.argv)
    if argc == 1:
        print(f"No scores provided. Usage: python3 {__name__} "
              "<score1> <score2> ...")
    elif argc > 1:
        try:
            score: list = []
            for arg in sys.argv[1:]:
                if arg 


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    ft_score_analytics()
