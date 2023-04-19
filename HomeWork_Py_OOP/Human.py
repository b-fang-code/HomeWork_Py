class Human():

    def get_eye_color(self):
        return self.eye_color

    def get_hair_color(self):
        return self.hair_color

    def set_eye_color(self, eye_color):
        self.eye_color = eye_color

    def set_hair_color(self, hair_color):
        self.hair_color = hair_color

    def __init__(self, name: str, age: int, eye_color, sex: str, height: float, hair_color: str):
        self.name = name
        self.age = age
        self.eye_color = eye_color
        self.sex = sex
        self.height = height
        self.hair_color = hair_color

    def present(self):
        return f'Это {self.name}, возраст: {self.age} лет, цвет глаз: {self.eye_color}, пол: {self.sex}, ' \
               f'рост: {self.height}, цвет волос: {self.hair_color}'
