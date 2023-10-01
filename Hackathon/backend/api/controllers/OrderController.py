"""
Order Service API Paths:

POST /orders - Create a new order
GET /orders - Get the list of all orders (For Admin/Seller involved)
GET /orders/{order_id} - Get details of a specific order (For Buyer/Admin/Seller involved)
PUT /orders/{order_id} - Update details of a specific order (For Admin/Seller involved)
DELETE /orders/{order_id} - Delete a specific order (For Admin/Seller involved)
"""
from fastapi import Depends, HTTPException, APIRouter, status, Header


order_router = APIRouter(prefix="/orders", tags=["Order"])


@order_router.post("/")
async def create_order():
    pass


@order_router.get("/")
async def get_all_orders():
    pass


@order_router.get("/{order_id}")
async def get_order(order_id: str):
    pass


@order_router.put("/{order_id}")
async def update_order(order_id: str):
    pass


@order_router.delete("/{order_id}")
async def delete_order(order_id: str):
    pass