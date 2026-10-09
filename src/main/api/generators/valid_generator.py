import random


class ValidGenerator:
    CREDIT_TIME = 12
    @staticmethod
    def credit_valid_gen():
        amount =  random.randint(5000, 15000)
        termMonths = ValidGenerator.CREDIT_TIME
        return amount, termMonths

    @staticmethod
    def deposit_valid_gen():
        amount = 9000
        return amount


    @staticmethod
    def send_transfer_gen():
        amount = random.randint(500, 9000)
        return amount

    @staticmethod
    def credit_amount_gen():
        amount = 5000
        return amount

    @staticmethod
    def credit_amount_gen_invalid():
        amount = 4000
        return amount