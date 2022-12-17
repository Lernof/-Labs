class Car():
    def __init__(self, brand, class_of_car, driver, engine) -> None:
        self.brand: str = brand
        self.class_of_car: str = class_of_car
        self.driver: Driver = driver
        self.engine: Engine = engine
    
    def start(self):
        print('Поехали')

    def stop(self):
        print('Останавливаемся')

    def turnRight(self):
        print('Поворот направо')
        
    def turnLeft(self):
        print('Поворот налево')

    def __str__(self):
        return f'brand: {self.brand}\tclass of car: {self.class_of_car}\n{str(self.driver)}\n{str(self.engine)}'

class Engine():
    def __init__(self, power, manifacturer) -> None:
        self.power: int = power
        self.manifacturer: str = manifacturer

    def __str__(self):
        return f'power: {self.power}\tmanifacturer: {self.manifacturer}'


class Person():

    def __init__(self, age: int, full_name) -> None:
        if 0 < age < 110:
            self.__age = age
        else: raise ValueError('Invalid age')
        self.full_name = full_name 

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 0 < age < 110:
            self.__age = age
        else: print('Invalid age')

    def __str__(self):
        return f'age: {self.age}\tfull name: {self.full_name}'

class Driver(Person):
    def __init__(self, age, full_name, experience_in_years) -> None:
        super().__init__(age, full_name)
        self.experience_in_years: int = experience_in_years
    
    def __str__(self):
        return super().__str__() + f'\texperience in years: {self.experience_in_years}'

class Lorry(Car):

    def __init__(self, brand, class_of_car, driver, engine, carrying) -> None:
        super().__init__(brand, class_of_car, driver, engine)
        self.carrying = carrying

    def __str__(self):
        return super().__str__() + f'\tcarrying: {self.carrying}'

class SportCar(Car):
    def __init__(self, brand, class_of_car, driver, engine, speed) -> None:
        super().__init__(brand, class_of_car, driver, engine)
        self.speed = speed

    def __str__(self):
        return super().__str__() + f'\tspeed: {self.speed}'

engine = Engine(20, 'BMW')
driver = Driver(25, 'Amir Abdykeyev', 3)

car = Car(brand='BMW', class_of_car='sport car', driver=driver, engine=engine)
sport_car = SportCar(brand='BMW', class_of_car='sport car', driver=driver, engine=engine, speed = 30)
