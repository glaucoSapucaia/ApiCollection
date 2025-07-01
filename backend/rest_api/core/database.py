from databases import Database

DATABASE_URL = "postgresql://postgres:postgres@db:5432/mydb"

database = Database(DATABASE_URL)
