import pandas as pd
from pydantic import BaseModel, Field


class HeartAttackData(BaseModel):
    age: int = Field(..., ge=14, le=120)
    gender: bool = Field(...)
    heart_rate: int = Field(..., ge=20, le=200)
    systolic_blood_pressure: int = Field(..., ge=30, le=250)
    diastolic_blood_pressure: int = Field(..., ge=30, le=250)
    blood_sugar: int = Field(..., ge=30, le=550)
    ck_mb: float = Field(..., ge=0, le=300)
    troponin: float = Field(..., ge=0, le=15)

    def to_dataframe(self) -> pd.DataFrame:
        return pd.DataFrame([self.model_dump()])
