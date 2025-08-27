# 🍣 Sushi Restaurant Management API

---

## 1. Introduction  

This project is a **Sushi Restaurant Management System** that provides REST APIs for:  
- Managing Customers  
- Managing Sushi Items  
- Managing Orders  
- Managing Order Details  

The project follows a **layered/clean architecture**:  
- `domain` → core entities  
- `application` → business logic / services  
- `infrastructure` → persistence (database models, repositories)  
- `presentation` → REST API routes  

It uses **Flask**, **SQLAlchemy**, and optionally **Docker**. API documentation is provided with **Swagger UI (Flasgger)**.

---

## 2. Technologies  

- Python (>=3.9)  
- Flask, Flask-Migrate, SQLAlchemy  
- SQL Server (via pyodbc) or SQLite  
- Docker (optional)  
- Swagger UI (Flasgger)  

---

## 3. Project Structure  

```
sushi-restaurant-management/
│── wsgi.py
│── requirements.txt / pyproject.toml
│── app/
│ ├── init.py
│ ├── config.py
│ ├── extensions.py
│ ├── domain/
│ │ ├── customer.py
│ │ ├── sushi_item.py
│ │ ├── order.py
│ │ └── order_detail.py
│ ├── application/
│ │ ├── customer_service.py
│ │ ├── sushi_item_service.py
│ │ ├── order_service.py
│ │ └── order_detail_service.py
│ ├── infrastructure/
│ │ ├── models/
│ │ └── repositories/
│ └── presentation/
│ ├── customer_route.py
│ ├── sushi_item_route.py
│ ├── order_route.py
│ └── order_detail_route.py
│── migrations/ (if using Flask-Migrate)
```

---

## 4. Installation & Running (Local)

### 4.1. Setup environment
```
git clone https://github.com/takahashidan85/sushi-restaurant-management.git
cd sushi-restaurant-management
```

#### (Recommended) create virtual environment
```
python -m venv .venv
```

#### Activate virtual environment

CMD:
```
.venv\Scripts\activate
```
PowerShell:
```
.venv\Scripts\Activate.ps1
```
If you got error, run PowerShell as Administrator and execute:
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```
Press **Y** to process

Linux/macOS:
```
source .venv/bin/activate
```


### 4.2. Install dependencies

```
pip install --upgrade pip
pip install -r requirements.txt
```

### 4.3. Configure database

Update app/config.py for SQL Server or SQLite.
If using Flask-Migrate:
```
flask db init
flask db migrate
flask db upgrade
```

### 4.4. Run the app

```
export FLASK_APP=wsgi.py
export FLASK_ENV=development
```

```
flask run --host=0.0.0.0 --port=8000
```

Or run with Gunicorn:
```
pip install gunicorn
gunicorn --bind 0.0.0.0:8000 wsgi:app
```

## 5. Run with Docker (optional)

```
docker build -t sushi-app .
docker run -p 8000:8000 sushi-app
```
---

## 6. API Documentation & Swagger UI

If Swagger (Flasgger) is enabled, access API docs at:
```
http://localhost:8000/apidocs
```

Or OpenAPI JSON at:
```
http://localhost:8000/apispec_1.json
```

Main Endpoints:

**POST /customers/**, **GET /customers/**, **PUT /customers/<id>**, **DELETE /customers/<id>**
**POST /sushi_items/**, **GET /sushi_items/**, **PUT /sushi_items/<id>**, **DELETE /sushi_items/<id>**
**POST /orders/**, **GET /orders/**, **PUT /orders/<id>**, **DELETE /orders/<id>**
**POST /order_details/**, **GET /order_details/**, **PUT /order_details/<id>**, **DELETE /order_details/<id>**

---

## 7. Learning Objectives

Apply layered / clean architecture in software development.
Implement RESTful CRUD APIs with Flask.
Generate API documentation with Swagger.
Deploy application using Docker.

---

## 8. Future Improvements

Add authentication (JWT).
Build frontend (Web/Mobile).
Deploy to cloud (Heroku, DigitalOcean, etc.).
Add logging, unit testing, CI/CD workflows.

---

## 9. About the author

- **Name:** Trần Cát Đằng (Takahashi Dan)
- **Email:** catdangtran1@gmail.com
- **Discord:** TakahashiDan
- **Github:** https://github.com/takahashidan85

---

## 10. License

- MIT License
