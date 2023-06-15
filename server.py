import socket
from _thread import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QPushButton, QWidget
from PyQt5.QtCore import pyqtSignal, QThread
import sys


client_sockets = []

HOST = socket.gethostbyname(socket.gethostname())
PORT = 1234


class ClientThread(QThread):
    received = pyqtSignal(str)

    def __init__(self, client_socket, addr):
        super().__init__()
        self.client_socket = client_socket
        self.addr = addr

    def run(self):
        print('>> Connected by:', self.addr[0], ':', self.addr[1])

        while True:
            try:
                data = self.client_socket.recv(1024)

                if not data:
                    print('>> Disconnected by', self.addr[0], ':', self.addr[1])
                    break

                received_message = data.decode()
                print('>> Received from', self.addr[0], ':', self.addr[1], received_message)

                with open(f"{self.addr[0]}.txt", "a", encoding='utf-8') as f:
                    f.write(received_message)

                for client in client_sockets:
                    if client != self.client_socket:
                        client.send(data)

                self.received.emit(received_message)

            except ConnectionResetError as e:
                print('>> Disconnected by', self.addr[0], ':', self.addr[1])
                break

        if self.client_socket in client_sockets:
            client_sockets.remove(self.client_socket)
            print('remove client list:', len(client_sockets))

        self.client_socket.close()


class LogWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Log Server")

        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def add_log(self, message):
        self.text_edit.append(message)


class Server(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        print('>> Server Start with IP:', HOST)
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen()

        while True:
            print('>> Wait')

            client_socket, addr = server_socket.accept()
            client_sockets.append(client_socket)

            client_thread = ClientThread(client_socket, addr)
            client_thread.received.connect(log_window.add_log)
            client_thread.start()

            print("접속 PC 수:", len(client_sockets))

        server_socket.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    log_window = LogWindow()
    log_window.show()

    server_thread = Server()
    server_thread.start()

    sys.exit(app.exec_())
