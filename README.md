# E-commerce Order Management System

A FastAPI-based backend system for managing and processing e-commerce orders asynchronously using **SQLite, a task queue, and asyncio**.

---

## Features
- **Order Management**: Place orders, check status, and retrieve metrics.
- **Asynchronous Processing**: Orders are queued and processed in the background.
- **Metrics API**: Track total orders, pending/completed orders, and processing time.
- **Modular Architecture**: Organized into controllers, DAOs, routers, and utilities.

---

## 📁 Project Structure
```
e-commerce-app/
|-- app/
|   |-- __init__.py
|   |-- controllers/
|   |   |--__init__.py
|   |   |-- order_controller.py
|   |-- dao/
|   |   |-- __init__.py
|   |   |-- order_dao.py
|   |-- models/
|   |   |-- __init__.py
|   |   |-- order_model.py
|   |-- routers/
|   |   |-- __init__.py
|   |   |-- order_router.py
|   |-- utils/
|   |   |-- __init__.py
|   |   |-- database.py
|   |   |-- queue_worker.py
|   |-- main.py
|-- requirements.txt
|-- README.md
```

---

## Installation & Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the FastAPI Server
```bash
python -m app.main
```

---

## API Endpoints

### 1. Place an Order
- **Endpoint:** `POST /order/`
- **Request:**
```json
{
    "order_id": "123",
    "user_id": "user_1",
    "item_ids": "item_1,item_2",
    "total_amount": 99.99
}
```
- **Response:**
```json
{
    "message": "Order placed successfully",
    "order_id": "123"
}
```

#### cURL Example:
```bash
curl -X POST "http://127.0.0.1:8000/order/" -H "Content-Type: application/json" -d '{
    "order_id": "123",
    "user_id": "user_1",
    "item_ids": "item_1,item_2",
    "total_amount": 99.99
}'
```

---

### 2. Check Order Status
- **Endpoint:** `GET /order/{order_id}`
- **Response:**
```json
{
    "order_id": "123",
    "status": "Processing"
}
```

#### cURL Example:
```bash
curl -X GET "http://127.0.0.1:8000/order/123"
```

---

### 3. Get Order Processing Metrics
- **Endpoint:** `GET /metrics/`
- **Response:**
```json
{
    "total_orders": 10,
    "pending_orders": 2,
    "completed_orders": 8,
    "avg_processing_time_sec": 2.0
}
```

#### cURL Example:
```bash
curl -X GET "http://127.0.0.1:8000/metrics/"
```

---

## Design Decisions & Trade-offs

### Why FastAPI?
- **Asynchronous support** for high performance.
- **Automatic request validation** with Pydantic.
- **Swagger** documentation built-in.

### Why SQLite with a Queue?
- **Lightweight and easy to set up.**  
- **Supports ACID transactions** to ensure data integrity.  
- **Memory queue (`asyncio.Queue`)** is used to simulate real-world async processing.  

### Trade-offs
- **SQLite is not ideal for large-scale applications**. In production, **PostgreSQL or MySQL** would be better.
- **A proper message broker (e.g., RabbitMQ, Redis, Kafka) would be more scalable** for handling millions of orders.

---

## Assumptions
- Orders are **processed in FIFO order**.
- Each `order_id` is **unique**.
- **Processing time is simulated as 2 seconds per order**.
- In a real-world system, **users would authenticate before placing orders**.

---

## Future Improvements
- Use **PostgreSQL/MySQL** instead of SQLite.  
- Implement **Redis or RabbitMQ** for scalable background processing.  
- Add **authentication (JWT-based)** to secure API endpoints.  
- Introduce **unit tests** for API and database operations.  

---

## Run the API with Swagger UI
Once the FastAPI server is running, access the API documentation at:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---
