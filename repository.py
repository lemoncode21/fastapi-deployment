from sqlalchemy.sql import select
from schema import NoteCreate

from config import db, commit_rollback
from model import Note
from schema import NoteCreate


class NoteRepository:

    @staticmethod
    async def create(form: NoteCreate):
        db.add(Note(name=form.name,description=form.description))
        await commit_rollback()

    @staticmethod
    async def get_all():
        query = select(from_obj=Note,columns="*")
        return (await db.execute(query)).fetchall()

    