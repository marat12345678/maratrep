from src.main.api.models.base_model import BaseModel


# модель для захода в акаунт
class LoginUserRequest(BaseModel):
    username: str
    password: str

