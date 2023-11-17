import requests
import asyncio
import utils.validators


class TestValidators:
    @staticmethod
    def test_check_type_date_1():
        ret = asyncio.run(utils.validators.check_type("12.12.1999"))
        assert ret == "date"

    @staticmethod
    def test_check_type_date_2():
        ret = asyncio.run(utils.validators.check_type("1999-12-11"))
        assert ret == "date"

    @staticmethod
    def test_check_type_date_3():
        ret = asyncio.run(utils.validators.check_type("12.12.19991"))
        assert ret == "text"

    @staticmethod
    def test_check_type_date_4():
        ret = asyncio.run(utils.validators.check_type("19991-12-11"))
        assert ret == "text"

    @staticmethod
    def test_check_type_date_5():
        ret = asyncio.run(utils.validators.check_type("99.12.2000"))
        assert ret == "text"

    @staticmethod
    def test_check_type_date_6():
        ret = asyncio.run(utils.validators.check_type("10.32.2000"))
        assert ret == "text"

    @staticmethod
    def test_check_type_date_7():
        ret = asyncio.run(utils.validators.check_type("30.02.2000"))
        assert ret == "text"

    @staticmethod
    def test_check_type_email_1():
        ret = asyncio.run(utils.validators.check_type("test@mail.ru"))
        assert ret == "email"

    @staticmethod
    def test_check_type_email_2():
        ret = asyncio.run(utils.validators.check_type("@mail.ru"))
        assert ret == "text"

    @staticmethod
    def test_check_type_email_3():
        ret = asyncio.run(utils.validators.check_type("test@mail."))
        assert ret == "text"

    @staticmethod
    def test_check_type_email_4():
        ret = asyncio.run(utils.validators.check_type("test@.ru"))
        assert ret == "text"

    @staticmethod
    def test_check_type_phone_1():
        ret = asyncio.run(utils.validators.check_type("+79991112233"))
        assert ret == "phone"

    @staticmethod
    def test_check_type_phone_2():
        ret = asyncio.run(utils.validators.check_type("+79"))
        assert ret == "text"

    @staticmethod
    def test_check_type_phone_3():
        ret = asyncio.run(utils.validators.check_type("123+79991112233"))
        assert ret == "text"

    @staticmethod
    def test_check_type_phone_4():
        ret = asyncio.run(utils.validators.check_type("+79991112233111111111"))
        assert ret == "text"

    @staticmethod
    def test_check_type_text():
        ret = asyncio.run(utils.validators.check_type("sample text"))
        assert ret == "text"


def test_request_1():
    url = "http://localhost:8000/get_form?form=date_field=12.12.1999"
    response = requests.post(url)
    assert response.json() == {'form_name': 'Form template name'}


def test_request_2():
    url = "http://localhost:8000/get_form?form=phone_field=%2B72221112233"
    response = requests.post(url)
    assert response.json() == {'form_name': 'Form template name'}


def test_request_3():
    url = "http://localhost:8000/get_form?form=date_created=12.12.2000"
    response = requests.post(url)
    assert response.json() == {'form_names': ['form one', 'phone form', 'Text form']}


def test_request_4():
    url = "http://localhost:8000/get_form?form=date_created=12.12.2000%26user_email=user@mail.ru"
    response = requests.post(url)
    assert response.json() == {'form_name': 'form one'}


def test_request_5():
    url = "http://localhost:8000/get_form?form=date_created=12.12.2001f"
    response = requests.post(url)
    assert response.json() == {'date_created': 'text'}

