import os
import site
import sys


def is_virtual_env() -> bool:
    return sys.prefix != sys.base_prefix


def get_env_name() -> str:
    return os.path.basename(sys.prefix)


def get_package_path() -> str:
    site_packages: list[str] = site.getsitepackages()
    if site_packages:
        return site_packages[0]
    return "Não encontrado"


def display_global_status() -> None:
    print("MATRIX STATUS: You're still plugged in")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")
    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")
    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env\\Scripts\\activate # On Windows\n")
    print("Then run this program again.")


def display_virtual_status() -> None:
    env_name: str = get_env_name()
    pkg_path: str = get_package_path()

    print("MATRIX STATUS: Welcome to the construct")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {env_name}")
    print(f"Environment Path: {sys.prefix}\n")
    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.\n")
    print("Package installation path:")
    print(pkg_path)


def main() -> None:
    if is_virtual_env():
        display_virtual_status()
    else:
        display_global_status()


if __name__ == "__main__":
    main()
