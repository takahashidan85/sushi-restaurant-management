# System Architecture - Sushi Restaurant Management

## 1. Overview
The Sushi Restaurant Management System is a **Flask-based web application** that provides RESTful APIs for managing customers, sushi items, orders, and order details.  
It demonstrates **clean layered architecture** with separation of concerns and scalability in mind.

---

## 2. High-Level Architecture

```text
┌─────────────────────────────┐
│        Presentation          │
│  (Flask Routes + SwaggerUI)  │
└──────────────┬──────────────┘
               │
┌──────────────┴──────────────┐
│        Application           │
│ (Service layer: business     │
│  logic for CRUD operations)  │
└──────────────┬──────────────┘
               │
┌──────────────┴──────────────┐
│          Domain              │
│ (Entities, rules, contracts) │
└──────────────┬──────────────┘
               │
┌──────────────┴──────────────┐
│       Infrastructure         │
│ (SQLAlchemy ORM, Repos, DB)  │
└─────────────────────────────┘
```

---

## 3. Components

### 3.1 Presentation Layer
- **Framework**: Flask  
- **Features**:  
  - REST API endpoints (CRUD).  
  - Swagger UI (`/apidocs`).  
  - Request and response logging for debugging.  
- Example: `customer_route.py` defines `/customers` endpoints.

### 3.2 Application Layer
- **Services** orchestrate CRUD operations and enforce business rules.  
- Example:  
  - `CustomerService`: create customer only if email is unique.  
  - `OrderService`: validate order has at least one detail and ensure valid status transitions.  
  - `SushiItemService`: ensure sushi item price is non-negative.

### 3.3 Domain Layer
- **Entities**: Customer, Order, SushiItem, OrderDetail.  
- **Business rules**:  
  - Customer email must be unique.  
  - An Order must have at least one OrderDetail.  
  - Total price is calculated from `OrderDetails`.  
  - SushiItem price must be greater than or equal to zero.  
  - Order status transitions must follow predefined rules (e.g., `pending` → `completed`).

### 3.4 Infrastructure Layer
- **Database**: SQLAlchemy ORM.  
- **Repositories**: isolate DB logic.  
  - Example: `CustomerRepository.get_by_email(email)`.  
- **Migrations**: Flask-Migrate (Alembic).  
- **Supported DBs**: SQLite (default), SQL Server (via pyodbc).  
- **Logging**: Centralized logging for actions and errors.  

---

## 4. Database Design

See the [ERD](diagrams/erd/erd.png).  

### Main Entities
- **Customer**: id, name, email (unique).  
- **SushiItem**: id, name, price, description, category.  
- **Order**: id, customer_id (FK), status, order_type, create_time, total_price.  
- **OrderDetail**: id, order_id (FK), sushi_item_id (FK), quantity, unit_price.  

### Relationships
- Customer 1 — n Orders.  
- Order 1 — n OrderDetails.  
- SushiItem 1 — n OrderDetails.  

---

## 5. Deployment

### Local (development)
- Run Flask app in virtual environment.  
- Swagger UI: `http://127.0.0.1:8000/apidocs`.  

### Docker (production-ready)
- Built with `Dockerfile`.  
- Run with:  
  ```bash
  docker build -t sushi-app .
  docker run -p 8000:8000 --env-file .env sushi-app
  ```  
- **Gunicorn** is used as WSGI server.  
- Environment variable `DATABASE_URL` must be set inside `.env`.  

---

## 6. Extensions
- **Flask** (framework).  
- **SQLAlchemy** (ORM).  
- **Flask-Migrate** (migration).  
- **Flasgger** (Swagger docs).  
- **Gunicorn** (WSGI production).  
- **RotatingFileHandler** (logging).  

---

## 7. Future Enhancements
- Add caching layer (Redis).  
- Add background job processing (Celery).  
- Integrate JWT Authentication.  
- Add monitoring/logging (Prometheus + Grafana).  
- Implement role-based access control (RBAC) for admin and staff users.  
- Add support for PostgreSQL in production.  
- Enhance API rate limiting for better security.