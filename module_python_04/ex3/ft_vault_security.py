def secure_archive(
    filename: str, action: str = "read", content: str = ""
) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(filename, "r") as f:
                data: str = f.read()
            return True, data

        elif action == "write":
            with open(filename, "w") as f:
                f.write(content)
            return True, "Content successfully written to file"

        return False, f"Invalid action '{action}'"

    except Exception as e:
        return False, str(e)


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    res1: tuple[bool, str] = secure_archive("/not/existing/file", "read")
    print(res1)

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    res2: tuple[bool, str] = secure_archive("/etc/master.passwd", "read")
    print(res2)

    print("\nUsing 'secure_archive' to read from a regular file:")
    res3: tuple[bool, str] = secure_archive("ancient_fragment.txt", "read")
    print(res3)

    if res3[0]:
        print("\nUsing 'secure_archive' to write previous content to a file:")
        res4: tuple[bool, str] = secure_archive(
                                                "new_file.txt",
                                                "write",
                                                res3[1]
                                                )
        print(res4)


if __name__ == "__main__":
    main()
