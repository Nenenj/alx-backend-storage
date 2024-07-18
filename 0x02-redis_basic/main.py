#!/usr/bin/env python3
"""
Main file to test the Cache class
"""

Cache = __import__('exercise').Cache
replay = __import__('exercise').replay

def main():
    cache = Cache()

    # Test storing data
    data = b"hello"
    key = cache.store(data)
    print(f"Generated key: {key}")

    # Test retrieving data
    retrieved_data = cache.get(key)
    print(f"Retrieved data: {retrieved_data}")

    # Test get_str
    data_str = "hello world"
    key_str = cache.store(data_str)
    print(f"Generated key for string: {key_str}")
    retrieved_str = cache.get_str(key_str)
    print(f"Retrieved string: {retrieved_str}")

    # Test get_int
    data_int = 123
    key_int = cache.store(data_int)
    print(f"Generated key for int: {key_int}")
    retrieved_int = cache.get_int(key_int)
    print(f"Retrieved int: {retrieved_int}")

    # Test call history
    print("Replay store call history:")
    replay(cache.store)

if __name__ == "__main__":
    main()
