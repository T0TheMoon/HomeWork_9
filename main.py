phonebook = {}  # Створюємо пустий словник для зберігання контактів (імена - ключі, номери телефону - значення).

# Декоратор для обробки помилок введення користувача.
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"  # Повертаємо текст помилки, коли ключ не знайдено.
        except ValueError:
            return "Give me name and phone please"  # Повертаємо текст помилки, коли введено некоректні дані.
        except IndexError:
            return "Enter user name and phone number"  # Повертаємо текст помилки, коли не введено обов'язкові дані.
    return inner

# Декорована функція для додавання нового контакту.
@input_error
def add_contact(name, phone):
    if name in phonebook:
        raise ValueError  # Піднімаємо помилку, якщо контакт з таким ім'ям вже існує.
    phonebook[name] = phone
    return f"Contact {name} with phone {phone} has been added."  # Повідомляємо користувача про успішне додавання.

# Декорована функція для зміни номера телефону контакту.
@input_error
def change_phone(name, phone):
    if name not in phonebook:
        raise KeyError  # Піднімаємо помилку, якщо контакт з таким ім'ям не існує.
    else:  
        phonebook[name] = phone
        return f"Phone number for {name} has been changed to {phone}."  # Повідомляємо користувача про успішну зміну номера.

# Декорована функція для отримання номера телефону контакту.
@input_error
def get_phone(name):
    if name not in phonebook:
        raise KeyError  # Піднімаємо помилку, якщо контакт з таким ім'ям не існує.
    return f"{name}'s phone number is {phonebook[name]}."  # Повертаємо номер телефону контакту.

# Декорована функція для виведення всіх контактів.
@input_error
def show_all_contacts():
    if not phonebook:
        raise ValueError  # Піднімаємо помилку, якщо контактів немає.
    result = "Contacts:\n"
    for name, phone in phonebook.items():
        result += f"{name}: {phone}\n"
    return result  # Повертаємо список всіх контактів.

# Головна функція взаємодії з користувачем.
def main():
    while True:  # Безкінечний цикл для взаємодії з користувачем.
        user_input = input("Write command \t")  # Очікуємо введення команди від користувача.
        user_devided = user_input.split(maxsplit=2)  # Розділяємо введену команду на окремі частини (максимум 2).
        result_text = ""  # Змінна для зберігання результуючого тексту команди.

        for char in user_input:
            if char != " ":
                result_text += char.lower()  # Створюємо результуючий текст команди, видаляючи пробіли та перетворюючи все до нижнього регістру.
            else:
                break  # Зупиняємо цикл, якщо знайдено перший пробіл (пошук команди завершено).

        if result_text == "hello":
            print("How can I help you? \n")  # Виводимо вітання.
        elif result_text == 'add':
            if len(user_devided) < 3:
                print("Error: write name and phone.")  # Виводимо повідомлення про помилку, якщо введені дані неповні.
            else:
                print(add_contact(user_devided[1], user_devided[2]))  # Викликаємо функцію `add_contact`.
        elif result_text == 'change':
            if len(user_devided) < 3:
                print("Error: write name and phone.")  # Виводимо повідомлення про помилку, якщо введені дані неповні.
            else:
                print(change_phone(user_devided[1], user_devided[2]))  # Викликаємо функцію `change_phone`.
        elif result_text == 'phone':
            if len(user_devided) < 2:
                print("Error: write name.")  # Виводимо повідомлення про помилку, якщо не введено ім'я.
            else:
                print(get_phone(user_devided[1]))  # Викликаємо функцію `get_phone`.
        elif user_input.lower() == 'show all':
            print(show_all_contacts())  # Викликаємо функцію `show_all_contacts`.
        elif user_input.lower() in ["good bye", "close", "exit"]:
            print("Good bye!")  # Виводимо прощальне повідомлення.
            break  # Виходимо з безкінечного циклу.
        else:
            print("This is information about command: 'hello', 'add', 'change', 'phone', 'show all', 'good bye', 'close', or 'exit'")
            # Виводимо повідомлення про невідому команду, тобто показуємо які команди виконує бот.
# Виконуємо головну функцію, якщо цей файл запускається окремо.
if __name__ == '__main__':
    main()