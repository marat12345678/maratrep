from src.main.api.models.base_model import BaseModel

# модель обработки при создании банковского счета

class CreateAccountScoreResponse(BaseModel):
    id: int
    number: str
    balance: float
