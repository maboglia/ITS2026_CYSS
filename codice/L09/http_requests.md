Gestire le HTTP request in Python è una delle attività più comuni, e puoi farlo a diversi livelli: da semplici chiamate client (tipo “consumo API”) fino alla creazione di un server web.




---


🔹 1. Fare HTTP request (client) con Python


Il modo più semplice è usare la libreria Requests.


📦 Installazione


pip install requests


📥 GET request


import requests


response = requests.get("https://api.github.com")


print(response.status_code)
print(response.text)


📤 POST request


import requests


data = {
    "username": "mario",
    "password": "1234"
}


response = requests.post("https://example.com/login", json=data)


print(response.status_code)
print(response.json())


📌 Altri esempi utili


Parametri URL


params = {"q": "python"}
response = requests.get("https://www.google.com/search", params=params)


Headers


headers = {"Authorization": "Bearer TOKEN"}
response = requests.get("https://api.example.com/data", headers=headers)


Timeout


response = requests.get("https://api.example.com", timeout=5)




---


🔹 2. Gestione errori


try:
    response = requests.get("https://api.example.com")
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print("Errore HTTP:", e)
except requests.exceptions.RequestException as e:
    print("Errore generico:", e)




---


🔹 3. Creare un server HTTP in Python


Se invece vuoi gestire richieste in ingresso (backend), puoi usare framework come:


⚡ Base: Flask


pip install flask


Esempio base


from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/hello", methods=["GET"])
def hello():
    return "Ciao!"


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    return jsonify({"message": f"Benvenuto {username}"})


app.run(debug=True)




---


🚀 Più moderno: FastAPI


Molto veloce e perfetto per API REST.


pip install fastapi uvicorn


Esempio


from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello World"}


Avvio:


uvicorn main:app --reload




---


🔹 4. Differenza chiave


Caso	Libreria


Fare richieste HTTP (client)	Requests
Creare API / server	Flask / FastAPI






---


🔹 5. Caso reale completo


👉 Consumo API + logica


import requests


def get_users():
    url = "https://jsonplaceholder.typicode.com/users"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Errore:", e)
        return []


users = get_users()


for u in users:
    print(u["name"])




---


💡 Consiglio pratico


Usa Requests → script, integrazioni, ETL


Usa FastAPI → microservizi moderni


Usa Flask → progetti semplici o didattici






---


## esempio stile Spring Boot ma in Python, con struttura a livelli:


👉 Controller → Service → Repository (DAO) → Model → DTO → Mapper


Useremo FastAPI perché è quello che più si avvicina al modello REST moderno.




---


📁 Struttura progetto


project/
│
├── main.py
├── models.py
├── schemas.py      # DTO
├── repository.py   # DAO
├── service.py
└── mapper.py




---


🔹 1. MODEL (Entity)


# models.py


class User:
    def __init__(self, id: int, username: str, email: str):
        self.id = id
        self.username = username
        self.email = email




---


🔹 2. DTO (Schemas)


# schemas.py


from pydantic import BaseModel


class UserDTO(BaseModel):
    id: int
    username: str
    email: str


class UserCreateDTO(BaseModel):
    username: str
    email: str


👉 Equivalente a @DTO in Spring




---


🔹 3. MAPPER


# mapper.py


from models import User
from schemas import UserDTO


def to_dto(user: User) -> UserDTO:
    return UserDTO(
        id=user.id,
        username=user.username,
        email=user.email
    )




---


🔹 4. REPOSITORY (DAO)


# repository.py


from models import User


class UserRepository:


    def __init__(self):
        self.users = []
        self.counter = 1


    def find_all(self):
        return self.users


    def save(self, user: User):
        user.id = self.counter
        self.counter += 1
        self.users.append(user)
        return user


👉 Simula un database (come JpaRepository)




---


🔹 5. SERVICE


# service.py


from repository import UserRepository
from models import User


class UserService:


    def __init__(self, repo: UserRepository):
        self.repo = repo


    def get_all_users(self):
        return self.repo.find_all()


    def create_user(self, username: str, email: str):
        user = User(id=0, username=username, email=email)
        return self.repo.save(user)


👉 Qui metti la business logic (come @Service)




---


🔹 6. CONTROLLER


# main.py


from fastapi import FastAPI
from schemas import UserDTO, UserCreateDTO
from repository import UserRepository
from service import UserService
from mapper import to_dto


app = FastAPI()


repo = UserRepository()
service = UserService(repo)


@app.get("/users", response_model=list[UserDTO])
def get_users():
    users = service.get_all_users()
    return [to_dto(u) for u in users]


@app.post("/users", response_model=UserDTO)
def create_user(user: UserCreateDTO):
    saved = service.create_user(user.username, user.email)
    return to_dto(saved)




---


🔥 Mapping con Spring Boot


Spring Boot	Python


@RestController	FastAPI routes
@Service	Service class
@Repository	Repository class
@Entity	Model
DTO	Pydantic schema
@Autowired	Dependency injection manuale






---


🚀 Avvio


uvicorn main:app --reload


Vai su: 👉 http://127.0.0.1:8000/docs (Swagger automatico)




---


💡 Migliorie “enterprise” (come Spring)


Se vuoi avvicinarti ancora di più a Spring Boot puoi aggiungere:


✔ Dependency Injection vera (FastAPI Depends)


✔ Database con SQLAlchemy


✔ Pattern Facade


✔ Validazione avanzata


✔ Autenticazione JWT


✔ Logging strutturato


