from Father import Father, father
from Mother import Mother, mother


class Daughter(Father, Mother):
    pass


daughter = Daughter('Маша', 10, father.get_eye_color(), 'женский', 160.2, mother.get_hair_color())
