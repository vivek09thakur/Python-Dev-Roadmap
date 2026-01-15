from fastapi import FastAPI
from fastapi.responses import HTMLResponse

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

@app.get("/home_page")
async def serveHomePage():
    return HTMLResponse("""
<html>
    <body>
        <h1>This is a home page</h1><br/>
        <p> welcome user</p>
    </body>
</html>
""")