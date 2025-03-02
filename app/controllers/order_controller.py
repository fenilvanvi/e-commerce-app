from datetime import datetime, timezone
from app.dao import order_dao

async def create_order(order):
    success = await order_dao.insert_order(order.order_id, order.user_id, order.item_ids, order.total_amount)
    if not success:
        return {"error": "Order ID already exists"}
    return {"message": "Order placed successfully", "order_id": order.order_id}

async def process_order(order_id):
    processed_at = datetime.now(timezone.utc)
    await order_dao.update_order_status(order_id, "Completed", processed_at)

async def get_order_status(order_id):
    status = await order_dao.get_order_status(order_id)
    if status is None:
        return {"error": "Order not found"}
    return {"order_id": order_id, "status": status}

async def get_metrics():
    return await order_dao.get_order_metrics()
