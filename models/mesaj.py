from pydantic import BaseModel

from models.ucak import Ucak


class Mesaj(BaseModel):
    secilen_ucak_id: int
    ucaklar: list[Ucak]
