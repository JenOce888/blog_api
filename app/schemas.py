from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Used when CREATING an article (user sends this)
class ArticleCreate(BaseModel):
    titre: str
    contenu: str
    auteur: str
    categorie: str
    tags: Optional[str] = None

# Used when UPDATING an article (all fields optional)
class ArticleUpdate(BaseModel):
    titre: Optional[str] = None
    contenu: Optional[str] = None
    categorie: Optional[str] = None
    tags: Optional[str] = None

# Used when RETURNING an article (API sends this back)
class ArticleResponse(BaseModel):
    id: int
    titre: str
    contenu: str
    auteur: str
    date: datetime
    categorie: str
    tags: Optional[str] = None

    class Config:
        from_attributes = True  # Allows reading data from SQLAlchemy objects