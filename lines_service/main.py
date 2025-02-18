from fastapi import FastAPI
import httpx

API_KEY = "0283d3b0c3fd42cca6c7db790e87fcac"
ENDPOINT_URL = "https://api-v3.mbta.com/"

app = FastAPI()

@app.get("/lines")
async def get_lines():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{ENDPOINT_URL}/lines?api_key={API_KEY}")
        response.raise_for_status()
        return response.json()

@app.get("/lines/{line_id}")
async def get_line(line_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{ENDPOINT_URL}/lines/{line_id}?api_key={API_KEY}")
        response.raise_for_status()
        return response.json()
