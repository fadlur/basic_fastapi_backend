from fastapi import FastAPI, Form, File, UploadFile
from fastapi import Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# --------------------------
# GET Request
# --------------------------
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"method": "GET", "item_id": item_id, "query": q}

# --------------------------
# POST Request - JSON Body
# --------------------------
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

@app.post("/items/json")
def create_item_json(item: Item):
    return {"method": "POST", "type": "application/json", "data": item.dict()}

# --------------------------
# POST Request - Form Data
# --------------------------
@app.post("/items/form")
def create_item_form(name: str = Form(...), price: float = Form(...)):
    return {"method": "POST", "type": "form-data", "name": name, "price": price}

# --------------------------
# POST Request - x-www-form-urlencoded
# --------------------------
@app.post("/items/xform")
async def create_item_xform(request: Request):
    form_data = await request.form()
    return {"method": "POST", "type": "x-www-form-urlencoded", "data": dict(form_data)}

# --------------------------
# POST Request - File Upload
# --------------------------
@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    return {
        "method": "POST",
        "type": "multipart/form-data",
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(content)
    }

# --------------------------
# PUT / PATCH Request
# --------------------------
@app.put("/items/{item_id}")
@app.patch("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"method": "PUT/PATCH", "item_id": item_id, "updated_data": item.dict()}

# --------------------------
# DELETE Request
# --------------------------
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"method": "DELETE", "item_id": item_id, "status": "deleted"}