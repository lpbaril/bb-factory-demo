"""Tip calculator: python3 tip.py <amount> [percent]"""
import sys


def tip(amount: float, percent: float) -> float:
    return amount * percent / 100


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: tip.py <amount> [percent]", file=sys.stderr)
        return 2
    amount = float(argv[1])
    percent = float(argv[2]) if len(argv) > 2 else 15
    print(f"{tip(amount, percent):.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
