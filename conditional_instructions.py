port_status = "down"
if port_status == "up":
    print("The port is operational")
else:
    print("The port is down")

port_speed = 1000
if port_speed == 100:
    print("FastEthernet port.")
elif port_speed == 1000:
    print("GigabitEthernet port.")
else:
    print("Speed unrecognized")