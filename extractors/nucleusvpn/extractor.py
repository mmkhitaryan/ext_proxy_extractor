from extractors.base import BaseExtractor
from extractors.common import Proxy

class NucleusVPNExtractor(BaseExtractor):
    @classmethod
    def get_proxies(cls):
        proxies = []
        data = cls.requests_instance.get(
            'https://api.nucleusvpn.com/api/proxy'
        ).json()

        for raw_proxy in data['proxy_list']:
            ip, port = raw_proxy["host"].split(':')
            proxies.append(
                Proxy(
                    proxy_type='http',
                    username='',
                    password='',
                    ip=ip,
                    port=int(port),
                    region=raw_proxy['country'],
                )
            )
        return proxies

EXTRACTOR = NucleusVPNExtractor