#!/usr/bin/env python

import requests
import os
from pprint import pprint

URL = 'https://www.dillards.com'

response = requests.get(URL)

print(response)

if response.status_code == requests.codes.OK:
    for header, value in sorted(response.headers.items()):
        print(header, value)

print('-' * 60)

print(response.content.decode())

IMAGE_URL = 'https://dimg.dillards.com/is/image/DillardsZoom/nav/tommy-bahama-grate-outdoors-short-sleeve-tee/05194854_zi_pomodoro__02_ai.jpg'


response = requests.get(IMAGE_URL)

with open('grate_outdoors.jpg', 'wb') as great_out:
    great_out.write(response.content)

os.system('open grate_outdoors.jpg')














