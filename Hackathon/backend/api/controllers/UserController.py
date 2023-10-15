"""
User Service API Paths:

POST /users/register - Register a new user
POST /users/login - Login a user and return a token
POST /users/logout - Logout a user and invalidate the token
"""
from fastapi import Depends, APIRouter
from fastapi import APIRouter, Depends, Header, HTTPException, status
from framework.database import get_session
from framework.schema import User
from models.user_model import UserCreate
from sqlalchemy.orm import Session
from services.AuthService import AuthServiceImpl
from models.auth_model import AuthRequest

user_router = APIRouter(prefix="/user", tags=["User"])

@user_router.post("/register")
async def register_user(register: UserCreate, session: Session = Depends(get_session)):
    return AuthServiceImpl("password").register(register, session)


@user_router.post("/login")
async def login(login: AuthRequest, session:Session=Depends(get_session)):
    return AuthServiceImpl("password").login(login, session)

@user_router.post("/logout")
async def logout(session=Depends(get_session)):
    pass