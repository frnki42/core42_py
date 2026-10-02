import sys
from importlib.metadata import version, PackageNotFoundError


DEPENDENCIES = {
    "pandas": "Data manipulation",
    "numpy": "Numerical computation",
    "matplotlib": "Visualization"
}


def print_install_instructions() -> None:
    print("\nTo install the missing dependencies:\n")
    print("___ using pip ___:")
    print("Create your virtual environment: python3 -m venv .venv")
    print("Activate the virtual environment: source .venv/bin/activate")
    print("Use requirements.txt to install missing dependencies:")
    print("pip install -r requirements.txt")
    print("Run the program again: python3 loading.py")
    print("\n___ using poetry ___:")
    print("Install missing dependencies: poetry install")
    print("Run the program again: poetry run python loading.py")


def check_dependencies() -> list[str]:
    print("Checking dependencies:")
    missing: list[str] = []
    for name, description in DEPENDENCIES.items():
        try:
            dep_version = version(name)
        except PackageNotFoundError:
            missing.append(name)
            print(f"[MISSING] {name} - {description}: not installed")
        else:
            print(f"[OK] {name} ({dep_version}) - {description} ready")
    return missing


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    missing_dependencies = check_dependencies()
    if missing_dependencies:
        print_install_instructions()
        sys.exit(1)


if __name__ == "__main__":
    main()
