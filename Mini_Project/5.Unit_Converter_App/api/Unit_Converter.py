from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field

app = FastAPI(title="API Konversi Satuan")

# 1. Definisi Skema Pydantic
class ConversionRequest(BaseModel):
    unit_type   : str = Field(...,example="length",description="Kategori konversi: 'length', 'temperature', atau 'weight'",)
    from_unit   : str = Field(..., example="km", description="Satuan asal (misal: km, m, c, f, kg)")
    to_unit     : str = Field(..., example="m", description="Satuan tujuan (misal: m, cm, f, c, g)")
    from_value  : float | int = Field( ..., example=5, description="Nilai asal yang akan dikonversi")
    to_value    : float | int | None = Field(default=None, description="Nilai hasil konversi (otomatis diisi jika kosong)")

# 2. Fungsi Logika Konversi
def convert_length(value: float, from_u: str, to_u: str) -> float:
    # Konversi ke meter dulu sebagai standar
    to_meters = {
        "km": value * 1000,
        "m": value,
        "cm": value / 100,
        "mm": value / 1000,
        "mile": value * 1609.34,
    }

    if from_u not in to_meters or to_u not in to_meters:
        raise HTTPException(
            status_code=400,
            detail=f"Satuan panjang tidak valid. Gunakan: {list(to_meters.keys())}",
        )

    meters = to_meters[from_u]

    # Konversi dari meter ke satuan tujuan
    from_meters = {
        "km": meters / 1000,
        "m": meters,
        "cm": meters * 100,
        "mm": meters * 1000,
        "mile": meters / 1609.34,
    }
    return round(from_meters[to_u], 4)

def convert_temperature(value: float, from_u: str, to_u: str) -> float:
    # Ubah ke Celcius dulu
    if from_u == "c":
        celsius = value
    elif from_u == "f":
        celsius = (value - 32) * 5 / 9
    elif from_u == "k":
        celsius = value - 273.15
    else:
        raise HTTPException(
            status_code=400,
            detail="Satuan suhu tidak valid. Gunakan: 'c', 'f', atau 'k'",
        )

    # Ubah Celcius ke satuan tujuan
    if to_u == "c":
        return round(celsius, 2)
    elif to_u == "f":
        return round((celsius * 9 / 5) + 32, 2)
    elif to_u == "k":
        return round(celsius + 273.15, 2)
    else:
        raise HTTPException(
            status_code=400,
            detail="Satuan suhu tidak valid. Gunakan: 'c', 'f', atau 'k'",
        )

# 3. Endpoint FastAPI
@app.post("/api/convert", response_model=ConversionRequest)
async def create_item(item: ConversionRequest):
    unit_type = item.unit_type.lower()
    from_u = item.from_unit.lower()
    to_u = item.to_unit.lower()

    # Hitung nilai jika to_value belum diisi
    if item.to_value is None:
        if unit_type == "length":
            item.to_value = convert_length(item.from_value, from_u, to_u)
        elif unit_type == "temperature":
            item.to_value = convert_temperature(item.from_value, from_u, to_u)
        else:
            raise HTTPException(
                status_code=400,
                detail="unit_type tidak valid. Gunakan 'length' atau 'temperature'",
            )

    return item
