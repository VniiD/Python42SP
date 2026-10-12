import importlib.util
from typing import List, Tuple


def check_reagents() -> None:
    reagents: List[Tuple[str, str]] = [
        ("pandas", "Data manipulation ready"),
        ("numpy", "Numerical computation ready"),
    ]
    print("REAGENT STATUS: Loading reagents...")
    print("Checking dependencies:")

    missing: bool = False
    status_messages: List[str] = []

    for name, message in reagents:
        spec = importlib.util.find_spec(name)
        if spec is not None:
            mod = __import__(name)
            version: str = getattr(mod, "__version__", "unknown")
            print(f"[OK] {name} ({version})")
            status_messages.append(message)
        else:
            print(f"[MISSING] {name}")
            missing = True

    if missing:
        print("\nWARNING: Reagents are missing!")
        print("Install via pip:")
        print("pip install -r ex0/requirements.txt")
        print("Install via Poetry:")
        print("poetry install")
    else:
        print("\npip vs Poetry:")
        for msg in status_messages:
            print(msg)
        print("requirements.txt declares what to install; pip resolves it.")
        print("pyproject.toml declares constraints, Poetry pins versions.")
        print("All reagents present and accounted for.")


if __name__ == "__main__":
    check_reagents()
