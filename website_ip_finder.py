import socket

website = input("Enter Website: ")

ip = socket.gethostbyname(website)

print("IP Address:", ip)