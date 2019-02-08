#!/usr/bin/env python3
import sys
import requests
http_response=requests.get('http://127.0.0.1:9200/_cat/shards')
lshard=http_response.text
if lshard.find('RELOCATING') == -1:
    sys.stdout.write('NOT RELOCATING')
else:
    sys.stdout.write('RELOCATING')