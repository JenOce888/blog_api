from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Article(Base):
    __tablename__ = "articles"

    id          = Column(Integer, primary_key=True, index=True)
    titre       = Column(String(255), nullable=False)
    contenu     = Column(Text, nullable=False)
    auteur      = Column(String(100), nullable=False)
    date        = Column(DateTime, default=func.now())
    categorie   = Column(String(100), nullable=False)
    tags        = Column(String(255), nullable=True)