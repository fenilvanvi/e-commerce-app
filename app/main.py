import asyncio

import uvicorn
from fastapi import FastAPI
from app.routers import order_router
from app.utils.database import init_db
from app.utils.queue_worker import process_orders

app = FastAPI()

app.include_router(order_router.router)


async def start_server():
    config = uvicorn.Config(app, host="0.0.0.0", port=8000)
    server = uvicorn.Server(config)
    await server.serve()


async def main():
    await init_db()

    server_task = asyncio.create_task(start_server())
    order_processing_task = asyncio.create_task(process_orders())

    await asyncio.gather(server_task, order_processing_task)


if __name__ == "__main__":
    asyncio.run(main())
