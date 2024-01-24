from datetime import date
from fastapi import FastAPI, HTTPException, Depends, Query
from databases import Database
from sqlalchemy import select
from models import author

app = FastAPI()

@app.post("/author/")
async def create_author(firstName: str, lastName: str, bio: str, birthDate: date = None):
    query = author.insert().values(firstName=firstName, lastName=lastName, bio=bio, birthDate=birthDate)
    await Database.execute(query)

    author_dict = {
        "authorName": firstName + " " + lastName,
        "bio": bio,
        "birthDate": birthDate

    }
    
    results = {
        "message" : "Author is created successfully",
        "response": author_dict
    }

    return results