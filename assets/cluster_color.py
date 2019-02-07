#!/usr/bin/env python3
import requests
import json

http_response = requests.get('http://127.0.0.1:9200/_cluster/health')
jsonresponse = json.loads(http_response.text)
print (jsonresponse['status'])
