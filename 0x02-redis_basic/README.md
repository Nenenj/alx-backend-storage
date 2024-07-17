# Cache with Redis

This project provides a `Cache` class for storing data in Redis. It includes methods for initializing the Redis client, flushing the database, and storing data with a randomly generated key.

## Installation

1. Install Redis on Ubuntu:
    ```sh
    sudo apt-get -y install redis-server
    ```

2. Install the Redis Python client:
    ```sh
    pip3 install redis
    ```

3. Update Redis configuration to bind to localhost:
    ```sh
    sudo sed -i "s/bind .*/bind 127.0.0.1/g" /etc/redis/redis.conf
    ```

4. Start the Redis server:
    ```sh
    sudo service redis-server start
    ```

## Usage

To use the `Cache` class, create an instance and store data as shown below:

```python
#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache

cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))

