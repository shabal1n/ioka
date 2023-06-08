import ioka
from ioka.abstract_api import AbstractAPI

class Customer(AbstractAPI):

    API_URL = '/v2/customers'

    @classmethod
    def create_customer(self, **kwargs):
        return self.post(f"{ioka.hostname}{self.API_URL}", data=kwargs)
    
    @classmethod
    def get_customers(self, **kwargs):
        return self.get(f"{ioka.hostname}{self.API_URL}", params=kwargs)
    
    @classmethod
    def get_customer_by_id(self, customer_id: str):
        return self.get(f"{ioka.hostname}{self.API_URL}/{customer_id}")
    
    @classmethod
    def get_customer_events(self, customer_id: str):
        return self.get(f"{ioka.hostname}{self.API_URL}/{customer_id}/events")
    
    @classmethod
    def delete_customer_by_id(self, customer_id: str):
        return self.delete(f"{ioka.hostname}{self.API_URL}/{customer_id}")