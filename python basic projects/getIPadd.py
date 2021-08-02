import socket as s
host = #url("somthing.com")

# it can only publish public ip address not someone's personal IP address

print(f'IP of {host} is {s.gethostbyname(host)}')