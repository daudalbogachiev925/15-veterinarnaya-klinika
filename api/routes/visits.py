from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

class VIn(BaseModel):
    pet_id: int
    vet_id: int
    service_id: int
    diagnosis: str | None = None
    price: float
    notes: str | None = None

@router.post("/")
def create(data: VIn, db: Session = Depends(get_session)):
    row = db.execute(text("""
        INSERT INTO visits (pet_id, vet_id, service_id, diagnosis, price, notes)
        VALUES (:pet_id,:vet_id,:service_id,:diagnosis,:price,:notes) RETURNING id
    """), data.dict()).fetchone()
    db.commit()
    return {"id": row[0]}

@router.get("/pet/{pet_id}")
def by_pet(pet_id: int, db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text("""
        SELECT v.id, s.name AS service, v.diagnosis, v.price, v.visit_date
        FROM visits v JOIN services s ON s.id=v.service_id
        WHERE v.pet_id=:p ORDER BY v.visit_date DESC
    """), {"p": pet_id}).fetchall()]
