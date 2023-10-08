"""
User Service API Paths:

POST /users/register - Register a new user
POST /users/login - Login a user and return a token
POST /users/logout - Logout a user and invalidate the token
"""
from fastapi import Depends, HTTPException, APIRouter, status, Header

user_router = APIRouter(prefix="/user", tags=["User"])


@user_router.post("/register")
async def register_user(register: AuthRequest, session: Session = Depends(get_session)):
    print("inside register_user")
    pass


@user_router.post("/login")
async def login(login: AuthRequest, channel: str = Header(default=None), session=Depends(get_session)) -> TokenResponse:
    print("inside login")
    pass

@user_router.post("/logout")
async def logout(session=Depends(get_session)):
    print("inside logout")
    pass




