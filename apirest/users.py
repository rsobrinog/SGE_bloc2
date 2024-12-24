from fastapi import APIRouter
import users_sch, user_service

router = APIRouter()

@router.get("/all_users")
async def get_users():
    return users_sch.users_schema(user_service.get_all_users())