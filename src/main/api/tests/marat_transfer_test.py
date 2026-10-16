import pytest
from sqlalchemy.orm import Session

from src.main.api.classes.api_manager import ApiManager
from src.main.api.db.crud.transaction_crud import TransactionCrud
from src.main.api.generators.valid_generator import ValidGenerator
from src.main.api.models.create_account_score_response import CreateAccountScoreResponse
from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.models.transfer_request import TransferRequest
from src.main.api.models.user_deposit_response import DepositResponse


@pytest.mark.api
class TestTransfer:
    @pytest.mark.parametrize(
        "amount",
        [ValidGenerator.send_transfer_gen()],
    )
    def test_transfer_valid(
        self,
        api_manager: ApiManager,
        create_user_sender: CreateUserRequest,
        create_account_sender: CreateAccountScoreResponse,
        create_user_account: CreateAccountScoreResponse,
        deposit_sender: DepositResponse,
        amount: int,
        db_session: Session,
    ):
        transfer_request = TransferRequest(
            fromAccountId=create_account_sender.id,
            toAccountId=create_user_account.id,
            amount=amount,
        )

        response = api_manager.user_steps.transfer(
            transfer_request,
            create_user_sender,
        )

        expected_balance = deposit_sender.balance - amount
        assert response.fromAccountIdBalance == expected_balance, (
            "После перевода баланс отправителя должен уменьшиться на сумму перевода"
        )

        transaction_from_db = TransactionCrud.get_by_from_account_id(
            db_session,
            create_account_sender.id,
            create_user_account.id,
            amount,
        )

        assert transaction_from_db is not None, (
            "транзакции должна быть в БД"
        )

    @pytest.mark.parametrize(
        "amount",
        [490, 10100],
    )
    def test_transfer_invalid(
        self,
        amount: int,
        api_manager: ApiManager,
        create_user_sender: CreateUserRequest,
        create_account_sender: CreateAccountScoreResponse,
        create_user_account: CreateAccountScoreResponse,
        deposit_sender: DepositResponse,
        db_session: Session,
    ):
        transfer_request = TransferRequest(
            fromAccountId=create_account_sender.id,
            toAccountId=create_user_account.id,
            amount=amount,
        )

        api_manager.user_steps.transfer_invalid(
            transfer_request,
            create_user_sender,
        )

        transaction_from_db = TransactionCrud.get_by_from_account_id(
            db_session,
            create_account_sender.id,
            create_user_account.id,
            amount,
        )

        assert transaction_from_db is None, (
            "запись о транзакции не должна появиться в БД"
        )