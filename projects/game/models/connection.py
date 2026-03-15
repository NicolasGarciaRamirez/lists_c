import socket


class Connection:

    def __init__(self, host="localhost", port=5002):
        self.host = host
        self.port = port

    def initialize_server(self):

        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server.bind((self.host, self.port))

        server.listen()

        print("Servidor listo, esperando conexión...")

        return server

    def get_connection(self, server):

        conn, addr = server.accept()

        print("Cliente conectado:", addr)

        return conn

    def connect_client(self):

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        client.connect((self.host, self.port))

        return client