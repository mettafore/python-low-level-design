"""
Admin Specific API Paths:

GET /admin/users - Get the list of all users (For Admin)
DELETE /admin/users/{user_id} - Delete a specific user (For Admin)
PUT /admin/users/{user_id} - Update details of a specific user (For Admin)
"""
from fastapi import Depends, HTTPException, APIRouter, status, Header

admin_router = APIRouter(prefix="/admin", tags=["Admin"])

@admin_router.get("/users")
async def get_users():
    pass

@admin_router.delete("/users/{user_id}")
async def delete_user(user_id: str):
    pass

@admin_router.put("/users/{user_id}")
async def update_user(user_id: str):
    pass
