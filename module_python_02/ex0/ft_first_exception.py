def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    test_cases: list[str] = ["25", "abc"]

    for temp_str in test_cases:
        print(f"Input data is '{temp_str}'")
        try:
            temp: int = input_temperature(temp_str)
            print(f"Temperature is now {temp}°C")
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
