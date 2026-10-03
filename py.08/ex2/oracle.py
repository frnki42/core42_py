import os


CONFIG_VARS = (
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
)


def print_config(config: dict[str, str | None]) -> None:
    print("\nConfiguration loaded:")
    mode = config["MATRIX_MODE"] or "development"
    is_production = mode == "production"
    if not config["DATABASE_URL"]:
        database_status = "not set"
    elif is_production:
        database_status = "Connected to production database"
    else:
        database_status = "Connected to local instance"
    if config["API_KEY"]:
        api_key_status = "Authenticated"
    else:
        api_key_status = "not set"
    if config["LOG_LEVEL"]:
        log_level = config["LOG_LEVEL"]
    elif is_production:
        log_level = "INFO"
    else:
        log_level = "DEBUG"
    if config["ZION_ENDPOINT"]:
        zion_endpoint_status = "Online"
    else:
        zion_endpoint_status = "Offline"
    print(f"Mode: {mode}")
    print(f"Database: {database_status}")
    print(f"API Access: {api_key_status}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {zion_endpoint_status}")


def print_missing_warnings(config: dict[str, str | None]) -> None:
    for name in CONFIG_VARS:
        if not config[name]:
            print(f"WARNING: {name} is not set")


def load_config() -> dict[str, str | None]:
    config: dict[str, str | None] = {}
    for name in CONFIG_VARS:
        config[name] = os.getenv(name)
    return config


def load_env_file() -> bool:
    try:
        from dotenv import load_dotenv
    except ImportError:
        print("\nWARNING: python-dotenv not installed, .env file ignored")
        return False
    return load_dotenv()


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...")
    load_env_file()
    config = load_config()
    print_missing_warnings(config)
    print_config(config)


if __name__ == "__main__":
    main()
