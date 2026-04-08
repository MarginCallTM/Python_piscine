from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import Optional
from enum import Enum


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field()
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType = Field()
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def check_signal_rules(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with AC")
        if self.contact_type == ContactType.physical:
            if not self.is_verified:
                raise ValueError("Physical contact must be verified")
        if self.contact_type == ContactType.telepathic:
            if self.witness_count < 3:
                raise ValueError("Telepathic contact need at least 3 Witness")
        if self.signal_strength > 7.0:
            if not self.message_received:
                raise ValueError("Strong signals need at least 7.0 signals")
        return self


if __name__ == "__main__":
    try:
        print("Alien Contact Log Validation")
        print("======================================")
        print("Valid contact report:")

        alien = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime(2024, 7, 15, 14, 30),
            contact_type=ContactType.radio,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli"
        )
        print(f"ID: {alien.contact_id}")
        print(f"Type: {alien.contact_type}")
        print(f"Location: {alien.location}")
        print(f"Signal: {alien.signal_strength}/10")
        print(f"Duration: {alien.duration_minutes} minutes")
        print(f"Witnesses: {alien.witness_count}")
        print(f"Message: {alien.message_received}")
        print("\n======================================")
    except ValidationError as e:
        print(e)
    try:
        print("Expected validation error:")
        bad_alien = AlienContact(
            contact_id="AC-130",
            timestamp=datetime(2024, 7, 15, 14, 30),
            contact_type=ContactType.telepathic,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=1,
            message_received="Greetings from Zeta Reticuli"
        )
    except ValidationError as e:
        print(e)
