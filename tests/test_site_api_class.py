import pytest
from src.site_api_class import HeadHunterAPI


@pytest.fixture
def hh_fixture():
    return {'items': [{'id': '92484444', 'premium': False, 'name': 'Frontend-разработчик', 'department': None, 'has_test': False, 'response_letter_required': False, 'area': {'id': '4', 'name': 'Новосибирск', 'url': 'https://api.hh.ru/areas/4'}, 'salary': {'from': 200000, 'to': 250000, 'currency': 'RUR', 'gross': False}, 'type': {'id': 'open', 'name': 'Открытая'}, 'address': None, 'response_url': None, 'sort_point_distance': None, 'published_at': '2024-01-31T18:30:59+0300', 'created_at': '2024-01-31T18:30:59+0300', 'archived': False, 'apply_alternate_url': 'https://hh.ru/applicant/vacancy_response?vacancyId=92484444', 'insider_interview': None, 'url': 'https://api.hh.ru/vacancies/92484444?host=hh.ru', 'alternate_url': 'https://hh.ru/vacancy/92484444', 'relations': [], 'employer': {'id': '10307188', 'name': 'ЭВА ПРОДАКТ', 'url': 'https://api.hh.ru/employers/10307188', 'alternate_url': 'https://hh.ru/employer/10307188', 'logo_urls': None, 'vacancies_url': 'https://api.hh.ru/vacancies?employer_id=10307188', 'accredited_it_employer': False, 'trusted': True}, 'snippet': {'requirement': 'Релевантный опыт по специальности не менее 2 лет. Отличного владения Type/JavaScript, Angular. Знание библиотеки RxJs. Отличного владения HTML5...', 'responsibility': 'Принимать участие в командной работе над приложением с использованием Angular, RxJS, Type/JavaScript, HTML5/CSS3. Поддержка сайта компании.'}, 'contacts': None, 'schedule': {'id': 'fullDay', 'name': 'Полный день'}, 'working_days': [], 'working_time_intervals': [], 'working_time_modes': [], 'accept_temporary': True, 'professional_roles': [{'id': '96', 'name': 'Программист, разработчик'}], 'accept_incomplete_resumes': False, 'experience': {'id': 'between3And6', 'name': 'От 3 до 6 лет'}, 'employment': {'id': 'full', 'name': 'Полная занятость'}}]}

def test_get_vacancies():
    hh = HeadHunterAPI()
    assert type(hh.get_vacancies("разработчик")) == dict

def test_clean_vacancies(hh_fixture):
    hh = HeadHunterAPI()
    assert hh.clean_vacancies(hh_fixture) == [{'title': 'Frontend-разработчик', 'url': 'https://hh.ru/vacancy/92484444', 'salary_from': 200000, 'employer': 'ЭВА ПРОДАКТ', 'area': 'Новосибирск'}]