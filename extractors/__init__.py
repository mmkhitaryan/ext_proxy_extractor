import importlib

_EXTRACTORS = ['.proxy_spider', '.vpnly']
ALL_EXTRACTORS = set()

for extractor_name in _EXTRACTORS:
    extractor_package = importlib.import_module(extractor_name, package='extractors')
    
    ALL_EXTRACTORS.add(
        extractor_package.EXTRACTOR
    )
