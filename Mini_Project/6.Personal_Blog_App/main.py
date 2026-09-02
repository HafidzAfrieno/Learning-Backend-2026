from fastapi import FastAPI, Request, Form, Depends, HTTPException, status
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordRequestForm

from utils.storage_function import JsonFileHandler
from utils.auth_function import AuthHandler

app = FastAPI()
auth = AuthHandler()
templates = Jinja2Templates(directory='templates')
app.mount("/static", StaticFiles(directory="static"), name="static")
db_handler = JsonFileHandler()

@app.post("/register")
async def register(username: str = Form(...), password: str = Form(...)):
    users = db_handler.read_data() 
    if username in users:
        raise HTTPException(status_code=400, detail="Username sudah terdaftar")
    hashed_password = auth.hash_password(password)
    users[username] = {"username": username, "password": hashed_password}
    db_handler.write_data(users) 
    return {"message": "User berhasil terdaftar"}

@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    users = db_handler.read_data()
    user = users.get(form_data.username)
    if not user or not auth.verify_password(form_data.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username atau password salah"
        )
    access_token = auth.create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/me")
async def read_users_me(current_user: dict = Depends(auth.get_current_user)):
    return current_user

#=======================================================================================================

@app.get('/',response_class=HTMLResponse)
async def home_page(request :Request):
    return templates.TemplateResponse(
        request=request,
        name='guest/index.html',
        context={
            "title":"Halaman User",
        }
    )

# 1. Halaman Dasbor Admin
@app.get("/admin/dashboard")
async def show_dashboard(request: Request):
    articles_data = db_handler.list_data()
    return templates.TemplateResponse(
        request=request, 
        name="admin/dashboard.html", 
        context={"articles": articles_data}
    )

# 2. Halaman Tambah Artikel (GET Form)
@app.get("/admin/create")
async def show_create_form(request: Request):
    return templates.TemplateResponse(request=request, name="admin/add-article.html")

# Submit Tambah Artikel (POST)
@app.post("/admin/create")
async def handle_create_article(title: str = Form(...), content: str = Form(...), created_at: str = Form(...)):
    db_handler.create_article(title=title, content=content, created_at=created_at)
    return RedirectResponse(url="/admin/dashboard", status_code=303)

# 3. Halaman Edit Artikel (GET Form dengan data awal)
@app.get("/admin/edit/{article_id}")
async def show_edit_form(request: Request, article_id: str):
    article = db_handler.list_data(article_id=article_id)
    if not article:
        return templates.TemplateResponse(request=request, name="404.html", status_code=404)
    return templates.TemplateResponse(
        request=request, 
        name="admin/edit-article.html", 
        context={"article": article}
    )

# Submit Edit Artikel (POST)
@app.post("/admin/edit/{article_id}")
async def handle_update_article(article_id: str, title: str = Form(...), content: str = Form(...)):
    db_handler.update_data(article_id=article_id, title=title, content=content)
    return RedirectResponse(url="/admin/dashboard", status_code=303)

# 4. Process Hapus Artikel (POST)
@app.post("/admin/delete/{article_id}")
async def handle_delete_article(article_id: str):
    db_handler.delete_data(article_id=article_id)
    return RedirectResponse(url="/admin/dashboard", status_code=303)


