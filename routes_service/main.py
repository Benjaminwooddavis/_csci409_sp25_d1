from fastapi import FastAPI
import httpx

API_KEY = "0283d3b0c3fd42cca6c7db790e87fcac"
ENDPOINT_URL = "https://api-v3.mbta.com/"

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Routes Service"}

@app.get("/routes")
async def get_routes():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{ENDPOINT_URL}/routes?api_key={API_KEY}")
        response.raise_for_status()
        return response.json()

@app.get("/routes/{route_id}")
async def get_route(route_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{ENDPOINT_URL}/routes/{route_id}?api_key={API_KEY}")
        response.raise_for_status()
        return response.json()
