from dataclasses import dataclass
from enum import Enum
from typing import Optional, Type

from src.main.api.models.base_model import BaseModel
from src.main.api.models.create_account_score_response import CreateAccountScoreResponse
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.create_user_respounse import CreateUserResponse
from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.models.credit_repay_response import CreditRepayResponse
from src.main.api.models.credit_request import CreditRequest
from src.main.api.models.credit_response import CreditResponse
from src.main.api.models.login_user_request import LoginUserRequest
from src.main.api.models.login_user_respounse import LoginUserResponse
from src.main.api.models.transfer_request import TransferRequest
from src.main.api.models.transfer_response import TransferResponse
from src.main.api.models.user_deposit_request import DepositRequest
from src.main.api.models.user_deposit_response import DepositResponse


@dataclass
class EndPointConfiguration:
    url : str
    request_model : Optional[Type[BaseModel]]
    response_model: Optional[Type[BaseModel]]


class CreditReques:
    pass


class EndPoint(Enum):
    ADMIN_CREATE_USER = EndPointConfiguration(
        request_model = CreateUserRequest,
        url = "/admin/create",
        response_model = CreateUserResponse
    )

    ADMIN_DELETE_USER = EndPointConfiguration(
        request_model = None,
        url = "/admin/users",
        response_model = None

    )
    LOGIN_USER = EndPointConfiguration(
        request_model = LoginUserRequest,
        url = "/auth/token/login",
        response_model = LoginUserResponse
    )


    CREATE_ACCOUNT = EndPointConfiguration(
        request_model = None,
        url = "/account/create",
        response_model = CreateAccountScoreResponse
    )

    DEPOSIT = EndPointConfiguration(
        request_model = DepositRequest,
        url = "/account/deposit",
        response_model = DepositResponse
    )

    CREDIT_ACCOUNT = EndPointConfiguration(
        request_model = CreditRequest,
        url = "/credit/request",
        response_model = CreditResponse
    )

    TRANSFER = EndPointConfiguration(
        request_model = TransferRequest,
        url = "/account/transfer",
        response_model = TransferResponse
    )

    CREDIT_REPAY = EndPointConfiguration(
        request_model = CreditRepayRequest,
        url = "/credit/repay",
        response_model = CreditRepayResponse
    )