from fastapi import FastAPI

app = FastAPI(
    title="Nandani's micro service",
    summary="Says a hello to user"

)

# request type : GET,POST,PUT,DELETE,PATCH
@app.get("/") #root
async def index():
    return {"message":"Hi user the backend is up and running"}

@app.get("/say_my_name")
async def sayName():
    return {"name": "Nandani Thakur"}