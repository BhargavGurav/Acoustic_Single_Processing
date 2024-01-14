import socket
import psutil

HOST = '127.0.0.1'
PORT = 6514
# Get the address and port of the socket
sockname = socket.gethostname()
peername = socket.getservbyport()

# Get the number of bytes that have been sent and received over the socket
sent = psutil.net_io_counters()[sockname][0]
received = psutil.net_io_counters()[peername][0]

# Calculate the bandwidth of the socket
bandwidth = sent - received
print(bandwidth)
