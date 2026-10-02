from importlib.metadata import version, PackageNotFoundError


DEPENDENCIES = {
    "pandas": "Data manipulation",
    "numpy": "Numerical computation",
    "matplotlib": "Visualization"
}


def check_dependencies() -> list[str]:
    print("Checking dependencies:")
    missing: list[str] = []
    for name, description in DEPENDENCIES.items():
        try:
            dep_version = version(name)
        except PackageNotFoundError:
            missing.append(name)
            print(f"[MISSING] {name} - {description} not ready")
        else:
            print(f"[OK] {name} ({dep_version}) - {description} ready")
    return missing


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    check_dependencies()


if __name__ == "__main__":
    main()
