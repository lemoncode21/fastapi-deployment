from fastapi import APIRouter
from repository import NoteRepository

from schema import NoteCreate, ResponseSchema

router = APIRouter(
    prefix="/note",
    tags=['note']
)


@router.post("", response_model_exclude_none=True)
async def create_note(create_form: NoteCreate):
    await NoteRepository.create(create_form)
    return ResponseSchema(detail="Successfully created data !")


@router.get("", response_model_exclude_none=True)
async def get_all_note():
    data = await NoteRepository.get_all()
    return ResponseSchema(detail="Successfully fetch data !", result=data)
