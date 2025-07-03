from sqlalchemy import Table, Column, Integer, String, DateTime, MetaData
from sqlalchemy.sql import func

metadata = MetaData()

notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(100)),
    Column("content", String(250)),
    Column("author", String(100)),
    Column("created_at", DateTime, server_default=func.now()),
    Column("updated_at", DateTime, onupdate=func.now()),
    Column("tags", String(100)),
)
