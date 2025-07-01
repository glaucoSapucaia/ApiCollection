from sqlalchemy import Table, Column, Integer, String, MetaData

metadata = MetaData()

notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(100)),
    Column("content", String(250)),
)
