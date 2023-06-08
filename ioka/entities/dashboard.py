import ioka
from ioka.abstract_api import AbstractAPI

class Dashboard(AbstractAPI):
    API_URL = "/v2/dashboard/payments"

    @classmethod
    def search_dashboard_payments(self, **kwargs):
        return self.get(f"{ioka.hostname}{self.API_URL}", params=kwargs)
    
    @classmethod
    def export_dashboard_payments(self, **kwargs):
        return self.get(f"{ioka.hostname}{self.API_URL}/export", params=kwargs)