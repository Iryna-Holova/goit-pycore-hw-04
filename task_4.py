"""
Task 4. Phonebook
"""


def parse_input(user_input: str) -> tuple:
    """
    Parses the user input string and returns a tuple containing the command
    and any arguments.

    Args:
        user_input (str): The user input string to be parsed.

    Returns:
        tuple: A tuple containing the command and any arguments. The command
        is a lowercase string without leading or trailing whitespace. The
        arguments are a tuple of strings.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args: list, contacts: dict) -> str:
    """
    Adds a contact to the `contacts` dictionary if the name is not already in
    the dictionary.

    Args:
        args (list): A list containing the name and phone number of the
        contact.
        contacts (dict): A dictionary containing existing contacts.

    Returns:
        str: A message indicating whether the contact was added or if it
        already exists. If the input is invalid, a message indicating an
        invalid input is returned.
    """
    try:
        name, phone = args
        if name in contacts:
            return "Contact already exists."
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "Invalid input. Please provide name and phone number."


def change_contact(args: list, contacts: dict) -> str:
    """
    Changes the phone number of a contact in the `contacts` dictionary if the
    name is in the dictionary.

    Args:
        args (list): A list containing the name and new phone number of the
        contact.
        contacts (dict): A dictionary containing existing contacts.

    Returns:
        str: A message indicating whether the contact was changed or if it
        does not exist. If the input is invalid, a message indicating an
        invalid input is returned.
    """
    try:
        name, new_phone = args
        if name not in contacts:
            return "Contact does not exist."
        contacts[name] = new_phone
        return "Contact updated."
    except ValueError:
        return "Invalid input. Please provide name and new phone number."


def get_phone(args: list, contacts: dict) -> str:
    """
    Returns the phone number of a contact in the `contacts` dictionary if the
    name is in the dictionary.

    Args:
        args (list): A list containing the name of the contact.
        contacts (dict): A dictionary containing existing contacts.

    Returns:
        str: The phone number of the contact if it is in the dictionary.
        If the name is not in the dictionary, a message indicating that the
        contact does not exist is returned.
    """
    try:
        name = args[0]
        if name in contacts:
            return contacts[name]
        return "Contact does not exist."
    except IndexError:
        return "Invalid input. Please provide name."


def get_contacts(contacts: dict) -> str:
    """
    Returns a string containing the names and phone numbers of all contacts
    in the `contacts` dictionary.

    Args:
        contacts (dict): A dictionary containing existing contacts.

    Returns:
        str: A string containing the names and phone numbers of all contacts
        in the dictionary. If the dictionary is empty, a message indicating
        that there are no contacts is returned.
    """
    if not contacts:
        return "There are no contacts."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main() -> None:
    """
    The main function of the program.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if not user_input:
            print("Please enter a command.")
            continue

        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(get_contacts(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
