from fastapi import FastAPI, Depends, HTTPException, status
from auth import AuthJwt
from ConvertNumber import ConvertNumber
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordRequestForm

# uvicorn main:app --reload

app = FastAPI()
convert = ConvertNumber()
securty = AuthJwt()

class UserRegister(BaseModel):
    username    : str
    password    :str

class Token(BaseModel):
    access_token : str
    token_type : str

class ConvertRequest(BaseModel):
    type_unit: str
    from_num: float
    unit_from: str
    unit_to: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/convert")
async def api_convert(data: ConvertRequest) -> dict:
    if data.type_unit == "weight":
        result = convert.convert_weight(from_num=data.from_num,unit_from=data.unit_from,unit_to=data.unit_to,)
    elif data.type_unit == "length":
        result = convert.convert_length( from_num=data.from_num, unit_from=data.unit_from, unit_to=data.unit_to,)
    elif data.type_unit == "tempr":
        result = convert.convert_tempr(from_num=data.from_num,unit_from=data.unit_from,unit_to=data.unit_to,)
    else:
        raise HTTPException(status_code=400, detail="Tipe unit tidak dikenal")
    return {"result_convert": result}

@app.post("/register")
async def register(user: UserRegister):
    if user.username in securty.fake_users_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Username sudah terdaftar"
        )
    
    hashed_password = securty.get_password_hash(user.password)
    securty.fake_users_db[user.username] = {
        "username": user.username,
        "password": hashed_password
    }
    return {"message": "Registrasi Berhasil!"}


@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = securty.fake_users_db.get(form_data.username)
    if not user or not securty.verify_password(form_data.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Username Atau Password Salah",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    access_token = securty.create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me")
async def read_users_me(current_user: dict = Depends(securty.get_current_user)):
    return {
        "username": current_user["username"], 
        "status": "Aktif"
    }