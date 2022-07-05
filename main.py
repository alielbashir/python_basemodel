from models.mesaj import Mesaj
from models.ucak import Ucak


ucaklar: list[Ucak] = [
    Ucak(id=1, lat=4.3, lon=14.3),
    Ucak(id=2, lat=33, lon=0.43),
]

mesaj = Mesaj(secilen_ucak_id=2, ucaklar=ucaklar)


print(mesaj)
