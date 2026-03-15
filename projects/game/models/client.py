import threading
from connection import Connection
from colors import Colors


class GameClient:

    def __init__(self):

        connection = Connection()
        self.client = connection.connect_client()

    def start(self):

        print(
            Colors.BLUE +
            "\n==============================\n"
            "       JUEGO DE NÚMEROS\n"
            "==============================\n"
            + Colors.END
        )

        print("Ingresa un número entre 1 y 10")
        print("El servidor intentará adivinarlo")
        print("Si falla 3 veces seguidas, GANAS\n")

        thread = threading.Thread(target=self.play)

        thread.start()
        thread.join()

        self.client.close()

    def play(self):

        while True:

            number = input("🎲 Ingresa tu número: ")

            self.client.send(number.encode())

            response = self.client.recv(1024).decode()

            print(response)

            option = input(
                Colors.CYAN + "¿Continuar jugando? (si / terminar): " + Colors.END
            )

            if option.lower() == "terminar":

                self.client.send("terminar".encode())

                final_message = self.client.recv(4096).decode()

                print(final_message)

                break


if __name__ == "__main__":

    client = GameClient()
    client.start()
