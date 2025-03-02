from pydantic import BaseModel

class Order(BaseModel):
    order_id: str
    user_id: str
    item_ids: str  # Store item IDs as a comma-separated string
    total_amount: float
