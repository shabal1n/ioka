import ioka
from ioka.abstract_api import AbstractAPI

class Webhook(AbstractAPI):

    API_URL = "/v2/webhooks"

    @classmethod
    def create_webhook(self, url: str, events: list):
        return self.post(f"{ioka.hostname}{self.API_URL}", data={"url": url, "events": events})
    
    @classmethod
    def get_webhooks(self):
        return self.get(f"{ioka.hostname}{self.API_URL}")
    
    @classmethod
    def get_webhook_by_id(self, webhook_id: str):
        return self.get(f"{ioka.hostname}{self.API_URL}/{webhook_id}")
    
    @classmethod
    def update_webhook_by_id(self, webhook_id: str, **kwargs):
        return self.patch(f"{ioka.hostname}{self.API_URL}/{webhook_id}", data=kwargs)
    
    @classmethod
    def delete_webhook_by_id(self, webhook_id: str):
        return self.delete(f"{ioka.hostname}{self.API_URL}/{webhook_id}")