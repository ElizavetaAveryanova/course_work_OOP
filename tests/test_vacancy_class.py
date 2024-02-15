import pytest
from src.vacancy_class import Vacancy


@pytest.fixture
def vacancy_fixture():
    return Vacancy('Frontend-разработчик', 'https://hh.ru/vacancy/92484444', 200000, 'ЭВА ПРОДАКТ', 'Новосибирск')

def test___repr__(vacancy_fixture):
    expected_output = (
        f"\nНаименование вакансии: Frontend-разработчик\n"
        f"Ссылка на вакансию: https://hh.ru/vacancy/92484444\n"
        f"Зарплата (от): 200000\n"
        f"Работодатель: ЭВА ПРОДАКТ\n"
        f"Город: Новосибирск\n"
    )
    assert repr(vacancy_fixture) == expected_output

def test_is_valid_title_empty(vacancy_fixture):
    with pytest.raises(Exception):
        vacancy_fixture.title = ""

def test_is_valid_title_int(vacancy_fixture):
    with pytest.raises(Exception):
        vacancy_fixture.title = 5

def test_is_valid_url_int(vacancy_fixture):
    with pytest.raises(Exception):
        vacancy_fixture.url = 5

def test_is_valid_url_start(vacancy_fixture):
    with pytest.raises(Exception):
        vacancy_fixture.url = "url"

def test_is_valid_salary_str(vacancy_fixture):
    with pytest.raises(Exception):
        vacancy_fixture.salary = "abc"

def test_is_valid_employer_empty(vacancy_fixture):
    with pytest.raises(Exception):
        vacancy_fixture.employer = ""

def test_is_valid_employer_int(vacancy_fixture):
    with pytest.raises(Exception):
        vacancy_fixture.employer = 5

def test__gt__(vacancy_fixture):
    hh = Vacancy('разработ', 'https://hh.ru/vacancy/924', 200, 'ЭВА', 'Москва')
    assert vacancy_fixture.__gt__(hh) is True

def test__lt__(vacancy_fixture):
    hh = Vacancy('разработ', 'https://hh.ru/vacancy/924', 200, 'ЭВА', 'Москва')
    assert vacancy_fixture.__lt__(hh) is False