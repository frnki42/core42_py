from datetime import datetime

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str = Field(max_length=200, default="")


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    valid_space_station = SpaceStation(
        station_id=".frnki-000",
        name=".frnki",
        crew_size=4,
        power_level=0.42,
        oxygen_level=4.20,
        last_maintenance=datetime(1942, 4, 2, 4, 2, 42),
        is_operational=False
    )
    print("Valid station created:")
    print(f"ID: {valid_space_station.station_id}")
    print(f"Name: {valid_space_station.name}")
    print(f"Crew: {valid_space_station.crew_size}")
    print(f"Power: {valid_space_station.power_level}")
    print(f"Oxygen: {valid_space_station.oxygen_level}")
    if valid_space_station.is_operational:
        status = "Operational"
    else:
        status = "Not Operational"
    print(f"Status: {status}\n")
    print("========================================")
    print("Expected validation error:")
    try:
        invalid_space_station = SpaceStation(
            station_id=".frnki-001",
            name=".frnki-invalid",
            crew_size=42,
            power_level=42.0,
            oxygen_level=4.20,
            last_maintenance=datetime(1942, 2, 4, 4, 2, 42),
        )
    except ValidationError as e:
        print(e)


if __name__ == "__main__":
    main()
