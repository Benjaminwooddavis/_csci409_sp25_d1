from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import httpx

API_KEY = "0283d3b0c3fd42cca6c7db790e87fcac"
ENDPOINT_URL = "https://api-v3.mbta.com/"

app = FastAPI()

# OAuth2 scheme for token-based authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Dummy function to verify token (In production, use a real verification process)
def get_current_user(token: str = Depends(oauth2_scheme)):
    if token != "valid_token":  # Replace with real token validation
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return {"username": "test_user"}  # Example user

@app.get("/")
def read_root():
    return {"message": "Routes Service"}

@app.get("/routes", dependencies=[Depends(get_current_user)])
async def get_routes():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{ENDPOINT_URL}/routes?api_key={API_KEY}")
        response.raise_for_status()
        return response.json()

@app.get("/routes/{route_id}", dependencies=[Depends(get_current_user)])
async def get_route(route_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{ENDPOINT_URL}/routes/{route_id}?api_key={API_KEY}")
        response.raise_for_status()
        return response.json()

