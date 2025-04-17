from pydantic import BaseModel, Field


class InputSchema(BaseModel):
    question: str = Field(..., description="User query for the chatbot.")
    namespace: str = Field(..., description="Namespace for the database.")
    previous_conversation: list = Field([], description="Previous conversation history.")
    llm_provider: str = Field(..., description="LLM provider (e.g., 'openai', 'anthropic')")
    llm_model: str = Field(..., description="LLM model name")


class PetBioSimple:
    class PetOverview(BaseModel):
        name: str = Field(default="Buddy", example="Buddy")
        species: str = Field(default="Dog", example="Dog")
        age: float = Field(default=2.0, example=2.0)

    class BasicCare(BaseModel):
        daily_routine: str = Field(default="Feeds at 8 AM and 6 PM", example="Feeds at 8 AM and 6 PM")
        grooming_frequency: str = Field(default="Monthly", example="Weekly")

    class Nutrition(BaseModel):
        food_type: str = Field(default="Dry kibble", example="Dry kibble")
        feeding_times_per_day: int = Field(default=2, example=2)

    class Exercise(BaseModel):
        activity_level: str = Field(default="Moderate", example="High")
        favorite_activity: str = Field(default="Walks", example="Fetch")

    class TrainingBehavior(BaseModel):
        trained: bool = Field(default=True, example=True)
        behavior_issue: Optional[str] = Field(default=None, example="Excessive barking")

    class HealthMonitoring(BaseModel):
        last_vet_visit: str = Field(default="2025-01-10", example="2025-01-10")
        any_recent_symptoms: Optional[str] = Field(default=None, example="Vomiting")

    class Grooming(BaseModel):
        brushing_frequency: str = Field(default="Twice a week", example="Daily")
        nail_trim_frequency: str = Field(default="Every 3 weeks", example="Monthly")

    class PetSafety(BaseModel):
        restricted_areas: Optional[List[str]] = Field(default_factory=list, example=["Kitchen"]) 
        frequently_travels: bool = Field(default=False, example=False)

    class SeasonalCare(BaseModel):
        handles_cold_well: bool = Field(default=False, example=False)
        uses_weather_items: List[str] = Field(default_factory=lambda: ["Jacket"], example=["Paw balm", "Jacket"])


class PetBioDetailed: 
    class PetOverview(BaseModel):
        name: str = Field(default="Buddy", example="Buddy")
        species: str = Field(default="Dog", example="Dog")
        breed: str = Field(default="Golden Retriever", example="Golden Retriever")
        age: float = Field(default=2.5, example=2.5, description="Age in years")
        weight: float = Field(default=30.0, example=30.0, description="Weight in kg")
        gender: str = Field(default="Male", example="Male")
        is_neutered: bool = Field(default=True, example=True)
        medical_conditions: List[str] = Field(default_factory=list, example=["Allergies"])

        class Config:
            schema_extra = {
                "example": {
                    "name": "Buddy",
                    "species": "Dog",
                    "breed": "Golden Retriever",
                    "age": 2.5,
                    "weight": 30.0,
                    "gender": "Male",
                    "is_neutered": True,
                    "medical_conditions": ["Allergies"]
                }
            }

    class BasicCare(BaseModel):
        daily_routine: str = Field(default="Wakes up at 7 AM, eats at 8 AM & 6 PM, walks twice daily.", example="...")
        grooming_frequency: str = Field(default="Monthly", example="Weekly")
        vaccinations_up_to_date: bool = Field(default=True, example=True)
        parasite_control_method: str = Field(default="Monthly drops", example="Monthly drops")

        class Config:
            schema_extra = {
                "example": {
                    "daily_routine": "Wakes up at 7 AM, eats at 8 AM & 6 PM, walks twice daily.",
                    "grooming_frequency": "Monthly",
                    "vaccinations_up_to_date": True,
                    "parasite_control_method": "Monthly drops"
                }
            }

    class Nutrition(BaseModel):
        food_type: str = Field(default="Dry kibble", example="Dry kibble")
        feeding_frequency_per_day: int = Field(default=2, example=2)
        food_allergies: List[str] = Field(default_factory=list, example=["Chicken"])
        treat_frequency: str = Field(default="Once a day", example="Twice a week")
        open_to_diet_change: bool = Field(default=True, example=True)

        class Config:
            schema_extra = {
                "example": {
                    "food_type": "Dry kibble",
                    "feeding_frequency_per_day": 2,
                    "food_allergies": ["Chicken"],
                    "treat_frequency": "Once a day",
                    "open_to_diet_change": True
                }
            }

    class Exercise(BaseModel):
        activity_level: str = Field(default="Moderate", example="High")
        favorite_activities: List[str] = Field(default_factory=lambda: ["Walks", "Fetch"], example=["Walks", "Fetch"])
        outdoor_time_per_day: str = Field(default="1 hour", example="2 hours")
        social_with_other_pets: Optional[bool] = Field(default=True, example=True)

        class Config:
            schema_extra = {
                "example": {
                    "activity_level": "High",
                    "favorite_activities": ["Walks", "Fetch"],
                    "outdoor_time_per_day": "2 hours",
                    "social_with_other_pets": True
                }
            }

    class TrainingBehavior(BaseModel):
        trained: bool = Field(default=True, example=True)
        knows_basic_commands: bool = Field(default=True, example=True)
        behavior_issues: List[str] = Field(default_factory=list, example=["Chewing furniture"])
        reaction_to_strangers: str = Field(default="Friendly", example="Anxious")

        class Config:
            schema_extra = {
                "example": {
                    "trained": True,
                    "knows_basic_commands": True,
                    "behavior_issues": ["Chewing furniture"],
                    "reaction_to_strangers": "Anxious"
                }
            }

    class HealthMonitoring(BaseModel):
        last_vet_check: str = Field(default="2025-01-10", example="2025-01-10")
        recent_symptoms: List[str] = Field(default_factory=list, example=["Vomiting"])
        has_pet_insurance: bool = Field(default=False, example=False)

        class Config:
            schema_extra = {
                "example": {
                    "last_vet_check": "2025-01-10",
                    "tracks_health_metrics": True,
                    "recent_symptoms": ["Vomiting"],
                    "has_pet_insurance": False
                }
            }

    class Grooming(BaseModel):
        brushing_frequency: str = Field(default="3 times a week", example="Daily")
        ear_eye_cleaning: bool = Field(default=True, example=True)
        dental_care: str = Field(default="Once a week", example="Daily")
        nail_trimming_frequency: str = Field(default="Every 3 weeks", example="Every 2 weeks")

        class Config:
            schema_extra = {
                "example": {
                    "brushing_frequency": "Daily",
                    "ear_eye_cleaning": True,
                    "dental_care": "Daily",
                    "nail_trimming_frequency": "Every 2 weeks"
                }
            }

    class PetSafety(BaseModel):
        has_toxic_plants_at_home: bool = Field(default=False, example=False)
        restricted_areas: List[str] = Field(default_factory=lambda: ["Kitchen"], example=["Garage", "Balcony"])
        frequently_travels: bool = Field(default=False, example=False)
        uses_collar_or_id: bool = Field(default=True, example=True)

        class Config:
            schema_extra = {
                "example": {
                    "has_toxic_plants_at_home": False,
                    "restricted_areas": ["Garage", "Balcony"],
                    "frequently_travels": True,
                    "uses_collar_or_id": True
                }
            }

    class SeasonalCare(BaseModel):
        handles_weather_well: str = Field(default="Handles heat better than cold", example="Sensitive to cold")
        weather_specific_items: List[str] = Field(default_factory=lambda: ["Jacket", "Cooling mat"], example=["Paw balm"])
        has_seasonal_allergies: Optional[bool] = Field(default=False, example=True)
        changes_routine_in_season: bool = Field(default=True, example=True)

        class Config:
            schema_extra = {
                "example": {
                    "handles_weather_well": "Sensitive to cold",
                    "weather_specific_items": ["Paw balm"],
                    "has_seasonal_allergies": True,
                    "changes_routine_in_season": True
                }
            }


