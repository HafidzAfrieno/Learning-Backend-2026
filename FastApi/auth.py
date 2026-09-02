from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone
from typing import Optional
import bcrypt
import jwt

class AuthJwt:
    def __init__(self):
        self.__SECRET_KEY = "uerifjdskjhfjvflskvnidsfvnsdfkjlvdfvj838riog"
        self.__ALGORITHM = "HS256"
        self.__ACCESS_TOKEN_EXPIRE_MINUTES = 30
        self.fake_users_db = {}
        self.oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    def get_password_hash(self, password: str) -> str:
        pwd_bytes = password.encode('utf-8')
        salt = bcrypt.gensalt()
        hashed_bytes = bcrypt.hashpw(pwd_bytes, salt)
        return hashed_bytes.decode('utf-8')

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        plain_pwd_bytes = plain_password.encode('utf-8')
        hashed_pwd_bytes = hashed_password.encode('utf-8')
        return bcrypt.checkpw(plain_pwd_bytes, hashed_pwd_bytes)

    def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None) -> str:
        to_encode = data.copy()
        expire_time = expires_delta or timedelta(minutes=self.__ACCESS_TOKEN_EXPIRE_MINUTES)
        expire = datetime.now(timezone.utc) + expire_time
        
        to_encode.update({"exp": expire})
        token_jwt = jwt.encode(to_encode, self.__SECRET_KEY, algorithm=self.__ALGORITHM)
        return token_jwt

    def get_current_user(self, token: str = Depends(OAuth2PasswordBearer(tokenUrl="token"))):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token tidak valid atau telah kadaluwarsa",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, self.__SECRET_KEY, algorithms=[self.__ALGORITHM])
            username: Optional[str] = payload.get("sub")
            if username is None:
                raise credentials_exception
        except jwt.PyJWTError:
            raise credentials_exception

        user = self.fake_users_db.get(username)
        if user is None:
            raise credentials_exception
        return user