from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from database import get_db
from services.file_handler import handle_upload
router = APIRouter()

@router.post("/image")
async def upload_image(file: UploadFile = File(...), db: Session = Depends(get_db)):
    return await handle_upload(file, "image", db)