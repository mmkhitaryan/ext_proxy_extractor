from extractors.base import BaseExtractor
from extractors.common import Proxy

class OneClickVPNExtractor(BaseExtractor):
    @classmethod
    def get_proxies(cls):
        proxies = []
        data = cls.requests_instance.get(
            'https://1clickvpn.net/api/v1/servers/'
        ).json()

        for raw_proxy in data:
            for node in raw_proxy['nodes']:
                if credentials := raw_proxy.get('credentials'):
                    proxies.append(
                        Proxy(
                            proxy_type=node['schema'],
                            username=credentials['username'],
                            password=credentials['password'],
                            ip=node['host'],
                            port=node['port'],
                            region=raw_proxy['countryCode']
                        )
                    )

                proxies.append(
                    Proxy(
                        proxy_type=node['schema'],
                        username='',
                        password='',
                        ip=node['host'],
                        port=node['port'],
                        region=raw_proxy['countryCode']
                    )
                )
        return proxies

EXTRACTOR = OneClickVPNExtractor