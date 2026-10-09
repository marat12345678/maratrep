import pytest
from src.main.api.classes.api_manager import ApiManager
from src.main.api.db.crud.credit_crud import CreditCrudDb
from src.main.api.generators.valid_generator import ValidGenerator
from src.main.api.models.create_user_secret_request import CreateUserSecretRequest
from src.main.api.models.credit_repay_request import CreditRepayRequest
from sqlalchemy.orm import Session
from src.main.api.models.credit_response import CreditResponse


@pytest.mark.api
class TestCreditRepay:
    @pytest.mark.parametrize("amount",[ValidGenerator.credit_amount_gen()])
    def test_CreditRepay_valid(self,api_manager:ApiManager, create_user_secret_request: CreateUserSecretRequest, credit_secret_user:CreditResponse, amount:int,db_session: Session):
        credit_repay_request = CreditRepayRequest(creditId=credit_secret_user.creditId, accountId=credit_secret_user.id , amount=amount)
        credit_response = api_manager.user_steps.credit_repay(create_user_secret_request,credit_repay_request  )
        assert credit_response.amountDeposited == credit_repay_request.amount
        credit_from_db = CreditCrudDb.get_credit_by_id(db_session, credit_secret_user.creditId)
        assert credit_from_db.balance == 0,"Кредит не погашен баланс не равен 0"

    @pytest.mark.parametrize("amount",[ValidGenerator.credit_amount_gen_invalid()])
    def test_CreditRepay_invalid(self,api_manager:ApiManager, create_user_secret_request:CreateUserSecretRequest,credit_secret_user:CreditResponse, amount:int, db_session: Session):
        credit_repay_request = CreditRepayRequest(creditId=credit_secret_user.creditId, accountId=credit_secret_user.id,amount=amount)
        api_manager.user_steps.credit_repay_invalid(create_user_secret_request, credit_repay_request)
        credit_from_db = CreditCrudDb.get_credit_by_id(db_session, credit_secret_user.creditId)
        assert credit_from_db.balance == -credit_secret_user.amount, "Сумма кредита изменилась"
