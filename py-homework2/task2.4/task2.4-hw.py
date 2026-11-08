def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Контакт додано."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Контакт оновлено."
    else:
        return "Контакт не знайдено."

def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return "Контакт не знайдено."

def show_all(contacts):
    if not contacts:
        return "Контакт не збережено"
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    print("Вас вітає AsistentBot")
    
    while True:
        user_input = input("Введіть команду: ")
        if not user_input.strip():
            continue

        command, *args = parse_input(user_input)

        if command in ["закрити", "вихід"]:
            print("Гарного дня!")
            break
        elif command == "привіт":
            print("Як можу допомогти?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Невідома команда.")

if __name__ == "__main__":
    main()