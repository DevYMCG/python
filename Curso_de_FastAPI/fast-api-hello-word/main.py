#Python
from lib2to3.pytree import Base
from typing import List, Optional
from enum import Enum

#Pydantic
from pydantic import BaseModel, EmailStr
from pydantic import Field

#FastAPI
from fastapi import FastAPI, Query
from fastapi import Body, Query, Path

# email - validators
from email_validator import validate_email, EmailNotValidError

app = FastAPI()

# Models
class HairColor(Enum):
    white= "white"
    brown = "brown"
    black = "black"
    blonde = "blonde"
    red = "red"

class Location(BaseModel):
    city: str = Field(
        ..., 
        min_length=1,
        max_length=30
        )
    state: str= Field(
        ..., 
        min_length=1,
        max_length=30
        )
    country: str = Field(
        ..., 
        min_length=1,
        max_length=30
        )

class Person(BaseModel):
    first_name: str = Field(
        ..., 
        min_length=1,
        max_length=50
        )
    last_name: str = Field(
        ..., 
        min_length=1,
        max_length=50
        )
    age: int = Field(
        ...,
        gt=0,
        le=115
    )
    email: EmailStr = Field(
        ...
        ) 
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)


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
        description="This is the person name. It´s between a and 50 characters",
        example="Rocio"
        ), 
    age: str = Query(
        ...,
        title="Person Age",
        description="This is the person age. It´s required",
        example=25
        ) 
):
    return {name: age}

# Validaciones: Path Parameters

@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ..., 
        gt=0,
        example=123,
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
        gt = 0,
        example=123
    ),
    person : Person = Body(...),
    location: Location = Body(...)
):
    results = person.dict()
    results.update(location.dict())
    return results