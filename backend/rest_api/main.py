from fastapi import FastAPI, Depends
from databases import Database
from core import models, schemas, crud, database

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.database.disconnect()


@app.post("/notes/", response_model=schemas.Note)
async def create_note(note: schemas.NoteCreate):
    return await crud.create_note(database.database, note)


@app.get("/notes/", response_model=list[schemas.Note])
async def read_notes():
    return await crud.get_notes(database.database)
