class Game:
    def __init__(self):
        self.is_running = True
        self.inventory = []
        self.location = 'start'

    def start(self):
        print("Вы оказались в заброшенном доме. Снаружи бушует буря, и у вас нет возможности уйти.")
        print("Ваше сердце стучит, страх охватывает вас.")
        self.main_loop()

    def main_loop(self):
        while self.is_running:
            if self.location == 'start':
                self.start_location()
            elif self.location == 'living_room':
                self.living_room()
            elif self.location == 'hallway':
                self.hallway()
            elif self.location == 'kitchen':
                self.kitchen()
            elif self.location == 'basement':
                self.basement()
            elif self.location == 'attic':
                self.attic()
            elif self.location == 'ending':
                self.end_game()
                self.is_running = False

    def start_location(self):
        print("\nВы находитесь в начальной комнате.")
        print("Что вы хотите сделать?")
        print("1. Исследовать комнату")
        print("2. Проверить двери")

        choice = input("Введите номер вашего выбора: ")

        if choice == '1':
            self.location = 'living_room'
        elif choice == '2':
            print("Вы проверяете двери, но они все заперты. Внезапно слышите шаги позади...")
        else:
            print("Некорректный ввод. Попробуйте еще раз.")

    def living_room(self):
        print("\nВы вошли в гостиную. В комнате много старой мебели.")
        print("На столе вы видите вещь.")
        print("Что вы хотите сделать?")
        print("1. Осмотреть стол")
        print("2. Выйти в коридор")

        choice = input("Введите номер вашего выбора: ")

        if choice == '1':
            print("Вы нашли ключ! Он может открыть двери.")
            self.inventory.append("ключ")
        elif choice == '2':
            self.location = 'hallway'
        else:
            print("Некорректный ввод. Попробуйте еще раз.")

    def hallway(self):
        print("\nВы находитесь в коридоре. Мрак окружает вас, и слышен шёпот.")
        print("В конце коридора две двери.")
        print("Что вы хотите сделать?")
        print("1. Открыть дверь влево (к кухне)")
        print("2. Открыть дверь вправо (в подвал)")
        print("3. Подняться на чердак")
        print("4. Вернуться в гостиную")

        choice = input("Введите номер вашего выбора: ")

        if choice == '1':
            self.location = 'kitchen'
        elif choice == '2':
            self.location = 'basement'
        elif choice == '3':
            self.location = 'attic'
        elif choice == '4':
            self.location = 'living_room'
        else:
            print("Некорректный ввод. Попробуйте еще раз.")

    def kitchen(self):
        print("\nВы вошли на кухню. Вокруг много старой утвари.")
        print("На столе лежит кровавый нож.")
        print("Что вы хотите сделать?")
        print("1. Взять нож")
        print("2. Вернуться в коридор")

        choice = input("Введите номер вашего выбора: ")

        if choice == '1':
            print("Вы взяли нож. Теперь у вас есть средство защиты!")
            self.inventory.append("нож")
        elif choice == '2':
            self.location = 'hallway'
        else:

            print("Некорректный ввод. Попробуйте еще раз.")

    def basement(self):
        print("\nВы спустились в подвал. В темноте слышен шум.")
        print("На столе лежит старая фотография с изображением семьи.")
        print("Что вы хотите сделать?")
        print("1. Осмотреть фотографию")
        print("2. Вернуться в коридор")

        choice = input("Введите номер вашего выбора: ")

        if choice == '1':
            print("Вы видите, что на фотографии кто-то из семьи выглядит очень злым...")
            self.inventory.append("фотография")
        elif choice == '2':
            self.location = 'hallway'
        else:
            print("Некорректный ввод. Попробуйте еще раз.")

    def attic(self):
        print("\nВы поднялись на чердак. Здесь очень темно и пыльно.")
        print("Слышится шёпот и ветер. На полу вы видите старый дневник.")
        print("Что вы хотите сделать?")
        print("1. Открыть дневник")
        print("2. Вернуться в коридор")

        choice = input("Введите номер вашего выбора: ")

        if choice == '1':
            print("Вы открываете дневник и читаете о трагических событиях, произошедших в этом доме.")
            self.location = 'ending'  # Конец игры с одной из возможных концовок
        elif choice == '2':
            self.location = 'hallway'
        else:
            print("Некорректный ввод. Попробуйте еще раз.")

    def end_game(self):
        print("\nВы узнали о ужасных событиях прошлого, и ваши страхи стали реальностью.")
        print("Вы навсегда останетесь в этом доме. Конец игры.")

# Начнем игру
if __name__ == "__main__":
    game = Game()
    game.start()

