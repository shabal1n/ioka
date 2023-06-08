from collections import namedtuple
import requests
import ioka
import json


class AbstractAPI:

    @classmethod
    def call_api(self, method, url, **kwargs):
        headers = {"API-KEY": ioka.api_key, "Content-Type": "application/json"}
        try:
            response = requests.request(method, url, headers=headers, **kwargs)
            if response.content:
                return self.json_to_object(response.json())
            elif response.status_code == 204 and method == "delete":
                return 'Success'
            return response
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
    
    @classmethod
    def json_to_object(self, response):
        if isinstance(response, list):
            return [self.json_to_object(item) for item in response]
        elif isinstance(response, dict):
            return namedtuple("GenericDict", response.keys())(*response.values())
        else:
            raise TypeError("Unknown type: {}".format(type(response)))

    @classmethod
    def get(self, url: str, params: dict = None):
        return self.call_api("get", url, params=params)

    @classmethod
    def post(self, url: str, data: dict = None):
        return self.call_api("post", url, json=data)
    
    @classmethod
    def patch(self, url: str, data: dict = None):
        return self.call_api("patch", url, json=data)
    
    @classmethod
    def delete(self, url: str, params: dict = None):
        return self.call_api("delete", url, params=params)