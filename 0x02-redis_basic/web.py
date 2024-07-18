#!/usr/bin/env python3
"""In this tasks, we will implement a get_page function
(prototype: def get_page(url: str) -> str:). The core of
the function is very simple. It uses the requests module
to obtain the HTML content of a particular URL and returns it.

Start in a new file named web.py and do not reuse the code
written in exercise.py.

Inside get_page track how many times a particular URL was
accessed in the key "count:{url}" and cache the result with
an expiration time of 10 seconds.

Tip: Use http://slowwly.robertomurray.co.uk to simulate
a slow response and test your caching."""


import redis
import requests
from typing import Callable
from functools import wraps

r = redis.Redis()


def url_access_count(method: Callable) -> Callable:
    """decorator for get_page function"""
    @wraps(method)
    def wrapper(url: str) -> str:
        """wrapper function"""
        key = "cached:" + url
        key_count = "count:" + url
        # Check if the URL is cached
        cached_value = r.get(key)
        if cached_value:
            return cached_value.decode("utf-8")

        # Get new content and update cache
        html_content = method(url)

        r.incr(key_count)
        r.setex(key, 10, html_content)
        return html_content
    return wrapper


@url_access_count
def get_page(url: str) -> str:
    """obtain the HTML content of a particular"""
    try:
        results = requests.get(url)
        return results.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return ""

if __name__ == "__main__":
    url = 'http://www.google.com'
    print(get_page(url))
    print(get_page(url))

    # Check the access count
    key_count = "count:" + url
    print(r.get(key_count).decode("utf-8"))
