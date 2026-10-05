from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, ValidationError, model_validator


SEPARATOR = "======================================"


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(max_length=500, default=None)
    is_verified: bool = False

    # model validator restricts even further after attributes got validated
    # and can check several fields together
    @model_validator(mode="after")
    def check_alien_contact_model(self) -> "AlienContact":
        if self.contact_id[:2] != "AC":
            raise ValueError('Contact ID must start with "AC" (Alien Contact)')
        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if (self.contact_type == ContactType.TELEPATHIC and
                self.witness_count < 3):
            raise ValueError("Telepathic contact requires at least "
                             "3 witnesses")
        if self.signal_strength > 7.0 and not self.message_received:
            raise ValueError("Strong signals (> 7.0) should include "
                             "received messages")
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print(SEPARATOR)
    print("Valid contact report:")
    alien = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime(2024, 1, 2, 4, 2, 42),
        location="Area 51, Nevada",
        contact_type=ContactType.RADIO,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli"
    )
    print(f"ID: {alien.contact_id}")
    print(f"Type: {alien.contact_type.value}")
    print(f"Location: {alien.location}")
    print(f"Signal: {alien.signal_strength}/10")
    print(f"Duration: {alien.duration_minutes} minutes")
    print(f"Witnesses: {alien.witness_count}")
    print(f"Message: '{alien.message_received}'\n")
    print(SEPARATOR)
    print("Expected validation error:")
    try:
        AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime(2024, 2, 3, 5, 3, 43),
            location="Area 51, Nevada",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=4.2,
            duration_minutes=42,
            witness_count=1,
            message_received="The Zion resistance will fall in the next week"
        )
    except ValidationError as e:
        print(e.errors()[0]["ctx"]["error"])


if __name__ == "__main__":
    main()
