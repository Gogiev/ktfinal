from fastapi import APIRouter, Depends
from app.api.deps import require_role, get_current_user
from app.models.user import User, UserRole

router = APIRouter()

@router.get("/me")
async def get_me(current_user: User = Depends(get_current_user)):
    return {"email": current_user.email, "role": current_user.role}

@router.get("/admin-only")
async def admin_endpoint(current_user: User = Depends(require_role(UserRole.ADMIN))):
    return {"message": "Привет, Админ!"}