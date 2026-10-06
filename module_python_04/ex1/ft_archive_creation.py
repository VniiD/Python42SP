import sys
from typing import IO


def read_file(filename: str) -> str | None:
    print(f"Accessing file '{filename}'")
    file_obj: IO[str] | None = None
    try:
        file_obj = open(filename, "r")
        content: str = file_obj.read()
        print(content, end="")
        return content
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")
        return None
    finally:
        if file_obj is not None:
            file_obj.close()
            print(f"File '{filename}' closed.")


def save_file(new_filename: str, content: str) -> None:
    print(f"Saving data to '{new_filename}'")
    file_obj: IO[str] | None = None
    try:
        file_obj = open(new_filename, "w")
        file_obj.write(content)
        print(f"Data saved in file '{new_filename}'.")
    except Exception as e:
        print(f"Error saving file '{new_filename}': {e}")
    finally:
        if file_obj is not None:
            file_obj.close()


def transform_content(content: str) -> str:
    lines: list[str] = content.splitlines()
    transformed_lines: list[str] = [f"{line}#" for line in lines]
    return "\n".join(transformed_lines) + "\n"


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    print("=== Cyber Archives Recovery & Preservation ===")
    content: str | None = read_file(sys.argv[1])

    if content is None:
        return

    print("\nTransform data:")
    transformed: str = transform_content(content)
    print(transformed, end="")

    new_filename: str = input("Enter new file name (or empty): ").strip()

    if new_filename:
        save_file(new_filename, transformed)
    else:
        print("Not saving data.")


if __name__ == "__main__":
    main()
