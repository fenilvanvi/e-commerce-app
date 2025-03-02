import aiosqlite
from app.utils.database import DB_NAME


async def insert_order(order_id, user_id, item_ids, total_amount):
    async with aiosqlite.connect(DB_NAME) as db:
        try:
            await db.execute(
                "INSERT INTO orders (order_id, user_id, item_ids, total_amount, status) VALUES (?, ?, ?, ?, ?)",
                (order_id, user_id, item_ids, total_amount, "Pending"),
            )
            await db.commit()
        except aiosqlite.IntegrityError:
            return False
    return True


async def update_order_status(order_id, status, processed_at):
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute(
            "UPDATE orders SET status = ?, processed_at = ? WHERE order_id = ?",
            (status, processed_at, order_id),
        )
        await db.commit()


async def get_order_status(order_id):
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT status FROM orders WHERE order_id = ?", (order_id,)) as cursor:
            result = await cursor.fetchone()
    return result[0] if result else None


async def get_order_metrics():
    async with aiosqlite.connect(DB_NAME) as db:
        async with db.execute("SELECT COUNT(*) FROM orders") as cursor:
            total_orders = (await cursor.fetchone())[0]
        async with db.execute("SELECT COUNT(*) FROM orders WHERE status='Pending'") as cursor:
            pending_orders = (await cursor.fetchone())[0]
        async with db.execute("SELECT COUNT(*) FROM orders WHERE status='Completed'") as cursor:
            completed_orders = (await cursor.fetchone())[0]
        async with db.execute(
                "SELECT AVG(julianday(processed_at) - julianday(created_at)) * 86400 FROM orders "
                "WHERE status='Completed'"
        ) as cursor:
            avg_processing_time = (await cursor.fetchone())[0] or 0.0

    return {
        "total_orders": total_orders,
        "pending_orders": pending_orders,
        "completed_orders": completed_orders,
        "avg_processing_time_sec": round(avg_processing_time, 2)
    }
