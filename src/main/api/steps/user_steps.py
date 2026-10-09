from src.main.api.foundation.endpoint import EndPoint
from src.main.api.foundation.requesters.crud_requester import CrudRequester
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.create_user_secret_request import CreateUserSecretRequest
from src.main.api.models.credit_repay_request import CreditRepayRequest
from src.main.api.models.credit_request import CreditRequest
from src.main.api.models.transfer_request import TransferRequest
from src.main.api.models.user_deposit_request import DepositRequest
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.respounse_specs import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps


class UserSteps(BaseSteps):
    def create_account(self, create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username , password=create_user_request.password),
            EndPoint.CREATE_ACCOUNT,
            ResponseSpecs.request_created()
        ).post()
        return response
    def create_secret_account(self, create_user_secret_request: CreateUserSecretRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_secret_request.username, password=create_user_secret_request.password),
            EndPoint.CREATE_ACCOUNT,
            ResponseSpecs.request_created()
        ).post()
        return response
    def deposit(self, deposit_request: DepositRequest,create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            EndPoint.DEPOSIT,
            ResponseSpecs.request_ok()
        ).post(deposit_request)
        return response

    def deposit_invalid(self, deposit_request: DepositRequest,create_user_request: CreateUserRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            EndPoint.DEPOSIT,
            ResponseSpecs.request_bad()
        ).post(deposit_request)

    def credit(self, credit_request: CreditRequest,create_user_secret_request: CreateUserSecretRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_secret_request.username, password=create_user_secret_request.password),
            EndPoint.CREDIT_ACCOUNT,
            ResponseSpecs.request_created()
        ).post(credit_request)
        return response

    def credit_invalid(self, credit_request: CreditRequest,create_user_secret_request: CreateUserSecretRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username=create_user_secret_request.username, password=create_user_secret_request.password),
            EndPoint.CREDIT_ACCOUNT,
            ResponseSpecs.request_bad()
        ).post(credit_request)


    def transfer(self, transfer_request: TransferRequest,create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username,password=create_user_request.password),
            EndPoint.TRANSFER,
            ResponseSpecs.request_ok()
        ).post(transfer_request)
        return response
    def transfer_invalid(self, transfer_request: TransferRequest,create_user_request: CreateUserRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username,password=create_user_request.password),
            EndPoint.TRANSFER,
            ResponseSpecs.request_bad()
        ).post(transfer_request)


    def credit_repay(self,create_user_secret_request: CreateUserSecretRequest,credit_repay_request: CreditRepayRequest ):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_secret_request.username,password=create_user_secret_request.password),
            EndPoint.CREDIT_REPAY,
            ResponseSpecs.request_ok()
        ).post(credit_repay_request)
        return response
    def credit_repay_invalid(self, create_user_secret_request: CreateUserSecretRequest,credit_repay_request: CreditRepayRequest):
        CrudRequester(
            RequestSpecs.auth_headers(username=create_user_secret_request.username,password=create_user_secret_request.password),
            EndPoint.CREDIT_REPAY,
            ResponseSpecs.request_unprocessable()
        ).post(credit_repay_request)