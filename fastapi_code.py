import uvicorn
from fastapi import FastAPI
from routers.weather import weather
from routers.photo import photo

app = FastAPI()
app.include_router(weather)
app.include_router(photo)
if __name__ == "__main__":
    uvicorn.run("fastapi_code:app")
    
# run from command line: uvicorn --host 0.0.0.0 fastapi_code:app --reload