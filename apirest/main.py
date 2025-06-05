from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
from services import user
import os

# 4. Crear l'aplicació FastAPI
app = FastAPI()
'''
Afegim el CORS per a que la tecnologia que s'utilitzi al 
frontend pugui fer consultes als endpoints de la APIREST
'''
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1. Carregar variables d'entorn
load_dotenv()

# 2. Configurar la connexió a PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL")  # Obtenir la URL de connexió des de .env
engine = create_engine(DATABASE_URL)      # Crear l'engine de connexió

# 3. Crear les taules a la base de dades
SQLModel.metadata.create_all(engine)

# 5. Dependència per obtenir la sessió de la base de dades
def get_db():
    db = Session(engine)
    try:
        yield db
    finally:
        db.close()

"""@app.get("/user/new", response_model=list[dict])
async def new_user():
    return{"Message":"Add user succesfully"}"""


# 6. Endpoint per afegir usuaris
@app.post("/users/create/", response_model=dict, tags=["USUARIS"])
async def create_user(name: str, email:str, age:int, db:Session = Depends(get_db)):
    result = user.add_new_user(name, email, age, db)
    return result

# 7. Endpoint per llegir usuaris
@app.get("/users/read/", response_model= list[dict], tags=["USUARIS"])
async def read_user(db:Session = Depends(get_db)):
    result = user.get_all_users(db)
    return result

@app.put("/user/update/", response_model= dict, tags=["USUARIS"])
async def update_user(id:int,name: str, db:Session = Depends(get_db)):
    result = user.update_user(id, name, db)
    return result

@app.delete("/user/delete/{userId}", response_model=dict, tags=["USUARIS"])
async def delete_user(userId:int, db:Session = Depends(get_db)):
    result = user.delete_user(userId, db)
    return result


@app.get("/users/get", response_model= list[dict])
async def find_users():
    result = user.get_users()
    return result













