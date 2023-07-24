import datetime

# Функция для добавления нового блюда
def add_dish():
    dish_name = input("Введите название блюда: ")
    dish_calories = float(input("Введите количество калорий в блюде: "))

    today = datetime.date.today()
    filename = f"{today}.txt"

    # Проверяем существование файла
    try:
        with open(filename, 'a') as file:
            # Записываем название и калории нового блюда в файл
            file.write(f"{dish_name}:{dish_calories}\n")
    except FileNotFoundError:
        # Если файл не существует, создаем его и записываем название и калории нового блюда
        with open(filename, 'w') as file:
            file.write(f"{dish_name}:{dish_calories}\n")

    print("Блюдо добавлено успешно!")


# Функция для получения суммы калорий
def get_total_calories():
    today = datetime.date.today()
    filename = f"{today}.txt"

    try:
        with open(filename, 'r') as file:
            total_calories = 0
            for line in file:
                line_data = line.strip().split(':')
                dish_calories = float(line_data[1])
                total_calories += dish_calories
        print(f"Сумма калорий: {total_calories}")
    except FileNotFoundError:
        print("На сегодня еще не добавлено ни одного блюда.")


# Функция для вывода всех блюд и их калорий
def show_all_dishes():
    today = datetime.date.today()
    filename = f"{today}.txt"

    try:
        with open(filename, 'r') as file:
            data = file.readlines()
            if len(data) == 0:
                print("На сегодня еще не добавлено ни одного блюда.")
                return

            total_calories = 0
            print("Блюда за сегодня:")
            for line in data:
                line_data = line.strip().split(':')
                dish_name = line_data[0]
                dish_calories = float(line_data[1])
                print(f"{dish_name}: {dish_calories} калорий")
                total_calories += dish_calories

            print(f"Сумма калорий: {total_calories}")
    except FileNotFoundError:
        print("На сегодня еще не добавлено ни одного блюда.")


# Функция для отображения текстового меню
def show_menu():
    print("Меню:")
    print("1. Добавить новое блюдо")
    print("2. Узнать сумму калорий")
    print("3. Вывести все блюда за сегодня")
    print("0. Выход")


# Основной цикл программы
while True:
    show_menu()
    choice = input("Выберите пункт меню: ")

    if choice == '1':
        add_dish()
    elif choice == '2':
        get_total_calories()
    elif choice == '3':
        show_all_dishes()
    elif choice == '0':
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")
