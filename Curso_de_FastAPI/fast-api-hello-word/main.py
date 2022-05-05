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
    status_code=status.HTTP_200_OK,
    tags=["Home"]
    ) #path operation decorator
def home(): #path operation function
    return {"First API": "Congratulations"} #JSON


# Request and Response Body
@app.post(
    path="/person/new", 
    response_model=PersonOut,
    status_code=status.HTTP_201_CREATED,
    tags=["Persons"],
    summary="Create Person in the app"
    )
def create_person(person : Person = Body(...)):
    """
    Create Person
    
    This path operation creates a person in the app and save the informmation in the database

    Parameters:
    - Request body parameters:
        - **person: Person** -> A person model with first name, last name, age, hair, color and marital status

    Returns a person model with first name, last name, age, hair, color and marital status
    """
    return person

# Validaciones : Query parameters

@app.get(
    path="/person/detail",
    status_code=status.HTTP_200_OK,
    tags=["Persons"],
    deprecated=True
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
    """
    Show Person
    
   This route operation returns the name and age of a person in the application

    Parameters:
    - Request body parameters:
        - **name:** -> name of person
        - **age:** -> edad of person

    Returns the name and age of a person
    """
    return {name: age}

# Validaciones: Path Parameters

persons = [1,2,3,4,5]

@app.get(
    path="/person/detail/{person_id}",
    status_code=status.HTTP_200_OK,
    tags=["Persons"]
    )
def show_person(
    person_id: int = Path(
        ..., 
        gt=0,
        example=123,
        title="Person Id",
        description="This is the person identifier. It´s required")
):
    """
    Show Person ID
    
    This route operation returns an identifier and tells us if it is in the application

    Parameters:
    - Request body parameters:
        - **person_id** -> person identifier

    Returns the identifier and a validation message.
    """
    if person_id not in persons:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="¡This person doesn´t exist!"
        )

    return {person_id: "It exists!"}

# Validaciones: Request Body

@app.put(
    path="/person/{person_id}",
    status_code=status.HTTP_200_OK,
    tags=["Persons"]
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
    """
    Update Person
    
   This route operation returns an identifier and tells us if the identifier is found in the application

    Parameters:
    - Request body parameters:
        - **person_id:** -> "This is the person ID"
        - **person: Person** -> "A person model with first name, last name, age, hair, color and marital status"
        - **location: Location** -> "A person Location with city, state and country"

    Returns a model with first name, last name, age, hair, color, marital status, city, state and country
    """
    results = person.dict()
    results.update(location.dict())
    return results

@app.post(
    path="/login",
    response_model=LoginOut,
    status_code=status.HTTP_200_OK,
    tags=["Persons"]
)
def login(username: str = Form(...), password: str = Form(...)):
    """
    Login
    
    This route operation authenticates a user to the system

    Parameters:
    - Request body parameters:
        - **username:** -> authentication user
        - **password:** -> Authentication key

    Returns el username y password 
    """
    return LoginOut(username=username)

# Cookies and Headers Parameters

@app.post(
    path="/contact",
    status_code=status.HTTP_200_OK,
    tags=["contacts"]
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
    """
    Contact
    
    This route operation authenticates a user to the system

    Parameters:
    - Request body parameters:
        - **first_name:** -> first_name of person
        - **last_name:** -> last_name of person
        - **email:** -> email of person
        - **message:** -> message of person
        - **user_agent:** -> user_agent of person
        - **ads:** -> ads of person

   Returns customer information
    """
    return user_agent

# Files

@app.post(
    path="/post-image",
    tags=["posts"]
)
def post_image(
    image: UploadFile = File(...)
):
    """
    Post Image
    
    This path operation displays information from the attached file.

    Parameters:
    - Request body parameters:
        - **image:** -> image .jpg or png to attach

    Returns Filename, Format and Size of the file
    """
    return {
        "Filename": image.filename,
        "Format": image.content_type,
        "Size(kb)": round(len(image.file.read())/1024, ndigits=2)
    }