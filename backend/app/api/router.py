from fastapi import APIRouter

api_router = APIRouter()

# Register sub-routers here as features are added
# Example:
# from app.api.endpoints import items, users
# api_router.include_router(users.router, prefix="/users", tags=["users"])
# api_router.include_router(items.router, prefix="/items", tags=["items"])
