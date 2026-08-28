from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# uvicorn main:app --reload

app = FastAPI()

# Tambahkan konfigurasi CORS ini
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Mengizinkan semua origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ConvertNumber:
    def __init__(self):
        self.from_num = 0
        self.to_num = 0
        self.unit_length = {"km": 1, "hm": 2, "dam": 3, "m": 4, "dm": 5, "cm": 6, "mm": 7}
        self.unit_weight = {"kg": 1, "hg": 2, "dag": 3, "g": 4, "dg": 5, "cg": 6, "mg": 7}
        self.unit_tempr = {"c": 1, "r": 2, "f": 3, "k": 4}

    def convert_length(self,from_num:int,unit_from:str,unit_to:str):
        unit_from = unit_from.lower()
        unit_to = unit_to.lower()

        if unit_from not in self.unit_length or unit_to not in self.unit_length:
            raise ValueError("Satuan panjang tidak valid.")

        self.from_num = from_num
        unit_type_1 = self.unit_length[unit_from]
        unit_type_2 = self.unit_length[unit_to]

        # Selisih tingkat satuan panjang
        step = abs(unit_type_1 - unit_type_2)
        if unit_type_1 < unit_type_2:
            self.to_num = from_num * (10 ** step)
        else:                        
            self.to_num = from_num / (10 ** step)
        return self.to_num

    def convert_weight(self, from_num: float, unit_from: str, unit_to: str) -> float:
        unit_from = unit_from.lower()
        unit_to = unit_to.lower()

        if unit_from not in self.unit_weight or unit_to not in self.unit_weight:
            raise ValueError("Satuan berat tidak valid.")

        self.from_num = from_num
        unit_type_1 = self.unit_weight[unit_from]
        unit_type_2 = self.unit_weight[unit_to]

        # Selisih tingkat satuan berat
        step = abs(unit_type_1 - unit_type_2)
        if unit_type_1 < unit_type_2:
            self.to_num = from_num * (10 ** step)
        else:                       
            self.to_num = from_num / (10 ** step)
        return self.to_num

    def convert_tempr(self, from_num: float, unit_from: str, unit_to: str) -> float:
        unit_from = unit_from.lower()
        unit_to = unit_to.lower()

        if unit_from not in self.unit_tempr or unit_to not in self.unit_tempr:
            raise ValueError("Satuan suhu tidak valid.")

        self.from_num = from_num

        if unit_from == "c":
            celsius = from_num
        elif unit_from == "r":
            celsius = from_num * (5 / 4)
        elif unit_from == "f":
            celsius = (from_num - 32) * (5 / 9)
        elif unit_from == "k":
            celsius = from_num - 273.15

        if unit_to == "c":
            self.to_num = celsius
        elif unit_to == "r":
            self.to_num = celsius * (4 / 5)
        elif unit_to == "f":
            self.to_num = (celsius * 9 / 5) + 32
        elif unit_to == "k":
            self.to_num = celsius + 273.15
        return self.to_num

class ConvertRequest(BaseModel):
    type_unit: str
    from_num: float
    unit_from: str
    unit_to: str
    
convert = ConvertNumber()

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