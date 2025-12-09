class Hero:
    def __init__(self, name , lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        print(f"{self.name} готов к бою!")

h= Hero("Star", 117, 99)
h.action()

class MageHero:
    def __init__(self, name, mp):
        self.name = name
        self.mp = mp
    def action(self, mp):
        print(f"Маг {self.name}  кастует заклинание! MP: {mp}")
class WarriorHero(MageHero):
    def __init__ (self, name, mp, lvl):
        super().__init__(name, mp)
        self.lvl = lvl
    def action(self):
        print(f"Воин {self.name}  рубит мечом! Уровень: {self.lvl}")
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
    def get_bank_name (self):
        return self.bank_name
    def bonus_for_level(self):
        return self.hero.lvl * 10

    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self, other):

        if not isinstance(other, BankAccount):
            return NotImplemented

        # сравниваем *класс* героя (точно тот же тип)
        if type(self.hero) is not type(other.hero):
            raise TypeError("Нельзя складывать аккаунты: герои разных классов.")

        return self._balance + other._balance

    def __eq__(self, other):

        if not isinstance(other, BankAccount):
            return NotImplemented

        name_self = getattr(self.hero, "name", None)
        name_other = getattr(other.hero, "name", None)

        lvl_self = getattr(self.hero, "lvl", None)
        lvl_other = getattr(other.hero, "lvl", None)

        return (name_self == name_other) and (lvl_self == lvl_other)

class OtpSender:
    pass


class KGSms(OtpSender):
    def send_otp(self, phone):
        otp = 1234   # фиксированный код
        return f"<text>Код: {otp}</text><phone>{phone}</phone>"


class RUSms(OtpSender):
    def send_otp(self, phone):
        otp = 1234
        return {"text": f"Код: {otp}", "phone": phone}


mage1 = MageHero("Merlin", 80)
mage2 = MageHero("Merlin", 80)
warrior = WarriorHero("Conan", 50, 9)

acc1 = BankAccount(mage1, 5000, "1234", "Simba")
acc2 = BankAccount(mage2, 3000, "0000", "Simba")
acc3 = BankAccount(warrior, 2500, "1111", "Simba")

mage1.action(44)
warrior.action()

print(acc1)
print(acc2)

print("Банк:", acc1.get_bank_name())
print("Бонус зауровень:", acc1.bonus_for_level(), "SOM")

print("\n=== Проверка __add__ ===")
print("Сумма счетов двух магов:", acc1 + acc2)

print("Сумма мага и воина:", acc1 + acc3)
print("\n=== Проверка __eq__ ===")
print("Mage1 == Mage2 ?", acc1 == acc2)  # True — одинаковое имя и уровень
print("Mage1 == Warrior ?", acc1 == acc3)  # False

sms = KGSms()
print("\n", sms.send_otp("+996558310198"))

