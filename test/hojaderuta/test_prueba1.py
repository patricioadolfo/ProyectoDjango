import pytest

@pytest.mark.skip(reason= "marca para ignorar test")
def test_prueba():

    assert 2 == 1

@pytest.mark.prueba
def test_prueba2():

    assert 1 == 1

@pytest.fixture(scope = 'session')
def fixture_1():

    print('se ejecuta al comienzo')

    yield 1

    print('se ejecuta al final')

@pytest.mark.prueba
def test_prueba3(fixture_1):

    print('desde mi test_3')

    variable = fixture_1

    assert variable == 1


@pytest.mark.prueba
def test_prueba4(fixture_1):

    print('desde mi test_4')

    variable = fixture_1

    assert variable == 1


