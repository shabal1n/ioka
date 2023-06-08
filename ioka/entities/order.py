import ioka
from ioka.abstract_api import AbstractAPI


class Order(AbstractAPI):
    API_URL = "/v2/orders"

    @classmethod
    def create_order(self, **kwargs):
        return self.post(f"{ioka.hostname}{self.API_URL}", data=kwargs)
    
    @classmethod
    def capture_order(self, order_id: str, **kwargs):
        return self.post(f"{ioka.hostname}{self.API_URL}/{order_id}/capture", data=kwargs)
    
    @classmethod
    def cancel_order(self, order_id: str, **kwargs):
        return self.post(f"{ioka.hostname}{self.API_URL}/{order_id}/cancel", data=kwargs)
    
    @classmethod
    def refund_order(self, order_id: str, **kwargs):
        return self.post(f"{ioka.hostname}{self.API_URL}/{order_id}/refunds", data=kwargs)

    @classmethod
    def get_orders(self, **kwargs):
        return self.get(f"{ioka.hostname}{self.API_URL}", params=kwargs)
    
    @classmethod
    def get_order_by_id(self, order_id: str, **kwargs):
        return self.get(f"{ioka.hostname}{self.API_URL}/{order_id}", params=kwargs)
    
    @classmethod
    def get_order_events(self, order_id: str, **kwargs):
        return self.get(f"{ioka.hostname}{self.API_URL}/{order_id}/events", params=kwargs)
    
    @classmethod
    def get_refunds(self, order_id: str, **kwargs):
        return self.get(f"{ioka.hostname}{self.API_URL}/{order_id}/refunds", params=kwargs)
    
    @classmethod
    def get_refund_by_id(self, order_id: str, refund_id: str, **kwargs):
        return self.get(f"{ioka.hostname}{self.API_URL}/{order_id}/refunds/{refund_id}", params=kwargs)