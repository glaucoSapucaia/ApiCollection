from .models import notes
from .schemas import NoteCreate


async def create_note(database, note: NoteCreate):
    query = notes.insert().values(title=note.title, content=note.content)
    last_record_id = await database.execute(query)
    return {**note.dict(), "id": last_record_id}


async def get_notes(database):
    query = notes.select()
    return await database.fetch_all(query)
