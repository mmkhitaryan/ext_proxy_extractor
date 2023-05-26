"""
Simply, open manifest of the web extension chrome-extension://inligpkjkhbpifecbdjhmdpcfhnlelja/manifest.json

Then open /common.js and you find function getIps().
"""
from extractors.base import BaseExtractor
from extractors.common import Proxy

CHROME_VERSION = '107'

class ProxySpiderExtractor(BaseExtractor):
    @classmethod
    def get_proxies(cls):
        proxies = []
        data = cls.requests_instance.get(
            'https://proxy-spider.com/api/extension.json'
            '?email=anonymous@proxy-spider.com&password=UjsUwi23KisklOla;ds3242'
            '&version=1.0.7&action=login'
        ).json()

        assert data["status"] == 'ok'

        username = data["data"]["servers"]["5081"]["credentials"]["username"]
        password = data["data"]["servers"]["5081"]["credentials"]["password"]

        for raw_proxy in data["data"]["servers"]["5081"]['proxies']:
            proxies.append(
                Proxy(
                    proxy_type='http',
                    username=username,
                    password=password,
                    ip=raw_proxy["proxy"],
                    region=raw_proxy["country"]
                )
            )

        return proxies
