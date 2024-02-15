import pytest
from src.user_util import user_format


@pytest.fixture
def user_fixture():
    return [{"title": 'Frontend-разработчик', "url": 'https://hh.ru/vac', "salary_from": 200000, "employer": 'ЭВА ПРОДАКТ', 'area': 'Новосибирск'}]

def test_user_format(user_fixture):
    vacancies = user_format(user_fixture)
    for vacancy in vacancies:
        expected_output = (
            f"\nНаименование вакансии: Frontend-разработчик\n"
            f"Ссылка на вакансию: https://hh.ru/vac\n"
            f"Зарплата (от): 200000\n"
            f"Работодатель: ЭВА ПРОДАКТ\n"
            f"Город: Новосибирск\n"
        )
        assert repr(vacancy) == expected_output