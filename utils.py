import http.client
import json
from dotenv import load_dotenv
import os
import time

class Utils:
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def api_call(url) -> json.loads:
        load_dotenv()
        key = os.getenv('api_key')
        url = url + f"?api_key={key}"
        conn = http.client.HTTPSConnection("api.sportradar.com")
        conn.request("GET", url)
        res = conn.getresponse()
        data = res.read()
        data = json.loads(data)
        time.sleep(1.1)
        return data