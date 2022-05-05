#Python
from typing import Optional
from enum import Enum

#Pydantic
from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr
from email_validator import validate_email, EmailNotValidError

#FastAPI
from fastapi import FastAPI, Header, Query, UploadFile
from fastapi import status
from fastapi import HTTPException
from fastapi import Body, Query, Path, Form, Header, Cookie, UploadFile, File


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

class PersonBase(BaseModel):
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

class Person(PersonBase):
    password: str = Field(..., min_length=8)

class PersonOut(PersonBase):
    pass

class LoginOut(BaseModel):
    username : str = Field(...,
    max_length=20,
    example="user2021"
    )
    message : str = Field(
    default="Login Succesfully!"    
    )

@app.get(
    path="/",
    status_code=status.HTTP_200_OK
    ) #path operation decorator
def home(): #path operation function
    return {"First API": "Congratulations"} #JSON


# Request and Response Body
@app.post(
    path="/person/new", 
    response_model=PersonOut,
    status_code=status.HTTP_201_CREATED
    )
def create_person(person : Person = Body(...)):
    return person

# Validaciones : Query parameters

@app.get(
    path="/person/detail",
    status_code=status.HTTP_200_OK
    )
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

persons = [1,2,3,4,5]

@app.get(
    path="/person/detail/{person_id}",
    status_code=status.HTTP_200_OK
    )
def show_person(
    person_id: int = Path(
        ..., 
        gt=0,
        example=123,
        title="Person Id",
        description="This is the person identifier. It´s required")
):
    if person_id not in persons:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="¡This person doesn´t exist!"
        )

    return {person_id: "It exists!"}

# Validaciones: Request Body

@app.put(
    path="/person/{person_id}",
    status_code=status.HTTP_200_OK
    )
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

@app.post(
    path="/login",
    response_model=LoginOut,
    status_code=status.HTTP_200_OK
)
def login(username: str = Form(...), password: str = Form(...)):
    return LoginOut(username=username)

# Cookies and Headers Parameters

@app.post(
    path="/contact",
    status_code=status.HTTP_200_OK
)
def contact(
    first_name: str = Form(
        ...,
        max_length=20,
        min_length=1
    ),
    last_name: str = Form(
        ...,
        max_length=20,
        min_length=1
    ),
    email: EmailStr = Form(...),
    message: str = Form(
        ...,
        min_length=20
    ),
    user_agent: Optional[str] = Header(default=None),
    ads: Optional[str] = Cookie(default=None)
):
    return user_agent

# Files

@app.post(
    path="/post-image"
)
def post_image(
    image: UploadFile = File(...)
):
    return {
        "Filename": image.filename,
        "Format": image.content_type,
        "Size(kb)": round(len(image.file.read())/1024, ndigits=2)
    }