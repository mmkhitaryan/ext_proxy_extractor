import requests

# TODO: move request+proxy extraction as strategy pattern
# in most of the extractors we only have request and json parsing logic
# to avoid boilerplating this logic should be placed in strategy class
class BaseExtractor():
    requests_instance = requests.Session()

    def get_proxies(self, *args, **kwargs):
        raise NotImplementedError
