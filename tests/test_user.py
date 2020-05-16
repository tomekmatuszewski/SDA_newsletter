import pytest
from system.user import User


@pytest.fixture(name='user')
def create_user():
    user = User('Joe', 'Doe')
    return user


def test_user(user):
    assert user


def test_email(user):
    assert user.email == "joe.doe@gmail.com"


def test_create_user():
    user1 = User('John', 'Nowak')
    assert user1.first_name == "John"
    assert user1.email == "john.nowak@gmail.com"