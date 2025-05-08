from rpyc.utils import server
from typing import Optional
import time
#import provider
from provider.provider import Provider

def start_server():
    _server = server.ThreadedServer(
        Provider,
        protocol_config={},
        port=10000,
    )
    _server.start()
