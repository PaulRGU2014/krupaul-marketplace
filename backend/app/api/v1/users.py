from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.models.user import User

router = APIRouter()


def _to_user_summary(user: User) -> dict[str, str | int]:
    return {"id": user.id, "email": user.email}


@router.get("/")
def list_users(db: Session = Depends(get_db)):
    db_users = db.scalars(select(User).order_by(User.id)).all()
    return [_to_user_summary(user) for user in db_users]
