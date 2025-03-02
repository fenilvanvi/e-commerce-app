from fastapi import APIRouter, HTTPException
from app.models.order_model import Order
from app.controllers import order_controller
from app.utils.queue_worker import add_order_to_queue

router = APIRouter()


@router.post("/order/")
async def create_order(order: Order):
    result = await order_controller.create_order(order)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])

    await add_order_to_queue(order.order_id)
    return result


@router.get("/order/{order_id}")
async def get_order_status(order_id: str):
    result = await order_controller.get_order_status(order_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result


@router.get("/metrics/")
async def get_metrics():
    return await order_controller.get_metrics()
