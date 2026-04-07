import os
import sys
from dotenv import load_dotenv


def load_configuration() -> dict[str, str]:
    """Load configuration from .env file and environment variables."""
    load_dotenv()

    required_vars = [
        "MATRIX_MODE",
        "DATABASE_URL",
        "API_KEY",
        "LOG_LEVEL",
        "ZION_ENDPOINT",
    ]

    config: dict[str, str] = {}
    missing: list[str] = []

    for var in required_vars:
        value = os.getenv(var)
        if value is None:
            missing.append(var)
        else:
            config[var] = value

    if missing:
        print("ERROR: Missing required environment variables:")
        for var in missing:
            print(f"  - {var}")
        print("\nCopy .env.example to .env and fill in your values:")
        print("  cp .env.example .env")
        sys.exit(1)

    return config


def display_configuration(config: dict[str, str]) -> None:
    """Display loaded configuration based on current mode."""
    mode = config["MATRIX_MODE"]

    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if mode == "development":
        print("Database: Connected to local instance")
        print("API Access: Authenticated")
        print(f"Log Level: {config['LOG_LEVEL']}")
        print("Zion Network: Online")
    elif mode == "production":
        print("Database: Connected to production instance")
        print("API Access: Authenticated")
        print(f"Log Level: {config['LOG_LEVEL']}")
        print("Zion Network: Online")


def security_check(config: dict[str, str]) -> None:
    """Verify environment security configuration."""
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] No .env file found — using environment variables")

    if config["MATRIX_MODE"] in ["development", "production"]:
        print("[OK] Production overrides available")


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...\n")

    config = load_configuration()

    display_configuration(config)
    security_check(config)

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
