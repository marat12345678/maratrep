from requests import Response
from http import HTTPStatus


#Проверяем коды
class ResponseSpecs:
    #проверяем 200тый код в ответе
    @staticmethod
    def request_ok():
        def confirm(response: Response):
            assert response.status_code == HTTPStatus.OK , response.text

        return confirm

    #проверяем 201 код в ответе
    @staticmethod
    def request_created():
        def confirm(response: Response):
            assert response.status_code == HTTPStatus.CREATED , response.text
        return confirm

    #проверяем 400 код
    @staticmethod
    def request_bad():
        def confirm(response: Response):
            assert response.status_code == HTTPStatus.BAD_REQUEST , response.text
        return confirm

    #проверяем 422 код
    @staticmethod
    def request_unprocessable():
        def confirm(response: Response):
            assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY, response.text
        return confirm


    