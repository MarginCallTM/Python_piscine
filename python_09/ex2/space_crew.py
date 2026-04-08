from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import List
from enum import Enum


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank = Field()
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field()
    duration_days: int = Field(ge=1, le=3650)
    crew: List[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validation_rules(self) -> 'SpaceMission':
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID: should start with M")
        if not any(member.rank in (Rank.captain, Rank.commander)
                   for member in self.crew):
            raise ValueError("Mission must have at"
                             "least one Captain or Commander")
        if self.duration_days > 365:
            hint = sum(
                1 for member in self.crew if member.years_experience >= 5)
            if hint < len(self.crew) / 2:
                raise ValueError("Long missions need 50% experienced crew")
        if any(not member.is_active for member in self.crew):
            raise ValueError("All crew members must be active")
        return self


if __name__ == "__main__":
    Edwins = CrewMember(
        member_id="OSS117",
        name="Edwins",
        rank=Rank.commander,
        age=29,
        specialization="Mission Command",
        years_experience=40,
        is_active=True
    )
    Aldrin = CrewMember(
        member_id="OSS118",
        name="Aldrin",
        rank=Rank.lieutenant,
        age=30,
        specialization="Navigation",
        years_experience=41,
        is_active=True
    )
    Armstrong = CrewMember(
        member_id="OSS119",
        name="Armstrong",
        rank=Rank.officer,
        age=31,
        specialization="Engineering",
        years_experience=42,
        is_active=True
    )

    iss = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2026, 1, 15),
        duration_days=900,
        crew=[Edwins, Aldrin, Armstrong],
        mission_status="planned",
        budget_millions=2500.0
    )

    try:
        print("Space Mission Crew Validation")
        print("=========================================")
        print("Valid mission created:")
        print(f"Mission: {iss.mission_name}")
        print(f"ID: {iss.mission_id}")
        print(f"Destination: {iss.destination}")
        print(f"Duration: {iss.duration_days} days")
        print(f"Budget: ${iss.budget_millions}M")
        print("Crew members:")
        for member in iss.crew:
            print(
                f"- {member.name} "
                f"({member.rank.value}) - {member.specialization}")
    except ValidationError as e:
        print(e)
    print("\n=========================================")
    try:
        Edwins = CrewMember(
            member_id="OSS117",
            name="Edwins",
            rank=Rank.commander,
            age=29,
            specialization="Mission Command",
            years_experience=40,
            is_active=True
        )

        Aldrin = CrewMember(
            member_id="OSS118",
            name="Aldrin",
            rank=Rank.lieutenant,
            age=30,
            specialization="Navigation",
            years_experience=41,
            is_active=False
        )

        Armstrong = CrewMember(
            member_id="OSS119",
            name="Armstrong",
            rank=Rank.officer,
            age=31,
            specialization="Engineering",
            years_experience=42,
            is_active=True
        )

        iss = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(2026, 1, 15),
            duration_days=900,
            crew=[Edwins, Aldrin, Armstrong],
            mission_status="planned",
            budget_millions=2500.0
        )
        print("Space Mission Crew Validation")
        print("=========================================")
        print("Valid mission created:")
        print(f"Mission: {iss.mission_name}")
        print(f"ID: {iss.mission_id}")
        print(f"Destination: {iss.destination}")
        print(f"Duration: {iss.duration_days} days")
        print(f"Budget: ${iss.budget_millions}M")
        print("Crew members:")
        for member in iss.crew:
            print(
                f"- {member.name} "
                f"({member.rank.value}) - {member.specialization}")
    except ValidationError as e:
        print(e)
