import uvicorn
from fastapi import FastAPI
from routers.weather import weather

app = FastAPI()
app.include_router(weather)
if __name__ == "__main__":
    uvicorn.run("fastapi_code:app")
    
# run from command line: uvicorn --host 0.0.0.0 fastapi_code:app --reload