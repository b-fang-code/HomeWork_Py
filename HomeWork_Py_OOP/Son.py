from Father import Father, father
from Mother import Mother, mother


class Son(Father, Mother):
    pass


son = Son('Аркаша', 5, mother.get_eye_color(), 'мужской', 120.3, father.get_hair_color())
