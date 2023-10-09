"""
User Service API Paths:

POST /users/register - Register a new user
POST /users/login - Login a user and return a token
POST /users/logout - Logout a user and invalidate the token
"""
from fastapi import Depends, HTTPException, APIRouter, status, Header
from bcrypt import gensalt, hashpw
from fastapi import APIRouter, Depends, Header, HTTPException, status
from framework.database import get_session
from framework.schema import User
from models.user_model import UserCreate, AdminCreate
from models.auth_model import InsertRecordResponse
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

user_router = APIRouter(prefix="/user", tags=["User"])


@user_router.post("/register")
async def register_user(register: AdminCreate, session: Session = Depends(get_session)):
    print(register)
    password_bytes = hashpw(bytes(register.password.get_secret_value(), "utf-8"), gensalt()).decode()
    try:
        new_user = User(email=register.email, password=password_bytes, first_name=register.first_name,
                        last_name=register.last_name, role=register.role)
        session.add(new_user)
        session.flush()  # Flush to get user_id populated
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="User already exists"
        )
    return InsertRecordResponse(id=new_user.id)


@user_router.post("/login")
async def login(login: AdminCreate, channel: str = Header(default=None), session=Depends(get_session)):
    print("inside login")
    pass

@user_router.post("/logout")
async def logout(session=Depends(get_session)):
    print("inside logout")
    pass
