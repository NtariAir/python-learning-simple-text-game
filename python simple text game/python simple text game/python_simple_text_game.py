class GameObject:

    __health_list = tuple()

    def __init__(self, name, class_name, health, descr, health_list):
        self.name = name
        self.class_name = class_name
        self.descr = descr
        self.__health = health
        self.__health_list = health_list
        objects[name] = self #добавляем объект в список

    def get_desr(self):
       
       return "{}\n  {}".format(self.class_name, self.descr)

    def exam(self):
       
        return "Имя: {}. Тип: {}".format(self.name, GameObject.get_desr(self))

    @property
    def health(self):
        
        return self.__health
    
    @health.setter
    def health(self, newHelth):
        
        self.__health = newHelth

    def hit_object(self, dmg = 1):
        
        if self.health > 0:
            self.health -= dmg
            return("Вы ударили '{}'".format(self.name))
        else:
            return "{}".format(self.status)
    
    @property
    def status(self):
        return "'{}':  {}".format(self.name, self.__health_list[self.health])
    

class Goblin(GameObject):

    def __init__(self, name):
        super().__init__(name = name, 
                         class_name = "Goblin",
                         health = 3,
                         descr = "Чудище обыкновенное. Зеленый, глупый, жадный, грязный",
                         health_list = ("Совсем мертвый", "Рука оторвана", "Слегка потрепан", "Вполне здоров")
                         )
        
class Human(GameObject):
    def __init__(self, name):
        super().__init__(name = name, 
                         class_name = "Human",
                         health = 5,
                         descr = "Человек. Наверное, разумный. Хотя до Вас ему далеко, конечно же",
                         health_list = ("Совсем мертвый", 
                                        "Кажется он не дышит",
                                        "Встать уже точно не сможет",
                                        "Кажется, ему плохо",
                                        "Слегка потрепан", 
                                        "Вполне здоров")
                         )

def get_input():
    comand = input(":").split()

    if len(comand)==0:
        return

    act_word = comand[0]

    if act_word.lower() in cmd_dict:
        action = cmd_dict[act_word.lower()]

        if len(comand) > 1:
            action(comand[1])
        else:
            action()

    else:
        print("Неизвестная команда '{}'".format(act_word))

objects = {}

ooo = Goblin("Гобл")
ppp = Human("ВРАЖИНА")

def say(text = ""):

    print("Вы сказали: {}".format(text))

def exam(obj_word = None):
    if obj_word == None:
        print("Вы находитесь здесь")
        print()
    elif obj_word in objects:
        print(objects[obj_word].exam())
    else:
        print("Здесь нету '{}'".format(obj_word))

def state(obj_word = None):
    if obj_word == None:
        print("Вы вполне здоровы")
    elif obj_word in objects:
        print(objects[obj_word].status)
    else:
        print("Непонятно кто такой этот '{}'".format(obj_word))

def hit(obj_word = None):
    if obj_word == None:
        print("Вы ударили себя в лицо")
    elif obj_word in objects:
        print(objects[obj_word].hit_object())
    else:
        print("Непонятно как ударить это '{}'".format(obj_word))

cmd_dict = {
    "сказать": say,
    "исследовать": exam,
    "состояние": state,
    "ударить": hit
    }

while True:
    get_input()
