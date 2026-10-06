from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_session

router = APIRouter()

@router.get("/revenue")
def revenue(db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text(open('sql/revenue.sql').read())).fetchall()]

@router.get("/vaccines")
def vaccines(db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text(open('sql/vaccines.sql').read())).fetchall()]

@router.get("/diagnoses")
def diagnoses(db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text(open('sql/top_diagnoses.sql').read())).fetchall()]

@router.get("/visits")
def visits(db: Session = Depends(get_session)):
    return [dict(r._mapping) for r in db.execute(text(open('sql/visits.sql').read())).fetchall()]
