'''Создать класс «Живое». Определить наследуемые классы – «лиса», «кролик» и «растение».
Лиса ест кролика. Кролик ест растения. Растение поглощает солнечный свет.
Представитель каждого класса может умереть, если достигнет определенного возраста или для него не будет еды.
Напишите виртуальные методы поедания и определения состояния живого существа (живой или нет,
в зависимости от достижения предельного возраста и наличия еды (входной параметр)).'''


class Alive:
    def __init__(self, population):
        self.population = population


class Plants(Alive):
    def __init__(self, koef_repr, population):
        super().__init__(population)
        self.koef_repr = koef_repr

    def reproduction(self):
        self.population *= self.koef_repr

    def info_population(self):
        print("count plants:", self.population)

    def rabbits_food(self, count_rabbits):
        self.population -= count_rabbits * 10

    def add_plants(self, count_plants):
        self.population += count_plants

    def dry(self):
        self.population -= int(self.population * 0.10)

    def frosts(self):
        self.population -= int(self.population * 0.05)


class Rabbit(Alive):
    def __init__(self, koef_repr, koef_death, population):
        super().__init__(population)
        self.koef_repr = koef_repr
        self.koef_death = koef_death

    def death(self):
        self.population -= int(self.population * self.koef_death)

    def info_population(self):
        print("count rabbits:", self.population)

    def reproduction(self):
        self.population *= self.koef_repr

    def teke_away(self, count_rabbits):
        self.population -= count_rabbits

    def foxes_food(self, count_foxes):
        self.population += int(count_foxes * 365)

    def rabbits_sale(self):
        # global budget = int(self.population * 0.50)
        self.population -= int(self.population * 0.50)

class Fox(Alive):

    def __init__(self, koef_repr, koef_death, population):
        super().__init__(population)
        self.koef_repr = koef_repr
        self.koef_death = koef_death

    def death(self):
        self.population -= int(self.population * self.koef_death)

    def info_population(self):
        print("count foxes:", self.population)

    def reproduction(self):
        self.population *= self.koef_repr

    def take_away(self, count_foxes):
        self.population -= count_foxes

    def foxes_sale(self):
        self.population -= int(self.population * 0.30)

plants = Plants(7, 70000)
rabbits = Rabbit(10, 0.3, 11)
foxes = Fox(2, 0.1, 10)

year = 1
while year <= 10:

    if plants.population <= 0 or rabbits.population <= 0:
        print("fatality")
        print("You lose on year", year)
        break

    if plants.population <= rabbits.population * 10:
        print("warning!!!")
        print(f" rabbits {rabbits.population} plants {plants.population}")
        choise = int(input("1 - add plants 2 - takeaway rabbits:"))
        if choise == 1:
            print("you need to add", rabbits.population * 10 - plants.population)
            count_plants = int(input("enter plants:"))
            plants.add_plants(count_plants)
        elif choise == 2:
            print("you need take away:", rabbits.population - plants.population // 10)
            count_rabbits = int(input("enter rabbits:"))
            rabbits.teke_away(count_rabbits)

    print("year is:", year)
    plants.rabbits_food(rabbits.population)

    rabbits.foxes_food(foxes.population)

    plants.reproduction()
    plants.dry()
    plants.frosts()
    plants.info_population()

    rabbits.reproduction()
    rabbits.death()
    rabbits.rabbits_sale()
    rabbits.info_population()

    foxes.reproduction()
    foxes.death()
    foxes.foxes_sale()
    foxes.info_population()
    year += 1


