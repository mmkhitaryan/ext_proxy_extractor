from extractors.base import BaseExtractor
from extractors.common import Proxy

class VPNLYExtractor(BaseExtractor):
    @classmethod
    def get_proxies(cls):
        proxies = []
        data = cls.requests_instance.get(
            'https://s3.hub-vpn.com/servers.json'
        ).json()
    
        for raw_proxy in data:
            proxies.append(
                Proxy(
                    proxy_type=raw_proxy['proto'],
                    username=raw_proxy['user'],
                    password=raw_proxy['pass'],
                    ip=raw_proxy["host"],
                    region=raw_proxy['city']['country']['code'],
                )
            )
        return proxies
