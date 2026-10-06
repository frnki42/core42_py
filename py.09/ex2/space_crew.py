from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, ValidationError, model_validator


SEPARATOR = "========================================="


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    # nested models: each CrewMember is validated first, the mission
    # validator below only runs if every crew member is valid
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def check_space_mission_model(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError('Mission ID must start with "M"')
        if not any(member.rank in (Rank.COMMANDER, Rank.CAPTAIN)
                   for member in self.crew):
            raise ValueError("Mission must have at least one "
                             "Commander or Captain")
        experts = sum(1 for member in self.crew if member.years_experience > 4)
        if self.duration_days > 365 and experts / len(self.crew) < 0.5:
            raise ValueError("Long missions (> 365 days) need 50% experienced "
                             "crew (5+ years)")
        if not all(member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")
        return self


def create_crew_members() -> list[CrewMember]:
    sarah_connor = CrewMember(
        member_id="0000000000",
        name="Sarah Connor",
        rank=Rank.COMMANDER,
        age=42,
        specialization="Mission Command",
        years_experience=20,
        is_active=True
    )
    john_smith = CrewMember(
        member_id="0000000001",
        name="John Smith",
        rank=Rank.LIEUTENANT,
        age=24,
        specialization="Navigation",
        years_experience=7,
        is_active=True
    )
    alice_johnson = CrewMember(
        member_id="0000000002",
        name="Alice Johnson",
        rank=Rank.OFFICER,
        age=23,
        specialization="Engineering",
        years_experience=5,
        is_active=True
    )
    return [sarah_connor, john_smith, alice_johnson]


def create_space_mission(crew_members: list[CrewMember]) -> SpaceMission:
    space_mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2024, 11, 18, 4, 2, 42),
        duration_days=900,
        crew=crew_members,
        budget_millions=2500.0
    )
    return space_mission


def main() -> None:
    print("Space Mission Crew Validation")
    print(SEPARATOR)
    crew_members = create_crew_members()
    space_mission = create_space_mission(crew_members)
    print("Valid mission created:")
    print(f"Mission: {space_mission.mission_name}")
    print(f"ID: {space_mission.mission_id}")
    print(f"Destination: {space_mission.destination}")
    print(f"Duration: {space_mission.duration_days} days")
    print(f"Budget: ${space_mission.budget_millions}M")
    print(f"Crew size: {len(space_mission.crew)}")
    print("Crew members:")
    for member in space_mission.crew:
        print(f"- {member.name} ({member.rank.value}) "
              f"- {member.specialization}")
    print(f"\n{SEPARATOR}")
    print("Expected validation error:")
    try:
        create_space_mission(crew_members[1:])
    except ValidationError as e:
        print(e.errors()[0]["ctx"]["error"])


if __name__ == "__main__":
    main()
