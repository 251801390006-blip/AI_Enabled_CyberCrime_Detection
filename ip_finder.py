import socket

hostname = socket.gethostname()

ip = socket.gethostbyname(hostname)

print("IP Address:", ip)