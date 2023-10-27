import socket
try:
  ip = input("please enter an ip address ")
    print(socket.gethostbyaddr(ip))
except socket.error as error:
    print(error)

#random commet
