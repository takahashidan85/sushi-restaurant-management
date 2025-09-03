# API Documentation - Sushi Restaurant Management

This REST API manages customers, sushi menu items, orders, and order details.  
All responses are in JSON format. 

---

Base URL: http://localhost:8000/

---

## 1. Summary Table

| Method | Path                      | Description                          | Tag        |
|--------|---------------------------|--------------------------------------|------------|
| POST   | /customers                | Create a new customer                | Customer   |
| GET    | /customers                | List all customers                   | Customer   |
| GET    | /customers/{id}           | Get customer by ID                   | Customer   |
| PUT    | /customers/{id}           | Update customer                      | Customer   |
| DELETE | /customers/{id}           | Delete customer                      | Customer   |
| POST   | /sushi-items              | Create a new sushi item              | SushiItem  |
| GET    | /sushi-items              | List all sushi items                 | SushiItem  |
| GET    | /sushi-items/{id}         | Get sushi item by ID                 | SushiItem  |
| PUT    | /sushi-items/{id}         | Update sushi item                    | SushiItem  |
| DELETE | /sushi-items/{id}         | Delete sushi item                    | SushiItem  |
| POST   | /orders                   | Create a new order                   | Order      |
| GET    | /orders                   | List all orders                      | Order      |
| GET    | /orders/{id}              | Get order by ID                      | Order      |
| PUT    | /orders/{id}              | Update order                         | Order      |
| DELETE | /orders/{id}              | Delete order                         | Order      |
| PATCH  | /orders/{id}/status       | Update order status                  | Order      |
| PATCH  | /orders/{id}/force-status | Force update order status (admin)    | Order      |
| POST   | /order-details            | Create order detail                  | OrderDetail|
| GET    | /order-details            | List all order details               | OrderDetail|
| GET    | /order-details/{id}       | Get order detail by ID               | OrderDetail|
| PUT    | /order-details/{id}       | Update order detail                  | OrderDetail|
| DELETE | /order-details/{id}       | Delete order detail                  | OrderDetail|

---

## 2. Customer APIs

### POST /customers
Description: Create a new customer.

Request Body:
{
  "name": "Alice",
  "email": "alice@example.com"
}

Responses:
- 201 Created:
  {"status": "success", "message": "Customer created"}
- 422 Validation Error
- 409 Customer already exists

---

### GET /customers
Description: List all customers.

Response 200:
[
  {"id": 1, "name": "Alice", "email": "alice@example.com"}
]

---

### GET /customers/{id}
Description: Get customer by ID.

Path Parameter:
- id (integer, required)

Responses:
- 200 Customer retrieved
- 404 Customer not found

---

### PUT /customers/{id}
Description: Update customer.

Path Parameter:
- id (integer, required)

Request Body:
{
  "name": "Alice Updated",
  "email": "alice_new@example.com"
}

Responses:
- 200 Customer updated
- 404 Customer not found

---

### DELETE /customers/{id}
Description: Delete customer.

Path Parameter:
- id (integer, required)

Responses:
- 200 OK:
  {"status": "success", "message": "Customer deleted"}
- 404 Customer not found

---

## 3. Sushi Item APIs

### POST /sushi-items
Description: Create a new sushi item.

Request Body:
{
  "name": "Salmon Roll",
  "price": 5.5,
  "category": "Rolls",
  "description": "Fresh salmon with rice"
}

Responses:
- 201 Sushi item created
- 422 Validation Error

---

### GET /sushi-items
Description: List all sushi items.

Response 200: JSON array of items.

---

### GET /sushi-items/{id}
Description: Get sushi item by ID.

Path Parameter:
- id (integer, required)

Responses:
- 200 Sushi item retrieved
- 404 Sushi item not found

---

### PUT /sushi-items/{id}
Description: Update sushi item.

Path Parameter:
- id (integer, required)

Request Body:
{
  "name": "Tuna Roll",
  "price": 6.0,
  "category": "Rolls",
  "description": "Fresh tuna with rice"
}

Responses:
- 200 Sushi item updated
- 404 Sushi item not found

---

### DELETE /sushi-items/{id}
Description: Delete sushi item.

Path Parameter:
- id (integer, required)

Responses:
- 200 OK:
  {"status": "success", "message": "Sushi item deleted"}
- 404 Sushi item not found

---

## 4. Order APIs

### POST /orders
Description: Create a new order.

Request Body:
{
  "customer_id": 1,
  "order_type": "dine-in"
}

Responses:
- 201 Order created
- 422 Validation Error

---

### GET /orders
Description: List all orders.

Response 200: JSON array of orders.

---

### GET /orders/{id}
Description: Get order by ID.

Path Parameter:
- id (integer, required)

Responses:
- 200 Order retrieved
- 404 Order not found

---

### PUT /orders/{id}
Description: Update order.

Path Parameter:
- id (integer, required)

Request Body:
{
  "customer_id": 2
}

Responses:
- 200 Order updated
- 404 Order not found

---

### DELETE /orders/{id}
Description: Delete order.

Path Parameter:
- id (integer, required)

Responses:
- 200 OK:
  {"status": "success", "message": "Order deleted"}
- 404 Order not found

---

### PATCH /orders/{id}/status
Description: Update order status.

Path Parameter:
- id (integer, required)

Request Body:
{
  "new_status": "completed"
}

Responses:
- 200 Order status updated
- 400 Invalid status transition
- 404 Order not found

---

### PATCH /orders/{id}/force-status
Description: Force update order status (admin only).

Path Parameter:
- id (integer, required)

Request Body:
{
  "new_status": "cancelled"
}

Responses:
- 200 Order status force-updated
- 422 Validation Error
- 500 Server Error

---

## 5. Order Detail APIs

### POST /order-details
Description: Create order detail.

Request Body:
{
  "order_id": 1,
  "sushi_item_id": 2,
  "quantity": 3
}

Responses:
- 201 Order detail created
- 422 Validation Error

---

### GET /order-details
Description: List all order details.

Response 200: JSON array of order details.

---

### GET /order-details/{id}
Description: Get order detail by ID.

Path Parameter:
- id (integer, required)

Responses:
- 200 Order detail retrieved
- 404 Order detail not found

---

### PUT /order-details/{id}
Description: Update order detail.

Path Parameter:
- id (integer, required)

Request Body:
{
  "quantity": 5
}

Responses:
- 200 Order detail updated
- 404 Order detail not found

---

### DELETE /order-details/{id}
Description: Delete order detail.

Path Parameter:
- id (integer, required)

Responses:
- 200 OK:
  {"status": "success", "message": "Order detail deleted"}
- 404 Order detail not found

---

## 6. Common Error Codes

- 400 Bad Request: Invalid request or invalid status transition.
- 404 Not Found: Resource does not exist.
- 409 Conflict: Resource already exists.
- 422 Validation Error: Missing/invalid fields.
- 500 Internal Server Error: Unexpected error.
