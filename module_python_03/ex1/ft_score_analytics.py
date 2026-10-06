import sys


def process_score(raw_args: list[str]) -> list[int]:
    valid_scores: list[int] = []
    for arg in raw_args:
        try:
            score: int = int(arg)
            valid_scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    return valid_scores


def print_analytics(scores: list[int]) -> None:
    total_players: int = len(scores)
    total_scores: int = sum(scores)
    avg_score: float = total_scores / total_players
    high_score: int = max(scores)
    low_score: int = min(scores)
    score_range: int = high_score - low_score

    print(f"Scores processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_scores}")
    print(f"Average score: {avg_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")


def main() -> None:
    print("=== Player Score Analytics ===")
    raw_args: list[str] = sys.argv[1:]

    if not raw_args:
        print("No scores provided. ft_score_anallytics.py <score1> ...")
        return

    scores: list[int] = process_score(raw_args)

    if not scores:
        print("No scores provided. ft_score_anallytics.py <score1> ...")
        return

    print_analytics(scores)


if __name__ == "__main__":
    main()
