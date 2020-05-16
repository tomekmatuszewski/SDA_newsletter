class User:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name
        self.is_active = True


    @property
    def email(self):
        return f'{self.first_name.lower()}.{self.last_name.lower()}@gmail.com'

    @classmethod
    def create_user(cls, first_name, last_name):
        return cls(first_name, last_name)

