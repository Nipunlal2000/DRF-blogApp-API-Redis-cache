# 📰 DRF Blog API with Redis Caching

![Python](https://img.shields.io/badge/Python-3.9-blue.svg)
![Django](https://img.shields.io/badge/Django-4.x-green.svg)
![DRF](https://img.shields.io/badge/DRF-3.x-red.svg)
![Redis](https://img.shields.io/badge/Redis-Caching-orange.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

A lightweight, high-performance **Blog REST API** built using Django REST Framework and Redis for caching.  
It demonstrates how to cache list and detail API views using both **manual cache control** and **`@method_decorator`-based caching**.

---

## 🚀 Features

- 📄 CRUD for blog posts
- ⚡ Redis-backed caching for optimized GET requests
- ✅ APIView and generic class-based views
- 🧪 Manual and decorator-based cache control
- 🧹 Auto cache invalidation on update/delete
- 🧾 Source flags to identify if data is from DB or Redis

---

## 🛠️ Tech Stack

| Tool            | Description                            |
|-----------------|----------------------------------------|
| Django          | Web framework                          |
| Django REST     | For API development                    |
| Redis           | In-memory cache database               |
| django-redis    | Django integration with Redis          |
| DRF Generic Views | For fast API setup                  |
| APIView         | For custom logic                       |

---

## ⚙️ Setup Instructions

### 1. 🔁 Clone the Repo

```bash
git clone https://github.com/<your-username>/drf-blog-api-redis-cache.git
cd drf-blog-api-redis-cache
```
### 2. 📦 Create Virtual Environment & Install Dependencies
```
python -m venv venv 
source venv/bin/activate  # For Linux/Mac 
venv\Scripts\activate     # For Windows 

pip install -r requirements.txt 
```
### 3. 🛠 Configure Redis Cache
add this in your Django settings.py:
```
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
```
### 4. 🛠 Apply Migrations
```
python manage.py makemigrations <br>
python manage.py migrate
```
### 5. ▶️ Run the Server
```
python manage.py runserver
```
### 🔄 API Endpoints

| Method | Endpoint           | Description                  |
| ------ | ------------------ | ---------------------------- |
| GET    | `/api/blogs/`      | List all blog posts (cached) |
| POST   | `/api/blogs/`      | Create a new blog post       |
| GET    | `/api/blogs/<id>/` | Retrieve a post (cached)     |
| PATCH  | `/api/blogs/<id>/` | Partially update a post      |
| DELETE | `/api/blogs/<id>/` | Delete a post                |

🙌 Author
Nipun Lal RC
Python Full Stack Developer | Django Enthusiast
📫 LinkedIn | ✉️ nipunlal5@outlook.com
