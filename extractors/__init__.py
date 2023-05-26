import importlib

_EXTRACTORS = ['proxy_spider', 'vpnly', '1clickvpn']
ALL_EXTRACTORS = set()

for extractor_name in _EXTRACTORS:
    extractor_package = importlib.import_module(f'.{extractor_name}.extractor', package='extractors')

    ALL_EXTRACTORS.add(
        extractor_package.EXTRACTOR
    )
