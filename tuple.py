device = ("Router", "192.168.1.1", "Cisco")
print(device)

interface = "GigabitEthernet0", "up",
print(interface)

try:
    device[1] = "192.168.2.1"
except TypeError as e:
    print(e)

##Unpacking a Tuple##
name, ip, brand = device
print(f"Name: {name}, IP: {ip}, Brand: {brand}")

device_info = ("Router1", "172.16.0.1", "Juniper", 22)
endpoint = ("10.10.10.1", 443)