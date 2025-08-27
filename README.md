# 🍣 Sushi Restaurant Management API

Một ứng dụng quản lý nhà hàng sushi được xây dựng bằng **Flask + SQLAlchemy + Flask-Migrate**, sử dụng kiến trúc **application factory** và phân lớp **models / services / routes**.  
Dự án hỗ trợ **SQL Server** (qua `pyodbc`), dễ mở rộng và bảo trì.

---

## 🚀 Tính năng
- Quản lý **khách hàng (Customer)**
- Quản lý **món sushi (SushiItem)**
- Quản lý **đơn hàng (Order)**
- Quản lý **chi tiết đơn hàng (OrderDetail)**
- API RESTful đầy đủ CRUD

---

## ⚙️ Công nghệ
- Flask, Flask-Migrate, SQLAlchemy
- Microsoft SQL Server (qua pyodbc)

---

## 📂 Cấu trúc (tóm lược)
\`\`\`
sushi-restaurant-management-full/
│── wsgi.py
│── requirements.txt
│── app/
│   ├── __init__.py
│   ├── config.py
│   ├── extensions.py
│   ├── models/
│   │   ├── customer.py
│   │   ├── sushi_item.py
│   │   ├── order.py
│   │   └── order_detail.py
│   ├── application/
│   │   ├── customer_service.py
│   │   ├── sushi_item_service.py
│   │   ├── order_service.py
│   │   └── order_detail_service.py
│   └── presentation/
│       ├── customer_route.py
│       ├── sushi_item_route.py
│       ├── order_route.py
│       └── order_detail_route.py
\`\`\`

---

## 🔧 Cài đặt & chạy
1. Tạo venv và cài requirements
2. Config database trong `app/config.py`
3. Chạy migrate + upgrade
4. Chạy Flask:
\`\`\`bash
$env:FLASK_APP="wsgi.py"
$env:FLASK_ENV="development"
flask run
\`\`\`

---

## 📌 API Endpoints (demo)
- `POST /customers/`, `GET /customers/`, `PUT /customers/<id>`, `DELETE /customers/<id>`
- `POST /sushi_items/`, `GET /sushi_items/`, `PUT /sushi_items/<id>`, `DELETE /sushi_items/<id>`
- `POST /orders/`, `GET /orders/`, `DELETE /orders/<id>`
- `POST /order_details/`, `GET /order_details/`, `PUT /order_details/<id>`, `DELETE /order_details/<id>`

---

## 🧪 Test
Ví dụ tạo customer:
\`\`\`bash
curl -X POST http://127.0.0.1:5000/customers/ -H "Content-Type: application/json" -d '{"name": "Dan", "email": "dan@example.com"}'
\`\`\`

---

## 📜 License
MIT
