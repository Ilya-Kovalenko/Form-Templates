import re
from datetime import datetime


async def validate_form(form: str) -> dict:
    validated_form = await get_form_to_dict(form)
    normalized_form = await normalize_form(validated_form)

    return normalized_form


async def get_form_to_dict(form: str) -> dict:
    try:
        items = {}
        for part in form.split("&"):
            k, v = part.split("=")
            items.update([(k, v)])
        return items
    except:
        raise ValueError('Error while parsing data from POST request. '
                         'Make sure that the data in the request matches the format: f_name1=value1&f_name2=value2')


async def normalize_form(form: dict) -> dict:
    for key in form.keys():
        form[key] = await check_type(form[key])

    return form


async def check_type(x: str) -> str:
    if re.fullmatch(r'\d{2}.\d{2}.\d{4}', x) is not None:
        if await check_date(x):
            return 'date'
        else:
            return 'text'

    elif re.match(r'\d{4}-\d{2}-\d{2}', x) is not None:
        year, month, day = x.split('-')
        if await check_date(f"{day}.{month}.{year}"):
            return 'date'
        else:
            return 'text'

    elif re.fullmatch(r'\+7\d{10}', x) is not None:
        return 'phone'

    elif re.fullmatch(r'[\w.-]+@[\w-]+\.[\w.]+', x) is not None:
        return 'email'

    else:
        return 'text'


async def check_date(date: str) -> bool:
    try:
        datetime.strptime(date, '%d.%m.%Y')
        return True
    except ValueError:
        return False
