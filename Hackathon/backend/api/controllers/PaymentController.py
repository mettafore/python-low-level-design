"""
Payment Service API Paths:

POST /payments - Initiate a new payment
GET /payments/{payment_id} - Get details of a specific payment (For Buyer/Admin/Seller involved)
PUT /payments/{payment_id} - Update details of a specific payment (For Admin/Seller involved)
DELETE /payments/{payment_id} - Delete a specific payment (For Admin/Seller involved)
"""
from fastapi import Depends, HTTPException, APIRouter, status, Header


payment_router = APIRouter(prefix="/payments", tags=["Payment"])

@payment_router.post("/")
async def create_payment():
    pass


@payment_router.get("/{payment_id}")
async def get_payment(payment_id: str):
    pass


@payment_router.put("/{payment_id}")
async def update_payment(payment_id: str):
    pass


@payment_router.delete("/{payment_id}")
async def delete_payment(payment_id: str):
    pass


