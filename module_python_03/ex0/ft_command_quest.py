import sys


def main() -> None:
    args: list[str] = sys.argv
    total_args: int = len(args)
    """ x: int = 10, type hint """
    print("Commmand Quest ===")
    print(f"Program name: {args[0]}")
    if total_args == 1:
        print("No argumments provided!")
    else:
        print(f"argumments received: {total_args - 1}")
        for i in range(1, total_args):
            print(f"Arguments {i}: {args[i]}")
    print(f"Total argumments: {total_args}")


if __name__ == "__main__":
    main()
