# ext_proxy_extractor
To test a proxy, you can use:
```
curl --proxy-basic -x https://username:password@ip:port https://google.com -vvv
```
Last time I checked, they all worked (except ones that require paid subscription)!

TODO:
- [ ] Make 10 integrations
- [ ] Unit tests
- [ ] Proxy checker
- [ ] Mitmproxy integration, so it can automatically switch between dead/alive proxies and load balance
