from pydantic import BaseModel


class Ucak(BaseModel):
    id: int
    lat: float
    long: float
    alt: float
