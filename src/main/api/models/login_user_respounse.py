from src.main.api.models.base_model import BaseModel
# Базовая модель  ответа на заход юзера

#сделали доп модель чтоб обрабатывать вложеность !
class User(BaseModel):
    username: str
    role: str



class LoginUserResponse(BaseModel):
    token: str
    user: User

