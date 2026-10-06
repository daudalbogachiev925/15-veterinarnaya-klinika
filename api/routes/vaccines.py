from fastapi import APIRouter, Depends
from pydantic import BaseModel
from datetime import date
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

class VacIn(BaseModel):
    pet_id: int
    vaccine: str
    given: date
    next_due: date | None = None
    vet_id: int | None = None

@router.post("/")
def create(data: VacIn, db: Session = Depends(get_session)):
    row = db.execute(text("""
        INSERT INTO vaccines (pet_id, vaccine, given, next_due, vet_id)
        VALUES (:pet_id,:vaccine,:given,:next_due,:vet_id) RETURNING id
    """), data.dict()).fetchone()
    db.commit()
    return {"id": row[0]}

@router.get("/pet/{pet_id}")
def by_pet(pet_id: int, db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(
        text("SELECT * FROM vaccines WHERE pet_id=:p ORDER BY given DESC"),
        {"p": pet_id}).fetchall()]
