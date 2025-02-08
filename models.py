from pydantic import BaseModel, Field

class Index(BaseModel):
    country: str = Field(..., description="Flag of the index.")
    name: str = Field(..., description="Name of the index.")
    last_value: str = Field(..., description="Last value of the index.")    