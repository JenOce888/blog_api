from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Optional
from app.database import get_db
from app.schemas import ArticleCreate, ArticleUpdate, ArticleResponse
from typing import List
import app.controllers as ctrl

router = APIRouter(prefix="/api/articles", tags=["Articles"])

# POST /api/articles — Create an article
@router.post("/", response_model=ArticleResponse, status_code=201)
def create_article(article: ArticleCreate, db: Session = Depends(get_db)):
    return ctrl.create_article(db, article)

# GET /api/articles — Get all articles (with optional filters)
@router.get("/", response_model=List[ArticleResponse], status_code=200)
def get_articles(
    categorie: Optional[str] = Query(None),
    auteur: Optional[str] = Query(None),
    date: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    return ctrl.get_articles(db, categorie, auteur, date)

# GET /api/articles/search — Search articles
@router.get("/search", response_model=List[ArticleResponse], status_code=200)
def search_articles(query: str = Query(...), db: Session = Depends(get_db)):
    results = ctrl.search_articles(db, query)
    if not results:
        raise HTTPException(status_code=404, detail="No articles found")
    return results

# GET /api/articles/{id} — Get a single article
@router.get("/{article_id}", response_model=ArticleResponse, status_code=200)
def get_article(article_id: int, db: Session = Depends(get_db)):
    article = ctrl.get_article(db, article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

# PUT /api/articles/{id} — Update an article
@router.put("/{article_id}", response_model=ArticleResponse, status_code=200)
def update_article(article_id: int, updates: ArticleUpdate, db: Session = Depends(get_db)):
    article = ctrl.update_article(db, article_id, updates)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return article

# DELETE /api/articles/{id} — Delete an article
@router.delete("/{article_id}", status_code=200)
def delete_article(article_id: int, db: Session = Depends(get_db)):
    article = ctrl.delete_article(db, article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")
    return {"message": f"Article {article_id} deleted successfully"}