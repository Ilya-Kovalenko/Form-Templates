from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://root:example@mongo_db/?authMechanism=DEFAULT")


async def find_form(form: dict) -> dict:
    mongo_client = AsyncIOMotorClient(MONGODB_URL)["base"]
    cursor = mongo_client.form_templates.find(form)

    results = []
    for document in await cursor.to_list(length=100):
        results.append(document["name"])

    if not results:
        return form
    elif len(results) == 1:
        return {"form_name": results[0]}
    else:
        return {"form_names": results}


async def migrate() -> None:
    mongo_client = AsyncIOMotorClient(MONGODB_URL)["base"]

    if await mongo_client.form_templates.find({}).to_list(length=100) != []:
        return

    forms = [
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

    for form in forms:
        await mongo_client.form_templates.insert_one(form)
