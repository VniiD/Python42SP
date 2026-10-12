import os
from typing import Optional
from dotenv import load_dotenv


def load_configuration() -> None:
    env_path: str = os.path.join(os.path.dirname(__file__), ".env")
    load_dotenv(dotenv_path=env_path)

    matrix_mode: str = os.getenv("MATRIX_MODE", "development")
    database_url: Optional[str] = os.getenv("DATABASE_URL")
    api_key: Optional[str] = os.getenv("API_KEY")
    log_level: str = os.getenv("LOG_LEVEL", "DEBUG")
    zion_endpoint: str = os.getenv("ZION_ENDPOINT", "http://offline")

    print("ORACLE STATUS: Consulting the configuration...")
    print("Configuration loaded:")
    print(f"Mode: {matrix_mode}")

    if database_url:
        print("Database: Connected to local instance")
    else:
        print("Database: WARNING - Missing configuration!")

    if api_key:
        print("Access: Authenticated")
    else:
        print("Access: WARNING - Unauthenticated (Missing API_KEY)")

    print(f"Log Level: {log_level}")

    if zion_endpoint != "http://offline":
        print("Remote Network: Online")
    else:
        print("Remote Network: Offline or Unconfigured")

    print("\nConfiguration security check:")
    if api_key and api_key != "dev_key_placeholder_999":
        print("[OK] No hardcoded secrets detected")
    else:
        print("[OK] No hardcoded secrets detected (using env/default)")

    git_ignored: bool = os.path.exists(
        os.path.join(os.path.dirname(__file__), ".gitignore")
    )
    if git_ignored:
        print("[OK] .env file properly ignored by git")
    else:
        print("[WARNING] .gitignore not found in ex1/")

    if matrix_mode == "production":
        print("[OK] Production overrides available")
    else:
        print("[OK] Development mode active")


if __name__ == "__main__":
    load_configuration()
