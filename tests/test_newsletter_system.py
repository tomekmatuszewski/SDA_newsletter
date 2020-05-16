from system.newsletter_system import NewsLetterSystem
import pytest

@pytest.fixture(name = 'system')
def create_system():
    system = NewsLetterSystem(10)
    return system

def test_newsletter_system(system):
    assert system

def test_create_names(system):
    assert len(system.names) == 10
    assert type(system.names[0]) is tuple

def test_add_users(system):
    assert len(system.list_of_users) == 10

def test_remove_user(system):
    system.remove_user()
    assert len(system.list_of_users) == 9

def test_remove_user_with_index(system):
    system.remove_user(8)
    assert len(system.list_of_users) == 9

def test_email(system):
    assert len(system.send_email("message")) == 10

def test_emial_marks(system):
    assert '@' and '.' in system.send_email("message")[0][1]
    assert '@' and '.' in system.send_email("message")[5][1]
