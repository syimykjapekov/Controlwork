from functools import wraps

# Словарь разрешенных команд по ролям
ALLOWED_COMMANDS = {
    "admin": ["start", "ban", "stop", "message"],
    "user": ["start", "message"]
}


class User:
    """Класс пользователя системы"""

    def __init__(self, username: str, role: str):
        self.username = username
        self.role = role

    def __str__(self):
        return f"{self.username} ({self.role})"


class CommandHandler:
    """Обработчик команд с контролем доступа"""

    def __init__(self):
        pass

    # Декоратор проверки прав доступа
    @staticmethod
    def check_permission(command_name: str):
        """Декоратор для проверки разрешений пользователя"""

        def decorator(func):
            @wraps(func)
            def wrapper(self, user: User, *args, **kwargs):
                # Проверка существования команды
                if command_name not in ALLOWED_COMMANDS["admin"] + ALLOWED_COMMANDS["user"]:
                    print(f"❌ Команда '{command_name}' не существует")
                    return

                # Проверка разрешений пользователя
                if command_name in ALLOWED_COMMANDS[user.role]:
                    print(f"✅ Пользователь {user} выполняет команду '{command_name}'")
                    return func(self, user, *args, **kwargs)
                else:
                    print(f"❌ Пользователь {user.username} не может выполнять команду '{command_name}'")
                    return None

            return wrapper

        return decorator

    @check_permission("start")
    def start(self, user: User):
        """Команда запуска системы"""
        print(f"   Система запущена пользователем {user.username}")

    @check_permission("ban")
    def ban(self, user: User, target_user: str = "нарушитель"):
        """Команда блокировки пользователя"""
        print(f"   Пользователь {target_user} заблокирован администратором {user.username}")

    @check_permission("stop")
    def stop(self, user: User):
        """Команда остановки системы"""
        print(f"   Система остановлена пользователем {user.username}")

    @check_permission("message")
    def message(self, user: User, text: str = "привет"):
        """Команда отправки сообщения"""
        print(f"   Сообщение от {user.username}: '{text}'")


# Демонстрация работы системы
def demonstrate_access_control():
    """Функция демонстрации работы системы контроля доступа"""

    print("=" * 50)
    print("СИСТЕМА КОНТРОЛЯ ДОСТУПА К КОМАНДАМ")
    print("=" * 50)

    # Создаем пользователей
    admin = User("Alice", "admin")
    user = User("Bob", "user")

    # Создаем обработчик команд
    handler = CommandHandler()

    print(f"\n📋 Доступные команды:")
    print(f"   Администратор: {', '.join(ALLOWED_COMMANDS['admin'])}")
    print(f"   Пользователь:  {', '.join(ALLOWED_COMMANDS['user'])}")

    # Демонстрация работы от имени администратора
    print(f"\n👑 Действия администратора {admin}:")
    print("-" * 30)
    handler.start(admin)
    handler.ban(admin, "spammer123")
    handler.stop(admin)
    handler.message(admin, "Сервер на обслуживании")

    # Демонстрация работы от имени обычного пользователя
    print(f"\n👤 Действия пользователя {user}:")
    print("-" * 30)
    handler.start(user)
    handler.ban(user)  # Должно вызвать ошибку доступа
    handler.stop(user)  # Должно вызвать ошибку доступа
    handler.message(user, "Всем привет!")

    print(f"\n" + "=" * 50)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("=" * 50)


# Запуск демонстрации
if __name__ == "__main__":
    demonstrate_access_control()

    import time
    from datetime import datetime
    from functools import wraps


    class BankAccount:
        """Класс для демонстрации различных типов методов"""

        # Атрибут класса
        bank_name = "Python Bank"
        total_accounts = 0
        transaction_log = []

        def __init__(self, owner: str, balance: float = 0.0):
            self.owner = owner
            self._balance = balance  # Защищенный атрибут
            self.__account_number = self._generate_account_number()  # Приватный атрибут
            BankAccount.total_accounts += 1

        # Обычный метод экземпляра
        def deposit(self, amount: float):
            """Пополнение счета"""
            if amount > 0:
                self._balance += amount
                self._log_transaction(f"Пополнение: +{amount}")
                print(f"✅ {self.owner}: Счет пополнен на {amount} ₽")
            else:
                print(f"❌ {self.owner}: Неверная сумма для пополнения")
            return self._balance

        def withdraw(self, amount: float):
            """Снятие со счета"""
            if 0 < amount <= self._balance:
                self._balance -= amount
                self._log_transaction(f"Снятие: -{amount}")
                print(f"✅ {self.owner}: Со счета снято {amount} ₽")
            else:
                print(f"❌ {self.owner}: Недостаточно средств или неверная сумма")
            return self._balance

        # Приватный метод
        def _generate_account_number(self):
            """Генерация номера счета"""
            return f"ACC{1000 + BankAccount.total_accounts:04d}"

        # Защищенный метод
        def _log_transaction(self, description: str):
            """Логирование транзакции"""
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"{timestamp} | {self.owner} | {description} | Баланс: {self._balance} ₽"
            BankAccount.transaction_log.append(log_entry)

        # Метод класса
        @classmethod
        def from_string(cls, data: str):
            """Создание счета из строки (альтернативный конструктор)"""
            try:
                owner, balance = data.split(',')
                return cls(owner.strip(), float(balance.strip()))
            except ValueError:
                raise ValueError("Некорректный формат данных. Используйте: 'Имя, баланс'")

        @classmethod
        def get_bank_info(cls):
            """Получение информации о банке"""
            return {
                'bank_name': cls.bank_name,
                'total_accounts': cls.total_accounts,
                'all_owners': [acc.owner for acc in cls._get_all_accounts()]
            }

        @classmethod
        def _get_all_accounts(cls):
            """Вспомогательный метод класса (условно)"""
            # В реальной системе здесь был бы запрос к БД
            return []

        # Статический метод
        @staticmethod
        def validate_amount(amount):
            """Валидация суммы"""
            if isinstance(amount, (int, float)) and amount >= 0:
                return True
            return False

        @staticmethod
        def format_currency(amount: float):
            """Форматирование валюты"""
            return f"{amount:,.2f} ₽".replace(',', ' ')

        # Свойства (property)
        @property
        def balance(self):
            """Геттер для баланса"""
            return self._balance

        @property
        def account_number(self):
            """Геттер для номера счета"""
            return self.__account_number

        def __str__(self):
            return f"Счет {self.account_number}: {self.owner} - {self.format_currency(self.balance)}"


    # Декораторы для логирования и замера времени
    def log_operation(func):
        """Декоратор для логирования операций"""

        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"📝 Начало операции: {func.__name__}")
            print(f"   Аргументы: {args[1:] if args else 'нет'}")
            result = func(*args, **kwargs)
            print(f"✅ Операция {func.__name__} завершена")
            return result

        return wrapper


    def measure_time(func):
        """Декоратор для замера времени выполнения"""

        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"⏱️  Время выполнения {func.__name__}: {end_time - start_time:.4f} сек")
            return result

        return wrapper


    class EnhancedBankAccount(BankAccount):
        """Расширенный класс счета с декорированными методами"""

        @log_operation
        @measure_time
        def deposit(self, amount: float):
            """Пополнение счета с логированием и замером времени"""
            return super().deposit(amount)

        @log_operation
        @measure_time
        def withdraw(self, amount: float):
            """Снятие со счета с логированием и замером времени"""
            return super().withdraw(amount)

        # Декоратор с параметрами
        @staticmethod
        def require_min_balance(min_balance: float):
            """Декоратор для проверки минимального баланса"""

            def decorator(func):
                @wraps(func)
                def wrapper(self, *args, **kwargs):
                    if self.balance >= min_balance:
                        return func(self, *args, **kwargs)
                    else:
                        print(f"🚫 Операция '{func.__name__}' отклонена. Минимальный баланс: {min_balance} ₽")
                        return None

                return wrapper

            return decorator

        @require_min_balance(1000)
        def premium_withdraw(self, amount: float):
            """Снятие для премиум-клиентов (требует минимальный баланс)"""
            print(f"⭐ Премиальное снятие для {self.owner}")
            return self.withdraw(amount)


    # Демонстрация работы
    def demonstrate_methods_and_decorators():
        """Демонстрация различных типов методов и декораторов"""

        print("=" * 60)
        print("ДЕМОНСТРАЦИЯ МЕТОДОВ КЛАССА И ДЕКОРАТОРОВ")
        print("=" * 60)

        # 1. Создание счетов
        print("\n1. СОЗДАНИЕ СЧЕТОВ:")
        print("-" * 40)

        account1 = BankAccount("Иван Иванов", 5000)
        account2 = BankAccount("Мария Петрова", 3000)

        print(account1)
        print(account2)

        # 2. Использование методов экземпляра
        print("\n2. ОПЕРАЦИИ СО СЧЕТОМ:")
        print("-" * 40)

        account1.deposit(1500)
        account1.withdraw(800)
        account1.withdraw(10000)  # Недостаточно средств

        # 3. Метод класса (альтернативный конструктор)
        print("\n3. МЕТОД КЛАССА (конструктор из строки):")
        print("-" * 40)

        account3 = BankAccount.from_string("Алексей Сидоров, 7500")
        print(f"Создан счет: {account3}")

        # 4. Статический метод
        print("\n4. СТАТИЧЕСКИЙ МЕТОД:")
        print("-" * 40)

        amounts = [1000, -500, "текст", 2000.50]
        for amount in amounts:
            is_valid = BankAccount.validate_amount(amount)
            print(f"Сумма {amount}: {'валидна' if is_valid else 'невалидна'}")

        formatted = BankAccount.format_currency(1234567.89)
        print(f"Форматированная сумма: {formatted}")

        # 5. Информация о банке через метод класса
        print("\n5. ИНФОРМАЦИЯ О БАНКЕ:")
        print("-" * 40)

        bank_info = BankAccount.get_bank_info()
        for key, value in bank_info.items():
            print(f"{key}: {value}")

        # 6. Декорированные методы
        print("\n6. ДЕКОРИРОВАННЫЕ МЕТОДЫ:")
        print("-" * 40)

        enhanced_account = EnhancedBankAccount("Тестовый Клиент", 5000)
        enhanced_account.deposit(2000)
        enhanced_account.withdraw(1000)

        # 7. Декоратор с параметрами
        print("\n7. ДЕКОРАТОР С ПАРАМЕТРАМИ:")
        print("-" * 40)

        enhanced_account.premium_withdraw(500)  # Должно сработать
        enhanced_account.withdraw(4500)  # Опускаем баланс ниже 1000
        enhanced_account.premium_withdraw(100)  # Должно отказать

        print("\n" + "=" * 60)
        print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
        print("=" * 60)


    # Запуск демонстрации
    if __name__ == "__main__":
        demonstrate_methods_and_decorators()
        demonstrate_access_control()