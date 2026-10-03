import os
from dotenv import load_dotenv


CONFIG_VARS = (
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
)


def print_config(config: dict[str, str | None]) -> None:
    print("Configuration loaded:")
    matrix_mode_status = config["MATRIX_MODE"] or "not set"
    log_level_status = config["LOG_LEVEL"] or "not set"
    if config["DATABASE_URL"]:
        database_url_status = "Connected to local instance"
    else:
        database_url_status = "not set"
    if config["API_KEY"]:
        api_key_status = "Authenticated"
    else:
        api_key_status = "not set"
    if config["ZION_ENDPOINT"]:
        zion_endpoint_status = "Online"
    else:
        zion_endpoint_status = "Offline"
    print(f"Mode: {matrix_mode_status}")
    print(f"Database: {database_url_status}")
    print(f"API Access: {api_key_status}")
    print(f"Log Level: {log_level_status}")
    print(f"Zion Network: {zion_endpoint_status}")


def load_config() -> dict[str, str | None]:
    config: dict[str, str | None] = {}
    for name in CONFIG_VARS:
        config[name] = os.getenv(name)
    return config


def main() -> None:
    load_dotenv()
    print("\nORACLE STATUS: Reading the Matrix...\n")
    config = load_config()
    print_config(config)


if __name__ == "__main__":
    main()
