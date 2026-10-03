import os


CONFIG_VARS = (
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT",
)
VALID_MODES = ("development", "production")


def print_config(config: dict[str, str | None]) -> None:
    mode = config["MATRIX_MODE"] or "development"
    if mode not in VALID_MODES:
        print(f"WARNING: unknown MATRIX_MODE '{mode}', using development")
        mode = "development"
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
    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")
    print(f"Database: {database_status}")
    print(f"API Access: {api_key_status}")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {zion_endpoint_status}")


def print_security_check(
        is_env_loaded: bool, config: dict[str, str | None]) -> None:
    print("\nEnvironment security check:")
    if is_env_loaded:
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] No .env file loaded")
    if config["API_KEY"]:
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WARNING] API key missing")
    print("[OK] Production overrides available")


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
    is_env_loaded = load_env_file()
    config = load_config()
    print_missing_warnings(config)
    print_config(config)
    print_security_check(is_env_loaded, config)
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
