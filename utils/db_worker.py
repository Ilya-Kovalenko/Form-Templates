from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGODB_URL, FORMS


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

    db_forms = await mongo_client.form_templates.find({}).to_list(length=100)

    for el in db_forms:
        el.pop("_id")

    if db_forms == FORMS:
        return

    await mongo_client.form_templates.delete_many({})

    for form in FORMS:
        await mongo_client.form_templates.insert_one(form)
