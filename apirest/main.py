from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from SGE_bloc2.apirest.routers import users
#from fastapi.middleware.cors import CORSMiddleware

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

# Afegim les trucades als routers (carpeta routers)
app.include_router(users.router)