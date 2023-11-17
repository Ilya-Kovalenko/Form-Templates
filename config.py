import os

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://root:example@mongo_db/?authMechanism=DEFAULT")

FORMS = [
        {
            "name": "form one",
            "username": "text",
            "password": "text",
            "user_email": "email",
            "user_phone": "phone",
            "date_created": "date"
        },
        {
            "name": "phone form",
            "username": "text",
            "mobile_phone": "phone",
            "home_phone": "phone",
            "work_phone": "phone",
            "date_created": "date"
        },
        {
            "name": "Form template name",
            "name_field": "text",
            "email_field": "email",
            "phone_field": "phone",
            "date_field": "date"
        },
        {
            "name": "Text form",
            "text1": "text",
            "text2": "text",
            "text3": "text",
            "date_created": "date"
        }
    ]
