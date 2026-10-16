import pytest
from sqlalchemy.orm import Session

from src.main.api.classes.api_manager import ApiManager
from src.main.api.db.crud.credit_crud import CreditCrudDb
from src.main.api.generators.valid_generator import ValidGenerator
from src.main.api.models.create_account_score_response import CreateAccountScoreResponse
from src.main.api.models.create_user_secret_request import CreateUserSecretRequest
from src.main.api.models.credit_request import CreditRequest


@pytest.mark.api
class TestCreditRequest:
    @pytest.mark.parametrize(
        "amount, term_months",
        [ValidGenerator.credit_valid_gen()],
    )
    def test_credit_request_valid(
        self,
        api_manager: ApiManager,
        create_user_secret_request: CreateUserSecretRequest,
        create_user_account_secret: CreateAccountScoreResponse,
        amount: int,
        term_months: int,
        db_session: Session,
    ):
        credit_request = CreditRequest(
            accountId=create_user_account_secret.id,
            amount=amount,
            termMonths=term_months,
        )

        credit_response = api_manager.user_steps.credit(
            credit_request,
            create_user_secret_request,
        )

        assert credit_response.balance == credit_request.amount, "Баланс в ответе должен совпадать с суммой кредита"


        credit_from_db = CreditCrudDb.get_credit_by_id(
            db_session,
            credit_response.creditId,
        )

        assert credit_from_db is not None, "Кредит должен существовать в БД"
        assert credit_from_db.id == credit_response.creditId, "ID кредита  совпадать с ID в ответе API"


    @pytest.mark.parametrize(
        "amount, term_months",
        [
            (4900, ValidGenerator.CREDIT_TIME),
            (15100, ValidGenerator.CREDIT_TIME),
        ],
    )
    def test_credit_request_invalid(
        self,
        api_manager: ApiManager,
        create_user_secret_request: CreateUserSecretRequest,
        create_user_account_secret: CreateAccountScoreResponse,
        amount: int,
        term_months: int,
        db_session: Session,
    ):
        credit_request = CreditRequest(
            accountId=create_user_account_secret.id,
            amount=amount,
            termMonths=term_months,
        )

        api_manager.user_steps.credit_invalid(
            credit_request,
            create_user_secret_request,
        )

        credit_from_db = CreditCrudDb.get_credit_by_id_invalid(
            db_session,
            create_user_account_secret.id,
        )

        assert credit_from_db is None, "Кредит не должен создаваться при недопустимой сумме"