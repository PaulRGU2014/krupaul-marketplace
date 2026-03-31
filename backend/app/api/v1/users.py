from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.models.user import User

router = APIRouter()

@router.get("/") 

def list_users(db: Session = Depends(get_db)):
    users = db.scalars(select(User)).all()
    return [{"id":u.id, "email":u.email} for u in users]