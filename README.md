# goitneo-python-hw-1-group-8
Exercise 1:
It is simple function for displaying a list of colleagues who need to be congratulated on their birthdays this week.
Example of dictionary this function can work:
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
]

Exercise 2:
It is a virtual bot assistant that will recognise commands entered from the keyboard and respond according to the entered command. 

The bot accepts commands:

"hello" and responds to the console with the message "How can I help you?"

"add username phone". Following this command, the bot saves a new contact in its memory, for example, in the dictionary. The user enters the name username and the phone number phone, always separated by a space.

"change username phone". This command saves the new phone number phone for the contact username that already exists in the address book.  

"phone username" This command displays the phone number for the specified contact username in the console.

"all". This command displays all saved contacts with phone numbers in the console.

"close", "exit" with any of these commands, the bot terminates its work after it displays the message "Good bye!" in the console and completes its execution.
