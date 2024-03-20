try:
    result = 10/0
except ZeroDivisionError:
    print("Attempted to divide by zero. Setting result to None.")
    result = None
    print(f"Result: {result}")

try:
    network_device = {"ip": "192.168.1.1", "port": 22}
    print(network_device["hostname"])
except KeyError as e:
    print(f"Missing key: {e}")
except Exception as e:
    print(f"An unexpected error occured: {e}")