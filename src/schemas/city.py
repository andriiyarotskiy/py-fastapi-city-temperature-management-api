from pydantic import BaseModel, Field


class CityBase(BaseModel):
    name: str
    additional_info: str | None = Field(max_length=15, default="")


class CityCreate(CityBase):
    pass


class CityUpdate(CityBase):
    pass


class CityRead(CityBase):
    id: int
