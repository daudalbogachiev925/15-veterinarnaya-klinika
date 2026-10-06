from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from datetime import date
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

class PIn(BaseModel):
    owner_id: int
    species: str
    breed: str | None = None
    name: str
    birth: date | None = None
    weight: float | None = None
    chip: str | None = None

@router.post("/")
def create(data: PIn, db: Session = Depends(get_session)):
    row = db.execute(text("""
        INSERT INTO pets (owner_id, species, breed, name, birth, weight, chip)
        VALUES (:owner_id,:species,:breed,:name,:birth,:weight,:chip) RETURNING id
    """), data.dict()).fetchone()
    db.commit()
    return {"id": row[0]}

@router.get("/{pet_id}")
def get(pet_id: int, db: Session = Depends(get_session)):
    p = db.execute(text("SELECT * FROM pets WHERE id=:i"), {"i": pet_id}).fetchone()
    if not p: raise HTTPException(404)
    return dict(p._mapping)
