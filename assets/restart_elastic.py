#!/usr/bin/env python3
import requests
import json
import subprocess
import time
import sys

def readnodes():
    http_response = requests.get('http://127.0.0.1:9200/_cluster/health')
    jsonresponse = json.loads(http_response.text)
    return jsonresponse['number_of_nodes']

healthurl='http://127.0.0.1:9200/_cluster/health'
subprocess.run(["systemctl","restart","elasticsearch"])
while True:
    try:
        http_response = requests.get(healthurl)
    except requests.exceptions.ConnectionError as e:
        time.sleep(1)
    else:
        break
time.sleep(30)
sys.stdout.write(str(readnodes()))
