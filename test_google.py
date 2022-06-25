import pytest

# scope='function' значение по умолчанию, можно не прописывать
# scope='session' вызов в каждую сессию (1 запуск тестов == 1 сессия)

# positive test
def test_first(before_each):
    assert 1 == 1


# падающий тест, через запятую можно передать сообщение, кот выведется в логах
def test_second(before_each):
    assert 1 == 2, "Ошибочка"


# фикстуры
# @pytest.fixture() - декоратор
@pytest.fixture(scope='function')
def before_each(request):
    print("Called before each test " + request.node.name)


@pytest.fixture(scope='session', autouse=True)
def before_all(request):
    print("Called before all test " + request.node.name)


def test_third(before_each):
    assert 2 == 2


def test_fourth(message):
    assert "message" in message


# фикстура перед тестами
@pytest.fixture()
def client():
    client = 1234
    print("Подготовка клиента")
    return client


# фикстура после тестов
@pytest.fixture()
def manager():
    manager = 1234
    print("Подготовка менеджера")
    yield manager
    print("Удаление менеджера")


def test_manager(manager):
    assert manager == 1234



