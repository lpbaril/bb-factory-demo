"""Tip calculator: python3 tip.py <amount> [percent] [--split N]"""
import sys

USAGE = "usage: tip.py <amount> [percent] [--split N]"


def tip(amount: float, percent: float) -> float:
    return amount * percent / 100


def main(argv: list[str]) -> int:
    args = argv[1:]
    people = 1
    if "--split" in args:
        i = args.index("--split")
        value = args[i + 1] if i + 1 < len(args) else None
        del args[i:i + 2]
        try:
            people = int(value) if value is not None else 0
        except ValueError:
            people = 0
        if people < 1:
            got = "nothing" if value is None else repr(value)
            print(f"error: --split needs a positive integer, got {got}", file=sys.stderr)
            return 1
    if not args:
        print(USAGE, file=sys.stderr)
        return 2
    amount = float(args[0])
    percent = float(args[1]) if len(args) > 1 else 15
    print(f"{tip(amount, percent) / people:.2f}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
