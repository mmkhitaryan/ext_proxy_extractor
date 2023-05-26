from typing import Literal
from dataclasses import dataclass

@dataclass
class Proxy:
    proxy_type: Literal["http", "socks4", "socks5"]
    username: str
    password: str
    ip: str
    port: int
    region: str
