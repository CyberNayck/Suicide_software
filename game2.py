class Game:
    def __init__(self):
        self.is_running = True
        self.inventory = []
        self.location = 'village'  # Начальная локация

    def start(self):
        print("Добро пожаловать в мир приключений!")
        print("Вы находитесь в маленькой деревне, полной тайн и загадок.")
        self.main_loop()

    def main_loop(self):
        while self.is_running:
            if self.location == 'village':
                self.village()
            elif self.location == 'forest':
                self.forest()
            elif self.location == 'castle':
                self.castle()
            elif self.location == 'ending':
                self.end_game()
                self.is_running = False

    def village(self):
        print("\nВы находитесь в деревне. Здесь стоят красивые дома и веселятся люди.")
        print("1. Поговорить с местным фермером.")
        print("2. Идти в лес.")
        print("3. Отправиться к замку.")
        
        choice = input("Введите номер вашего выбора: ")

        if choice == '1':
            self.talk_to_farmer()
        elif choice == '2':
            self.location = 'forest'
        elif choice == '3':
            self.location = 'castle'
        else:
            print("Некорректный ввод. Попробуйте еще раз.")

    def talk_to_farmer(self):
        print("\nВы подошли к фермеру.")
        print("Фермер говорит: 'В нашем лесу завелся ужасный монстр. Пожалуйста, помогите нам!'")
        print("1. Согласиться помочь фермеру.")
        print("2. Уйти.")

        choice = input("Введите номер вашего выбора: ")

        if choice == '1':
            print("Фермер дал вам карту леса.")
            self.inventory.append("карта леса")
        elif choice == '2':
            print("Вы решили не помогать фермеру и ушли.")
        else:
            print("Некорректный ввод. Попробуйте еще раз.")

    def forest(self):
        print("\nВы находитесь в лесу. Повсюду слышен треск ветвей и шёпот древних деревьев.")
        if "карта леса" in self.inventory:
            print("У вас есть карта леса.")
        
        print("1. Исследовать глубже.")
        print("2. Вернуться в деревню.")
        print("3. Найти безопасное место для отдыха.")

        choice = input("Введите номер вашего выбора: ")

        if choice == '1':
            self.encounter_monster()
        elif choice == '2':
            self.location = 'village'
        elif choice == '3':
            print("Вы нашли безопасное место и смогли отдохнуть.")
            print("Ваши очки здоровья восстанавливаются!")
        else:
            print("Некорректный ввод. Попробуйте еще раз.")

    def encounter_monster(self):
        print("\nВы наткнулись на ужасного монстра!")
        print("1. Сразиться с монстром.")
        print("2. Попробовать убежать.")
        
        choice = input("Введите номер вашего выбора: ")
        
        if choice == '1':
            print("Вы смело сражаетесь, но монстр слишком силен...")
            self.location = 'ending'  # Умер при сражении
        elif choice == '2':
            print("Вы бежите и скрываетесь в безопасности.")
            self.location = 'village'  # Возвращение в деревню
        else:
            print("Некорректный ввод. Попробуйте еще раз.")

    def castle(self):
        print("\nВы подошли к замку. Он выглядит величественно и устрашающе.")

        print("Вы можете попробовать войти внутрь или обойти вокруг.")
        print("1. Войти в замок.")
        print("2. Обойти вокруг.")
        
        choice = input("Введите номер вашего выбора: ")

        if choice == '1':
            self.explore_castle()
        elif choice == '2':
            print("Вы обходите замок, находите секретный вход и попадаете внутрь!")
            self.explore_castle()
        else:
            print("Некорректный ввод. Попробуйте еще раз.")

    def explore_castle(self):
        print("\nВнутри замка темно и мрачно.")
        print("Вы слышите шёпот...")
        print("1. Исследовать зал тронов.")
        print("2. Вернуться обратно.")
        
        choice = input("Введите номер вашего выбора: ")

        if choice == '1':
            print("Вы обнаруживаете заколдованный трон!")
            print("1. Сесть на трон.")
            print("2. Оставить трон в покое.")
            
            throne_choice = input("Введите номер вашего выбора: ")

            if throne_choice == '1':
                self.location = 'ending'  # Конец игры — вы стали королём
            elif throne_choice == '2':
                print("Вы оставляете трон и продолжаете исследовать замок.")
            else:
                print("Некорректный ввод. Попробуйте еще раз.")
        elif choice == '2':
            self.location = 'castle'
        else:
            print("Некорректный ввод. Попробуйте еще раз.")

    def end_game(self):
        print("\nИгра окончена.")
        if "карта леса" in self.inventory:
            print("Вы вернулись в деревню с картой леса.")
        else:
            print("Вы покинули эту страну, так и не помогая местным жителям.")
        print("Спасибо за игру!")

# Начнем игру
if __name__ == "__main__":
    game = Game()
    game.start()
