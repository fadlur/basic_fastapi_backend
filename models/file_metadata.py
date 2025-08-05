from sqlalchemy import Column, Integer, String, Float
from database import Base

class FileMetadata(Base):
    __tablename__ = "file_metadata"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    file_type = Column(String)
    mime_type = Column(String)
    size_kb = Column(Float)
    saved_path = Column(String)