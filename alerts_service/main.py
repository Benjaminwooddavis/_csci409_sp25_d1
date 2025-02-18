from fastapi import FastAPI, Depends
import httpx

API_KEY = "0283d3b0c3fd42cca6c7db790e87fcac"
ENDPOINT_URL = "https://api-v3.mbta.com/"

app = FastAPI()

async def get_alerts():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{ENDPOINT_URL}/alerts?api_key={API_KEY}")
        response.raise_for_status()
        return response.json()

@app.get("/alerts")
async def read_alerts(alerts=Depends(get_alerts)):
    return alerts

@app.get("/alerts/{alert_id}")
async def read_alert(alert_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{ENDPOINT_URL}/alerts/{alert_id}?api_key={API_KEY}")
        response.raise_for_status()
        return response.json()
