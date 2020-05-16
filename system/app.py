from system.newsletter_system import NewsLetterSystem

number_of_users = int(input("Enter number of users: "))
system = NewsLetterSystem(number_of_users)

while True:
    message = input("Enter message: ")
    messages = system.send_email(message)
    system.show_messages(messages)
    next_message = input("Do you want to sent next message [Y/N]")
    if next_message == "Y":
        continue
    else:
        break



