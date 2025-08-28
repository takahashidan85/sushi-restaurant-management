# System Architecture - Sushi Restaurant Management

## 1. Overview
The Sushi Restaurant Management System is a **Flask-based web application** that provides RESTful APIs for managing customers, sushi items, orders, and order details.  
The application is designed to demonstrate layered architecture with clear separation between presentation, application, domain, and infrastructure layers.

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
│ (Entities, core business     │
│   rules, data contracts)     │
└──────────────┬──────────────┘
               │
┌──────────────┴──────────────┐
│       Infrastructure         │
│ (SQLAlchemy ORM, Repos, DB)  │
└─────────────────────────────┘
```
- **Presentation**: Flask Blueprints (`customer_route.py`, `sushi_item_route.py`, `order_route.py`, `order_detail_route.py`) expose RESTful APIs. Swagger UI (`/apidocs`) provides interactive documentation.
- **Application**: Service classes (e.g., `CustomerService`, `OrderService`) handle business logic and orchestrate CRUD operations.
- **Domain**: Contains core entities and domain logic.
- **Infrastructure**: Implements repositories and SQLAlchemy models to interact with the database.

## 3. Components

### 3.1 Presentation Layer

- Framework: **Flask**
- Features:
    - API endpoints for CRUD operations
    - Swagger UI for API documentation (`flasgger` + `flask-swagger-ui`)

### 3.2 Application Layer

- Encapsulates business logic
- Services delegate requests from routes to repositories

### 3.3 Domain Layer

- Defines the business entities (Customer, Order, SushiItem, OrderDetail)
- Provides abstractions decoupled from persistence layer

### 3.4 Infrastructure Layer

- Database: **SQLAlchemy ORM**
- Migration tool: **Flask-Migrate (Alembic)**
- Supports **SQLite** (default) and **SQL Server** (via extension)

## 4. Database Design

See the [Entity Relationship Diagram (ERD)](ERD_SushiRestaurant.png) for table relationships.

Main entities:

- **Customer:** id, name, email
- **SushiItem:** id, name, price, description
- **Order:** id, customer_id, status
- **OrderDetail:** id, order_id, sushi_item_id, quantity

## 5. Deployment

### Local (development)

- Run Flask app directly with `.venv`
- Swagger UI available at `http://127.0.0.1:8000/apidocs`

### Docker (production-ready)

- Containerized using `Dockerfile`
- Run with `docker build` and `docker run`
- Gunicorn as WSGI server for better performance

## 6. Extensions

- **Flask** (framework)
- **SQLAlchemy** (ORM)
- **Flask-Migrate** (database migration)
- **Flasgger** (Swagger API docs)
- **Gunicorn** (production server, via Docker)