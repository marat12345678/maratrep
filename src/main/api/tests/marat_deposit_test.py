import pytest
from sqlalchemy.orm import Session

from src.main.api.classes.api_manager import ApiManager
from src.main.api.db.crud.account_crud import AccountCrudDb
from src.main.api.generators.valid_generator import ValidGenerator
from src.main.api.models.create_account_score_response import CreateAccountScoreResponse
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.user_deposit_request import DepositRequest


@pytest.mark.api
class TestDeposit:
    @pytest.mark.parametrize(
        "amount",
        [ValidGenerator.deposit_valid_gen()],
    )
    def test_deposit_valid(
        self,
        api_manager: ApiManager,
        create_user_request: CreateUserRequest,
        create_user_account: CreateAccountScoreResponse,
        amount: int,
        db_session: Session,
    ):
        user_deposit_request = DepositRequest(
            accountId=create_user_account.id,
            amount=amount,
        )

        deposit_response = api_manager.user_steps.deposit(
            user_deposit_request,
            create_user_request,
        )

        assert deposit_response.balance == user_deposit_request.amount, "Баланс в ответе должен совпадать с суммой пополнения"


        account_from_db = AccountCrudDb.get_account_by_id(
            db_session,
            create_user_account.id,
        )

        assert account_from_db is not None, "Счёт должен существовать в БД"
        assert account_from_db.balance == deposit_response.balance, "Баланс счёта в БД должен совпадать с ответом"


    @pytest.mark.parametrize(
        "amount",
        [900, 9005],
    )
    def test_deposit_invalid(
        self,
        amount: int,
        api_manager: ApiManager,
        create_user_request: CreateUserRequest,
        create_user_account: CreateAccountScoreResponse,
        db_session: Session,
    ):
        user_deposit_request = DepositRequest(
            accountId=create_user_account.id,
            amount=amount,
        )

        api_manager.user_steps.deposit_invalid(
            user_deposit_request,
            create_user_request,
        )

        account_from_db = AccountCrudDb.get_account_by_id(
            db_session,
            create_user_account.id,
        )

        assert account_from_db is not None, "Счёт должен существовать в БД"
        assert account_from_db.balance == create_user_account.balance, "баланс счёта не должен измениться"
        