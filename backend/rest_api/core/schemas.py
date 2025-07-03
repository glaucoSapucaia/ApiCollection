from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class NoteBase(BaseModel):
    title: str
    content: str
    author: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    tags: Optional[str] = None


class NoteCreate(NoteBase):
    pass


class Note(NoteBase):
    id: int

    model_config = {"from_attributes": True}
