import importlib.util
import sys
from typing import Any


def check_dependency(package_name: str) -> bool:
    spec = importlib.util.find_spec(package_name)
    return spec is not None


def get_package_version(package_name: str) -> str:
    try:
        module: Any = __import__(package_name)
        return getattr(module, "__version__", "unknown")
    except ImportError:
        return "not installed"


def verify_environment() -> bool:
    required_packages: list[tuple[str, str]] = [
        ("pandas", "Data manipulation ready"),
        ("numpy", "Numerical computation ready"),
        ("matplotlib", "Visualization ready"),
    ]

    all_present: bool = True
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    for pkg, purpose in required_packages:
        if check_dependency(pkg):
            version: str = get_package_version(pkg)
            print(f"[OK] {pkg} ({version})")
            print(f"     {purpose}")
        else:
            print(f"[MISSING] {pkg}")
            all_present = False

    return all_present


def run_analysis() -> None:
    import matplotlib.pyplot as plt  # type: ignore
    import numpy as np  # type: ignore
    import pandas as pd  # type: ignore

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    data_points: int = 1000
    signal: Any = np.random.normal(loc=0.0, scale=1.0, size=data_points)
    noise: Any = np.random.uniform(low=-0.5, high=0.5, size=data_points)
    matrix_stream: Any = np.cumsum(signal + noise)

    df: Any = pd.DataFrame({
        "time_step": np.arange(data_points),
        "stream_value": matrix_stream
    })

    print("Generating visualization...")
    plt.figure(figsize=(10, 5))
    plt.plot(
            df["time_step"],
            df["stream_value"],
            color="green",
            label="Data Stream"
            )
    plt.title("Matrix Data Stream Analysis")
    plt.xlabel("Time Step")
    plt.ylabel("Signal Amplitude")
    plt.grid(True)
    plt.legend()

    output_filename: str = "matrix_analysis.png"
    plt.savefig(output_filename)
    plt.close()

    print("Analysis complete!")
    print(f"Results saved to: {output_filename}")


def main() -> None:
    if not verify_environment():
        print("\nERROR: Missing required dependencies!")
        print("\nTo install using pip, run:")
        print("  pip install -r requirements.txt")
        print("\nTo install using Poetry, run:")
        print("  poetry install")
        sys.exit(1)

    run_analysis()


if __name__ == "__main__":
    main()
