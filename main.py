from fastapi import FastAPI
import asyncio




app = FastAPI()

@app.get("/")
async def read_root():
    await asyncio.sleep(0)
    return {"Hello": "World"}

