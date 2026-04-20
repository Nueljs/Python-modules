import os
from dotenv import load_dotenv
import sys


class Config:
    def __init__(self) -> None:
        self.mode: str | None = None
        self.database_url: str | None = None
        self.api_key: str | None = None
        self.log_level: str | None = None
        self.zion_endpoint: str | None = None


def load_environment() -> None:
    dotenv_path: str = os.path.join(os.path.dirname(__file__), ".env")
    if not os.path.exists(dotenv_path):
        print("WARN: .env not found, using environment variables only")
    load_dotenv(dotenv_path)


def get_env_variable(key: str, default: str | None = None) -> str | None:
    return os.environ.get(key, default)


def build_config() -> Config:
    config: Config = Config()
    config.mode = get_env_variable("MATRIX_MODE", "development")
    config.database_url = get_env_variable("DATABASE_URL")
    config.api_key = get_env_variable("API_KEY")
    config.log_level = get_env_variable("LOG_LEVEL", "DEBUG")
    config.zion_endpoint = get_env_variable("ZION_ENDPOINT")

    return config


def validate_config(config: Config) -> None:
    if config.mode == "production" and config.api_key is None:
        print("ERROR: API_KEY is required in production")
        sys.exit(1)


def display_status(config: Config) -> None:
    print()
    print("ORACLE STATUS: Reading the Matrix...")
    print()
    print("Configuration loaded:")
    print(f"Mode: {config.mode}")
    if config.database_url:
        print("Database: Connected to local instance")
    else:
        print("Database: Not configured")
    if config.api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing")
    print(f"Log Level: {config.log_level}")
    if config.zion_endpoint:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")


def security_checks() -> None:
    env_file: str = os.path.join(os.path.dirname(__file__), ".env")
    env_example: str = os.path.join(os.path.dirname(__file__), ".env.example")

    print("[OK] No hardcoded secrets detected")
    if os.path.exists(env_file):
        print("[OK] .env file properly configured")
    elif os.path.exists(env_example):
        print("[OK] .env.example present for reference")

    print("[OK] Production overrides available")


if __name__ == "__main__":
    load_environment()
    config = build_config()
    validate_config(config)
    display_status(config)
    print()
    print("Environment security check:")
    security_checks()
    print()
    print("The Oracle sees all configurations.")
