class GameObject:

    def __init__(self, name, class_name, health, descr):
        self.name = name
        self.class_name = class_name
        self.descr = descr
        self.health = health
        objects[name] = self #добавляем объект в список объектов

    def get_desr(self):
        return "{}\n  {}".format(self.class_name, self.descr)

    def exam(self):
        return "Имя: {}. Тип: {}".format(self.name, GameObject.get_desr(self))

class Goblin(GameObject):

    def __init__(self, name):
        GameObject.__init__(self = self, 
                            name = name, 
                            class_name = "Goblin", 
                            descr = "Чудище обыкновенное. Зеленый",
                            health = 3)
        
def get_input():
    comand = input(":").split()

    if len(comand)==0:
        return

    act_word = comand[0]

    if act_word in cmd_dict:
        action = cmd_dict[act_word]
        action(comand[1])
    else:
        print("Неизвестная команда '{}'".format(act_word))

objects = {}
ooo = Goblin("Гобл")

def say(text):
    print("Вы сказали: {}".format(text))

def exam(obj_word):
    if obj_word in objects:
        print(objects[obj_word].exam())
    else:
        print("Здесь нету {}".format(obj_word))

cmd_dict = {
    "сказать": say,
    "исследовать": exam
    }

while True:
    get_input()
