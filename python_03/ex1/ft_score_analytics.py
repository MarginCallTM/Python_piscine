import sys


class Leaderbord:
    def __init__(self) -> None:
        self.scores = []

    def claims_args(self, argv) -> None:
        if len(sys.argv) == 1:
            print("No score provided. Usage: python3"
                  "ft_score_analytics.py <score1> <score2> ...")
            return
        for i in argv[1:]:
            self.add_score(i)

    def add_score(self, values):
        try:
            self.scores.append(int(values))
        except ValueError:
            print(f"{values} is not a valide score..")

    def get_status(self) -> None:
        if not self.scores:
            return
        print(f"Scores processed: {self.scores}")
        print(f"Total players: {len(self.scores)}")
        print(f"Total score: {sum(self.scores)}")
        print(f"Average score: {sum(self.scores) / len(self.scores):.2f}")
        print(f"High score: {max(self.scores)}")
        print(f"Low score: {min(self.scores)}")
        print(f"Score Range: {max(self.scores) - min(self.scores)}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")

    board = Leaderbord()

    board.claims_args(sys.argv)

    board.get_status()
