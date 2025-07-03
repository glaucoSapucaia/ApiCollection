import os
import asyncio
from faker import Faker
from databases import Database
from datetime import datetime
from random import randint
from core.models import notes

DATABASE_URL = os.getenv("DATABASE_URL")

fake = Faker()
db = Database(DATABASE_URL)


async def gerar_notas(qtd: int = 1000):
    await db.connect()

    notas = []
    for _ in range(qtd):
        created_at = fake.date_time_this_year()
        updated_at = (
            created_at
            if randint(0, 3) == 0
            else fake.date_time_between(start_date=created_at, end_date=datetime.now())
        )

        notas.append(
            {
                "title": fake.sentence(nb_words=6),
                "content": fake.paragraph(nb_sentences=3),
                "author": fake.name(),
                "tags": ",".join(fake.words(nb=3)),
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

    query = notes.insert()
    await db.execute_many(query=query, values=notas)
    await db.disconnect()

    print(f"{qtd} notas inseridas com sucesso.")


if __name__ == "__main__":
    asyncio.run(gerar_notas())
