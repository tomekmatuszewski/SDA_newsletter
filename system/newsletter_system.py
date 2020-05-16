from faker import Faker
from system.user import User


class NewsLetterSystem:

    def __init__(self, number_of_users):
        self.number_of_users = number_of_users
        self.list_of_users = []
        self.names = []
        self.add_users()

    def create_names(self):
        for _ in range(self.number_of_users):
            fake_name = Faker()
            first_name = fake_name.first_name()
            last_name = fake_name.last_name()
            self.names.append((first_name, last_name))

    def add_users(self):
        self.create_names()
        for name in self.names:
            user = User(name[0], name[1])
            self.list_of_users.append(user)

    def remove_user(self, index=None):
        if index:
            del self.list_of_users[index]
        else:
            self.list_of_users.pop()

    def send_email(self, message):
        messages = []
        for user in self.list_of_users:
            if user.is_active:
                messages.append((message, f"{user.email}"))
        return messages


    def show_messages(self, messages):
        print(f"Message: '{messages[0][0]}' sent to:")
        for message in messages:
            print(message[1])


if __name__ == '__main__':
    n = NewsLetterSystem(10)
    print(n.send_email())