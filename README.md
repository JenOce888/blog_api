# Blog API

A backend REST API for managing a simple blog, built with FastAPI and MySQL.

## Technologies Used

- Python 3
- FastAPI
- SQLAlchemy
- MySQL
- Uvicorn

## Installation

1. Clone the repository :
   git clone https://github.com/JenOce888/blog_api.git
   cd blog_api

2. Install dependencies :
   pip install -r requirements.txt

3. Configure the database :
   - Create a .env file at the root of the project
   - Fill in the following information :
     DB_HOST=localhost
     DB_PORT=3306
     DB_USER=root
     DB_PASSWORD=your_password
     DB_NAME=blog_db

4. Run the application :
   uvicorn main:app --reload

5. Access the Swagger documentation :
   http://127.0.0.1:8000/docs

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /api/articles/ | Create an article |
| GET | /api/articles/ | Retrieve all articles |
| GET | /api/articles/{id} | Retrieve an article by ID |
| PUT | /api/articles/{id} | Update an article |
| DELETE | /api/articles/{id} | Delete an article |
| GET | /api/articles/search?query= | Search for an article |

## Available Filters

GET /api/articles?categorie=Technology
GET /api/articles?auteur=JenOce888
GET /api/articles?date=2026-03-23

## Usage Examples

### Create an article
POST /api/articles/
{
  "titre": "My first article",
  "contenu": "Content of the article",
  "auteur": "Your Name",
  "categorie": "Technology",
  "tags": "python,fastapi"
}

### Search for an article
GET /api/articles/search?query=fastapi

### Update an article
PUT /api/articles/1
{
  "titre": "Updated title",
  "categorie": "Development"
}

### Delete an article
DELETE /api/articles/1

## HTTP Status Codes

- 200 : Success
- 201 : Created successfully
- 404 : Article not found
- 422 : Validation error
500 : Internal server error

## Project Structure

blog_api/
│
├── app/
│   ├── __init__.py        
│   ├── database.py        
│   ├── models.py          
│   ├── schemas.py         
│   ├── controllers.py     
│   └── routes.py          
│
├── main.py                
├── .env                   
├── requirements.txt       
└── README.md              

## Author

MECHE JENNIFER OCEANE — INF222 EC1 TAF1