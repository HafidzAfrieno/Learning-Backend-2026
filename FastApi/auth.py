from datetime import datetime,timedelta
from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2AuthorizationCodeBearer,OAuth2PasswordRequestForm
import jwt
from passlib.context import CryptContext
from pydantic import BaseModel

class AuthJwt:
    def __init__(self):
        # Secret key untuk menandatangani JWT (Ganti di lingkungan produksi)
        self.__SECRET_KEY = "uerifjdskjhfjvflskvnidsfvnsdfkjlvdfvj838riog"
        self.__ALGORITHM = "HS256"
        self.__ACCESS_TOKEN_EXPIRE_MINUTES = 30
        self.fake_users_db = {}
        # Context untuk hashing password
        self.pwd_context = CryptContext(schemes=["bcrypt"],deprecared="auto")
        # handler skema OAuth2
        self.oauth2_sceme = OAuth2AuthorizationCodeBearer(tokenUrl="token")

    def get_password_has(self,password: str)-> str:
        return self.pwd_context.hash(password)

    def verify_password(self,plain_password: str,hashed_password:str)-> bool:
        return self.pwd_context.verify(plain_password,hashed_password)

    def create_access_token(self,data:dict,expires_delta:Optional[timedelta] = None):
        to_encode = data.copy()
        expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
        to_encode.update({"exp":expire})
        token_jwt = jwt.encode(to_encode,self.__SECRET_KEY,algorithm=self.__ALGORITHM)
        return token_jwt

    def get_current_user(self,token:str):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token tidak valid atau telah kadaluwarsa",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token,self.__SECRET_KEY,algorithms=[self.__ALGORITHM])
            username : str = payload.get("sub")
            if username is None:
                raise credentials_exception
        except jwt.PyJWTError:
            raise credentials_exception

        user = self.fake_users_db.get(username)
        if user is None:
            raise credentials_exception
        return user