from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

class OIn(BaseModel):
    full_name: str
    phone: str | None = None
    email: str | None = None
    address: str | None = None

@router.post("/")
def create(data: OIn, db: Session = Depends(get_session)):
    row = db.execute(text("""
        INSERT INTO owners (full_name, phone, email, address)
        VALUES (:full_name,:phone,:email,:address) RETURNING id
    """), data.dict()).fetchone()
    db.commit()
    return {"id": row[0]}

@router.get("/")
def list_all(q: str | None = None, db: Session = Depends(get_session)):
    sql = "SELECT * FROM owners"
    params = {}
    if q:
        sql += " WHERE full_name ILIKE :q OR phone ILIKE :q"
        params['q'] = f"%{q}%"
    return [dict(r._mapping) for r in db.execute(text(sql), params).fetchall()]

@router.get("/{owner_id}")
def get(owner_id: int, db: Session = Depends(get_session)):
    o = db.execute(text("SELECT * FROM owners WHERE id=:i"), {"i": owner_id}).fetchone()
    if not o: raise HTTPException(404)
    pets = db.execute(text("SELECT * FROM pets WHERE owner_id=:i"),
                      {"i": owner_id}).fetchall()
    return {**dict(o._mapping), "pets": [dict(p._mapping) for p in pets]}
