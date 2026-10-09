


import pytest

from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.generators.valid_generator import ValidGenerator
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.create_user_secret_request import CreateUserSecretRequest
from src.main.api.models.credit_request import CreditRequest
from src.main.api.models.user_deposit_request import DepositRequest


@pytest.fixture
def create_user_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(user_request)
    return user_request



@pytest.fixture
def create_user_account(api_manager, create_user_request):
    account_response = api_manager.user_steps.create_secret_account(create_user_request)
    return account_response




@pytest.fixture
def create_user_secret_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserSecretRequest)
    api_manager.admin_steps.create_user(user_request)
    return user_request




@pytest.fixture
def create_user_account_secret(api_manager, create_user_secret_request):
    account_response = api_manager.user_steps.create_secret_account(create_user_secret_request)
    return account_response



@pytest.fixture
def create_user_sender(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(user_request)
    return user_request

@pytest.fixture
def create_account_sender(api_manager,create_user_sender):
    account_response = api_manager.user_steps.create_secret_account(create_user_sender)
    return account_response

@pytest.fixture
def deposit_sender(api_manager, create_account_sender, create_user_sender):
    first_deposit = DepositRequest(
        accountId=create_account_sender.id,
        amount = ValidGenerator.deposit_valid_gen()
    )
    api_manager.user_steps.deposit(first_deposit, create_user_sender)

    second_deposit = DepositRequest(
        accountId=create_account_sender.id,
        amount= ValidGenerator.deposit_valid_gen()
    )
    return api_manager.user_steps.deposit(second_deposit, create_user_sender)


@pytest.fixture
def credit_secret_user(api_manager,create_user_secret_request, create_user_account_secret):
    user_deposit_request = DepositRequest(accountId=create_user_account_secret.id,amount=ValidGenerator.credit_amount_gen())
    api_manager.user_steps.deposit(user_deposit_request, create_user_secret_request)
    credit_request = CreditRequest(accountId=create_user_account_secret.id, amount=ValidGenerator.credit_amount_gen(), termMonths=ValidGenerator.CREDIT_TIME)
    credit_response = api_manager.user_steps.credit(credit_request, create_user_secret_request)
    return credit_response