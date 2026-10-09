from src.main.api.models.base_model import BaseModel

#модель для обработки ответа на создание нового юзера

class CreateUserResponse(BaseModel):
    id : int
    username : str
    password :str
    role : str
