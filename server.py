import uvicorn
import asyncio
from fastapi import FastAPI
from utils.validators import validate_form
from utils.db_worker import find_form, migrate


app = FastAPI()


@app.post("/get_form")
async def read_item(form: str) -> dict:
    try:
        v_form = await validate_form(form)

        results = await find_form(v_form)

        return results

    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    asyncio.run(migrate())
    uvicorn.run(app, host="0.0.0.0", port=8000)
