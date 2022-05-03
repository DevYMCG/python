#Python
from lib2to3.pytree import Base
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI, Query
from fastapi import Body, Query, Path

app = FastAPI()

# Models
class Location(BaseModel):
    city: str
    state: str
    country: str

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None


@app.get("/") #path operation decorator
def home(): #path operation function
    return {"First API": "Congratulations"} #JSON


# Request and Response Body
@app.post("/person/new")
def create_person(person : Person = Body(...)):
    return person

# Validaciones : Query parameters

@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        None, 
        min_length=1,
        max_length=50,
        title="Person Name",
        description="This is the person name. It´s between a and 50 characters"
        ), 
    age: str = Query(
        ...,
        title="Person Age",
        description="This is the person age. It´s required"
        ) 
):
    return {name: age}

# Validaciones: Path Parameters

@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ..., 
        gt=0,
        title="Person Id",
        description="This is the person identifier. It´s required")
):
    return {person_id: "It exists!"}

# Validaciones: Request Body

@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        title="Person ID",
        description="This is the person ID",
        gt = 0
    ),
    person : Person = Body(...),
    location: Location = Body(...)
):
    results = person.dict()
    results.update(location.dict())
    return results