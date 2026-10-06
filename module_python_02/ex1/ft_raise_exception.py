def input_temperature(temp_str: str) -> int:
    temp: int = int(temp_str)
    if temp < 0:
        raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
    if temp > 40:
        raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    test_cases: list[str] = ["25", "abc", "100", "-50"]

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
