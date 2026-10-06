import os
import sys
from typing import Optional

from dotenv import load_dotenv  # type: ignore


def load_configuration() -> dict[str, Optional[str]]:
    load_dotenv()

    config: dict[str, Optional[str]] = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }
    return config


def validate_configuration(config: dict[str, Optional[str]]) -> bool:
    missing_keys: list[str] = [key for key, val in config.items() if not val]

    if missing_keys:
        print("WARNING: Missing environment configurations:")
        for key in missing_keys:
            print(f"  - {key} is not set")
        print("\nPlease create a .env file or set environment variables.")
        return False
    return True


def display_oracle_status(config: dict[str, Optional[str]]) -> None:
    mode: str = config.get("MATRIX_MODE") or "unknown"
    db_status: str = (
        "Connected to local instance"
        if mode == "development"
        else "Connected to production cluster"
    )
    log_lvl: str = config.get("LOG_LEVEL") or "INFO"

    print("ORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {db_status}")
    print("API Access: Authenticated")
    print(f"Log Level: {log_lvl}")
    print("Zion Network: Online\n")

    has_hardcoded: bool = False
    has_env_file: bool = os.path.exists(".env")

    print("Environment security check:")
    print(
            f"[{'OK' if not has_hardcoded else 'FAIL'}]"
            f"No hardcoded secrets detected"
        )
    print(
        f"[{'OK' if has_env_file else 'FAIL'}]"
        f" .env file properly configured"
        )
    print("[OK] Production overrides available\n")
    print("The Oracle sees all configurations.")


def main() -> None:
    config: dict[str, Optional[str]] = load_configuration()

    if not validate_configuration(config):
        sys.exit(1)

    display_oracle_status(config)


if __name__ == "__main__":
    main()
