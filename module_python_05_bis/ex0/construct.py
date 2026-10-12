import os
import sys


def check_laboratory_status() -> None:
    in_venv: bool = sys.prefix != sys.base_prefix
    current_python: str = sys.executable
    venv_name: str = os.getenv("VIRTUAL_ENV", "None detected")

    if not in_venv:
        print("LABORATORY STATUS: You are working in the open")
        print(f"Current Python: {current_python}")
        print(f"Virtual Environment: {venv_name}")
        print("WARNING: You are in the global environment!")
        print("Every reagent you install here leaks into the whole system.")
        print("To seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print("source lab_env/bin/activate # On Unix")
        print(r"lab_env\Scripts\activate # On Windows")
        print("Then run this program again.")
    else:
        env_path: str = sys.prefix
        site_packages: str = os.path.join(
            env_path,
            "lib",
            f"python{sys.version_info.major}.{sys.version_info.minor}",
            "site-packages",
        )
        print("LABORATORY STATUS: The laboratory is sealed")
        print(f"Current Python: {current_python}")
        print(f"Virtual Environment: {os.path.basename(env_path)}")
        print(f"Environment Path: {env_path}")
        print("SUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecting")
        print("the global system.")
        print("Reagent installation path:")
        print(site_packages)


if __name__ == "__main__":
    check_laboratory_status()
