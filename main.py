# class Human:
#     def __init__(self, name):
#         self.name = name
#
#
# class Auto:
#     def __init__(self, brand):
#         self.brand = brand
#         self.passengers = []
#
#     def add_passengers(self, human):
#         self.passengers.append(human)
#
#     def print_passengers(self):
#         if self.passengers != []:
#             print(f'Names of {self.brand} passengers:')
#             for passenger in self.passengers:
#                 print(passenger.name)
#
# nick = Human('Nick')
# anna = Human('Anna')
# car = Auto('BMW')
# car.add_passengers(nick)
# car.add_passengers(anna)
# car.print_passengers()
import random
class Human:
    def __init__(self, name='Human', job=None, home=None, car=None, pet='cat'):
        self.name = name
        self.job = job
        self.home = home
        self.car = car
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.pet = pet
    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)
    def get_car(self):
        self.car = Auto(brands_of_car)
    def get_home(self):
        self.home = House()

    def eat(self):
        if self.home.food <= 0:
            self.shopping('food')
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5
    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 10:
                self.shopping('fuel')
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness
        self.satiety -= 5
    def shopping(self):
        pass
    def chill(self):
        pass
    def clean_home(self):
        pass
    def to_repair(self):
        pass

    def days_indexes(self):
        pass
    def is_alive(self):
        pass
    def live(self, day):
        pass

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= 10
            self.strength -= 1
            return True
        else:
            print('The car cannot move')
            return False



class House:
    def __init__(self):
        self.food = 0
        self.mess = 0

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness = job_list[self.job['job_gladness']]

class Pet:
    def __int__(self, pet_condition):
        self.pet = random.choise(list(pet_condition))
        self.pet = pet_condition[self.pet['pet_gladness']]
        self.gladness += 10
        self.salary -= 0.5




pet_condition = {'feed':{'gladness': 0, 'salary': -0.5, 'pet_gladness': +5},
                 'play':{'gladness': +10, 'salary': 0, 'pet_gladness': +5},
                 'walk':{'gladness': +5, 'salary': 0, 'pet_gladness': +5}}

job_list = {'C++': {'salary': 90, 'job_gladness': 3},
            'Python': {'salary': 50, 'job_gladness': 10},
            'Java': {'salary': 70, 'job_gladness': 7},
            'PHP': {'salary': 40, 'job_gladness': 5}}

brands_of_car = {"BMW": {'fuel': 100, 'strength': 100, 'consumption': 6},
                 "Lada": {'fuel': 50, 'strength': 30, 'consumption': 9},
                 "Ford": {'fuel': 80, 'strength': 150, 'consumption': 8},
                 "Audi": {'fuel': 70, 'strength': 120, 'consumption': 7}}

