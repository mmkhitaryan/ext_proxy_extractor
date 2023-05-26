import requests

class BaseExtractor():
    requests_instance = requests.Session()

    def get_proxies(self, *args, **kwargs):
        raise NotImplementedError
