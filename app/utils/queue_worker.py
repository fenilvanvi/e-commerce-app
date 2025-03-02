import asyncio
from app.controllers.order_controller import process_order

order_queue = asyncio.Queue()

async def process_orders():
    while True:
        order_id = await order_queue.get()
        await process_order(order_id)
        order_queue.task_done()


async def add_order_to_queue(order_id):
    await order_queue.put(order_id)
