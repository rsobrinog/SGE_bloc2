from typing import List
from fastapi import APIRouter

router = APIRouter

@router.get("/all_users", response_nodel=List[dict])
async def get_users():
    return {"":""}