import socket
def check_port(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('127.0.0.1', port)) == 0
print("Port 5000 is open:", check_port(5000))
print("Port 3000 is open:", check_port(3000))
