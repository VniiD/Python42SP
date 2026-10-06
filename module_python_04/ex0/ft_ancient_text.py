import sys
from typing import IO


def recover_ancient_text(filename: str) -> None:
    print(f"Accessing file '{filename}'")
    file_obj: IO[str] | None = None
    try:
        file_obj = open(filename, "r")
        content: str = file_obj.read()
        print(content, end="")
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")
    finally:
        if file_obj is not None:
            file_obj.close()
            print(f"File '{filename}' closed.")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return

    print("=== Cyber Archives Recovery ===")
    recover_ancient_text(sys.argv[1])


if __name__ == "__main__":
    main()
