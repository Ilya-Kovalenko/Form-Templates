import requests
import asyncio
import utils.validators
import unittest


class TestValidators(unittest.TestCase):
    def test_check_type_date_1(self):
        ret = asyncio.run(utils.validators.check_type("12.12.1999"))
        self.assertEqual(ret, "date")

    def test_check_type_date_2(self):
        ret = asyncio.run(utils.validators.check_type("1999-12-11"))
        self.assertEqual(ret, "date")

    def test_check_type_date_3(self):
        ret = asyncio.run(utils.validators.check_type("12.12.19991"))
        self.assertEqual(ret, "text")

    def test_check_type_date_4(self):
        ret = asyncio.run(utils.validators.check_type("19991-12-11"))
        self.assertEqual(ret, "text")

    def test_check_type_date_5(self):
        ret = asyncio.run(utils.validators.check_type("99.12.2000"))
        self.assertEqual(ret, "text")

    def test_check_type_date_6(self):
        ret = asyncio.run(utils.validators.check_type("10.32.2000"))
        self.assertEqual(ret, "text")

    def test_check_type_date_7(self):
        ret = asyncio.run(utils.validators.check_type("30.02.2000"))
        self.assertEqual(ret, "text")

    def test_check_type_email_1(self):
        ret = asyncio.run(utils.validators.check_type("test@mail.ru"))
        self.assertEqual(ret, "email")

    def test_check_type_email_2(self):
        ret = asyncio.run(utils.validators.check_type("@mail.ru"))
        self.assertEqual(ret, "text")

    def test_check_type_email_3(self):
        ret = asyncio.run(utils.validators.check_type("test@mail."))
        self.assertEqual(ret, "text")

    def test_check_type_email_4(self):
        ret = asyncio.run(utils.validators.check_type("test@.ru"))
        self.assertEqual(ret, "text")

    def test_check_type_phone_1(self):
        ret = asyncio.run(utils.validators.check_type("+79991112233"))
        self.assertEqual(ret, "phone")

    def test_check_type_phone_2(self):
        ret = asyncio.run(utils.validators.check_type("+79"))
        self.assertEqual(ret, "text")

    def test_check_type_phone_3(self):
        ret = asyncio.run(utils.validators.check_type("123+79991112233"))
        self.assertEqual(ret, "text")

    def test_check_type_phone_4(self):
        ret = asyncio.run(utils.validators.check_type("+79991112233111111111"))
        self.assertEqual(ret, "text")

    def test_check_type_text(self):
        ret = asyncio.run(utils.validators.check_type("sample text"))
        self.assertEqual(ret, "text")

class TestRequests(unittest.TestCase):
    def test_request_1(self):
        url = "http://localhost:8000/get_form?form=date_field=12.12.1999"
        response = requests.post(url)
        self.assertEqual(response.json(), {'form_name': 'Form template name'})

    def test_request_2(self):
        url = "http://localhost:8000/get_form?form=phone_field=%2B72221112233"
        response = requests.post(url)
        self.assertEqual(response.json(), {'form_name': 'Form template name'})

    def test_request_3(self):
        url = "http://localhost:8000/get_form?form=date_created=12.12.2000"
        response = requests.post(url)
        self.assertEqual(response.json(), {'form_names': ['form one', 'phone form', 'Text form']})

    def test_request_4(self):
        url = "http://localhost:8000/get_form?form=date_created=12.12.2000%26user_email=user@mail.ru"
        response = requests.post(url)
        self.assertEqual(response.json(), {'form_name': 'form one'})

    def test_request_5(self):
        url = "http://localhost:8000/get_form?form=date_created=12.12.2001f"
        response = requests.post(url)
        self.assertEqual(response.json(), {'date_created': 'text'})
