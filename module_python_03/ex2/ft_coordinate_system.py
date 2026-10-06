import math


def parse_coordinates(raw_input: str) -> tuple[float, float, float]:
    parts: list[str] = raw_input.split(",")
    if len(parts) != 3:
        raise ValueError("Invalid syntax")
    try:
        x: float = float(parts[0].strip())
        y: float = float(parts[1].strip())
        z: float = float(parts[2].strip())
        return (x, y, z)
    except ValueError:
        invalid_val: str = ""
        for part in parts:
            clean_part: str = part.strip()
            try:
                float(clean_part)
            except ValueError:
                invalid_val = clean_part
                break
        raise ValueError(
            f"Error on parameter '{invalid_val}': "
            f"could not convert string to float: '{invalid_val}'"
        )


def get_player_pos() -> tuple[float, float, float]:
    while True:
        try:
            prompt: str = "Enter new coordinates 'x, y, z': "
            user_input: str = input(prompt)
            return parse_coordinates(user_input)
        except ValueError as e:
            print(e)


def calculate_distance(
    pos1: tuple[float, float, float],
    pos2: tuple[float, float, float]
) -> float:
    dx: float = pos2[0] - pos1[0]
    dy: float = pos2[1] - pos1[1]
    dz: float = pos2[2] - pos1[2]
    return math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)


def main() -> None:
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    pos1: tuple[float, float, float] = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

    origin: tuple[float, float, float] = (0.0, 0.0, 0.0)
    dist_origin: float = calculate_distance(origin, pos1)
    print(f"Distance to center: {round(dist_origin, 4)}")

    print("Get a second set of coordinates")
    pos2: tuple[float, float, float] = get_player_pos()
    dist_between: float = calculate_distance(pos1, pos2)
    print(f"Distance the 2 sets of coordinates: {round(dist_between, 4)}")


if __name__ == "__main__":
    main()
