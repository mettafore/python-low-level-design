from abc import ABC, abstractmethod
from fastapi import Depends, HTTPException, status, Header
from sqlalchemy.orm import Session
from framework.database import get_session
from models.auth_model import AuthRequest, InsertRecordResponse, PasswordAuthRequest, TokenResponse
from models.user_model import UserCreate
from typing import Type, Dict
from framework.schema import User
from bcrypt import checkpw, gensalt, hashpw
from datetime import timedelta
import logging
from jwt import ExpiredSignatureError, InvalidTokenError, decode, encode
from datetime import datetime
from os import environ

logger = logging.getLogger(__name__)

class AuthStrategy(ABC):
    @abstractmethod
    def login(self, auth_request: AuthRequest, session: Session):
        pass

    def register(self, user_det: UserCreate, session: Session):
        password_bytes = hashpw(bytes(user_det.password.get_secret_value(), "utf-8"), gensalt()).decode()
        try:
            new_user = User(
                email=user_det.email, 
                password=password_bytes,
                first_name=user_det.first_name,
                last_name=user_det.last_name,
                role=user_det.role
                            )
            session.add(new_user)
            session.commit()  # Flush to get user_id populated
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT, detail="User already exists"
            )
        return InsertRecordResponse(id=new_user.id)

    @abstractmethod
    def logout(self, auth_request: AuthRequest, session: Session):
        pass

class PasswordAuthStrategy(AuthStrategy):
    def login(self, auth_request: PasswordAuthRequest, session: Session):
        user = session.query(User).filter(User.email == auth_request.email).first()

        if user and checkpw(
            auth_request.password.get_secret_value().encode(), 
            user.password.encode()
            ):
            user_id = user.id
            print(user.role.value)
            access_token = self._generate_token(
                payload = {
                    "id": str(user_id),
                    "role": str(user.role.value),
                },
                env_secret_key="JWT_ACCESS_SECRET_KEY",
                relative_time=timedelta(days=1),
            )
            refresh_token = self._generate_token(
                {"id": str(user_id)},
                "JWT_REFRESH_SECRET_KEY",
                timedelta(days=90),
            )
            return TokenResponse(token=access_token, refresh_token=refresh_token)
        else:
            logger.error("Invalid email or password [401:INVALID CREDENTIALS]")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid email or password"
            )
        
    def _generate_token(self, payload: Dict, env_secret_key: str, relative_time: timedelta):
        payload["exp"] = datetime.utcnow() + relative_time
        return encode(
            payload,
            environ.get(env_secret_key),
        )
    
    def decode_token(self, token: str = Header(...)):
        """
        Decode token and returns the payload as a dictionary.

        :param token: The `token` parameter is a string that represents a token. It is expected to be passed
        as a header in a request
        :type token: str
        :return: the decoded payload from the token.
        """
        payload = self._verify_token(token)
        payload["id"] = int(payload["id"])
        return payload
    
    def _verify_token(self, token: str):
        """
        Take token as input and verifies its validity by decoding it using a secret key, raising appropriate exceptions if the token is expired or invalid.

        :param token: The `token` parameter is a string that represents a JSON Web Token (JWT). It is used
        to authenticate and authorize a user in a web application
        :type token: str
        :return: the decoded token if it is valid.
        """
        try:
            return decode(token, environ.get("JWT_ACCESS_SECRET_KEY"), "HS256")
        except ExpiredSignatureError:
            logger.error("Expired token [401:EXPIRED TOKEN]")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Expired token"
            )
        except InvalidTokenError:
            logger.error("Invalid token [401:INVALID TOKEN]")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
            )


    def logout(self, auth_request: AuthRequest, session: Session):
        # Implement logout logic here
        pass

class OTPAuthStrategy(AuthStrategy):
    def login(self, auth_request: AuthRequest, session: Session):
        # Implement login logic here
        pass

    def logout(self, auth_request: AuthRequest, session: Session):
        # Implement logout logic here
        pass

class AuthStrategyFactory:
    @staticmethod
    def create_strategy(strategy_type: str) -> Type[AuthStrategy]:
        if strategy_type == 'password':
            return PasswordAuthStrategy()
        elif strategy_type == 'otp':
            return OTPAuthStrategy()
        else:
            raise ValueError("Invalid strategy type")

class AuthServiceImpl:
    def __init__(self, strategy: str):
        self.strategy = AuthStrategyFactory.create_strategy(strategy)

    def login(self, auth_request: AuthRequest, session: Session = Depends(get_session)):
        return self.strategy.login(auth_request, session)

    def register(self, user_det: UserCreate, session: Session = Depends(get_session)):
        return self.strategy.register(user_det, session)

    def logout(self, auth_request: AuthRequest, session: Session = Depends(get_session)):
        return self.strategy.logout(auth_request, session)
    
