from sqlalchemy.orm import Session
from app.models import Article
from app.schemas import ArticleCreate, ArticleUpdate

# Create a new article
def create_article(db: Session, article: ArticleCreate):
    new_article = Article(
        titre=article.titre,
        contenu=article.contenu,
        auteur=article.auteur,
        categorie=article.categorie,
        tags=article.tags
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article

# Get all articles (with optional filters)
def get_articles(db: Session, categorie: str = None, auteur: str = None, date: str = None):
    query = db.query(Article)
    if categorie:
        query = query.filter(Article.categorie == categorie)
    if auteur:
        query = query.filter(Article.auteur == auteur)
    if date:
        query = query.filter(Article.date >= date)
    return query.all()

# Get a single article by ID
def get_article(db: Session, article_id: int):
    return db.query(Article).filter(Article.id == article_id).first()

# Update an article
def update_article(db: Session, article_id: int, updates: ArticleUpdate):
    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        return None
    for field, value in updates.model_dump(exclude_none=True).items():
        setattr(article, field, value)
    db.commit()
    db.refresh(article)
    return article

# Delete an article
def delete_article(db: Session, article_id: int):
    article = db.query(Article).filter(Article.id == article_id).first()
    if not article:
        return None
    db.delete(article)
    db.commit()
    return article

# Search articles by title or content
def search_articles(db: Session, query: str):
    return db.query(Article).filter(
        Article.titre.contains(query) | Article.contenu.contains(query)
    ).all()