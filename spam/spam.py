import random
import time

import requests

endpoints = ('users', '')


def run():
    while True:
        try:
            target = random.choice(endpoints)
            print(requests.get(f"http://app:5000/{target}", timeout=1))
        except:
            pass
        time.sleep(1)


run()

