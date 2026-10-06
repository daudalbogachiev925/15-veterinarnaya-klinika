from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

class VIn(BaseModel):
    full_name: str
    spec: str | None = None
    cabinet: str | None = None

@router.post("/")
def create(data: VIn, db: Session = Depends(get_session)):
    row = db.execute(text("""
        INSERT INTO vets (full_name, spec, cabinet)
        VALUES (:full_name,:spec,:cabinet) RETURNING id
    """), data.dict()).fetchone()
    db.commit()
    return {"id": row[0]}

@router.get("/")
def list_all(db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text("SELECT * FROM vets")).fetchall()]
