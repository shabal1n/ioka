import ioka
from ioka.abstract_api import AbstractAPI
from ioka.entities.payment import Payment


class Card(AbstractAPI):
    API_URL = "/v2/customers"

    @classmethod
    def create_binding(self, customer_id: str, pan: str, exp: str, cvc: str, **kwargs):
        if Payment.validate_card(pan=pan, exp=exp, cvc=cvc):
            kwargs["pan"] = pan
            kwargs["exp"] = exp
            kwargs["cvc"] = cvc
            return self.post(
                f"{ioka.hostname}{self.API_URL}/{customer_id}/bindings", data=kwargs
            )
        else:
            raise ValueError("Invalid card details")

    @classmethod
    def get_cards(self, customer_id: str):
        return self.get(f"{ioka.hostname}{self.API_URL}/{customer_id}/cards")

    @classmethod
    def get_card_by_id(self, customer_id: str, card_id: str):
        return self.get(f"{ioka.hostname}{self.API_URL}/{customer_id}/cards/{card_id}")

    @classmethod
    def delete_card_by_id(self, customer_id: str, card_id: str):
        return self.delete(
            f"{ioka.hostname}{self.API_URL}/{customer_id}/cards/{card_id}"
        )
