#!/usr/bin/env python3
import requests
http_response=requests.get('http://127.0.0.1:9200/_cat/shards')
lshard=http_response.text
if lshard.find('RELOCATING') == -1:
    print ('NOT RELOCATING')
else:
    print ('RELOCATING')