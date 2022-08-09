import random
names = ['Орк', 'Эльф']
class Voin:

    def __init__(self, name, hp, attack_power):
        self.name = name
        self.health = hp
        self.attack_power = attack_power


    def attack(self):
        if(self.name == names[0]):
            enemy = elf
        else:
            enemy = ork
        hp_left = enemy.take_damage(self.attack_power)
        return(f'{self.name} атаковал {enemy.name} и оставил ему {hp_left} hp')

    def take_damage(self, damage_amount):
        self.health -= 20
        return self.health
ork = Voin(names[0], 100, 20)
elf = Voin(names[1], 100, 20)
while ork.health > 0 and elf.health > 0:
    a = (random.choice(names))
    if a == names[0]:
        print(ork.attack())
    else:
        print(elf.attack())

print('Игра окончена!')
