import socket
import threading
import receiver
import sender

if __name__ == '__main__':
    print(socket.gethostname())
    print(socket.gethostbyname(socket.gethostname()))

# EOF
