class Hero:
    def __init__(self, name , lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        print(f"{self.name} готов к бою!")

h= Hero("Star")
h.action()

class MageHero:
    def __init__(self, name, mp):
        super.__init__(name)
        self.mp = mp
    def action(self):
        print(f"Маг {self.name}  кастует заклинание! MP: {mp}")
class WarriorHero(MageHero):
    def __init__ (self, name, mp, lvl):
        super.__init__(name, mp)
        self.lvl = lvl
    def action(self):
        print(f"Воин {self.name}  рубит мечом! Уровень: {lvl}")
class BankAccount:
    def __init__(self, hero, bank_name, balance, password):
        self.hero = hero
        self.bank_name = bank_name
        self._balance = balance
        self.__password = password
    def login (self, password):
        return password == self.__password
    def full_info(self):
        return f"Герой: {self.hero.name} Баланс: {self._balance}"
    def get_bank ()