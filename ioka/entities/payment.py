import ioka
from ioka.abstract_api import AbstractAPI
import re


class Payment(AbstractAPI):
    API_URL = '/v2/orders'

    @classmethod
    def create_card_payment(
        self,
        order_id: str,
        pan: str = None,
        exp: str = None,
        cvc: str = None,
        card_id: str = None,
        **kwargs,
    ):
        if card_id is not None:
            kwargs["card_id"] = card_id
            return self.post(
                f"{ioka.hostname}{self.API_URL}/{order_id}/payments/card", data=kwargs
            )
        elif pan is not None and exp is not None and cvc is not None:
            if self.validate_card(pan=pan, exp=exp, cvc=cvc):
                kwargs["pan"] = pan
                kwargs["exp"] = exp
                kwargs["cvc"] = cvc
                return self.post(
                    f"{ioka.hostname}{self.API_URL}/{order_id}/payments/card", data=kwargs
                )
            else:
                raise ValueError("Invalid card details")

    @classmethod
    def get_payment(self, order_id: str, payment_id: str, **kwargs):
        return self.get(
            f"{ioka.hostname}{self.API_URL}/{order_id}/payments/{payment_id}", params=kwargs
        )

    @classmethod
    def validate_card(self, pan: str, exp: str, cvc: str):
        pan_match = re.match(r"^\d{12,19}$", pan)
        exp_match = re.match(r"^\d{2}/(\d{2})$", exp)
        cvc_match = re.match(r"^\d{3,4}$", cvc)
        return pan_match and exp_match and cvc_match
