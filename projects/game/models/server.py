import random
from connection import Connection
from colors import Colors


class GameServer:

    def __init__(self):

        self.aciertos = 0
        self.desaciertos = 0
        self.desaciertos_seguidos = 0
        self.game_result = None
        self.intentos = 0
        self.historial = []

        connection = Connection()

        self.server = connection.initialize_server()
        self.conn = connection.get_connection(self.server)

    def start_game(self):

        print(
            Colors.CYAN +
            "\n==============================\n"
            "      SERVIDOR INICIADO\n"
            "==============================\n"
            + Colors.END
        )

        while True:

            data = self.conn.recv(1024).decode()

            if data == "terminar":
                self.game_result = "terminado"
                break

            self.intentos += 1

            client_number = int(data)
            server_number = random.randint(1, 10)

            resultado = "ACIERTO" if client_number == server_number else "DESACIERTO"

            self.historial.append({
                "intento": self.intentos,
                "cliente": client_number,
                "servidor": server_number,
                "resultado": resultado
            })

            if resultado == "ACIERTO":

                self.aciertos += 1
                self.desaciertos_seguidos = 0

                message = (
                    f"\n{Colors.GREEN}"
                    "==============================\n"
                    f"        INTENTO #{self.intentos}\n"
                    "==============================\n"
                    f"🎲 Tu número: {client_number}\n"
                    f"🤖 Servidor: {server_number}\n"
                    "Resultado: ACIERTO\n"
                    "=============================="
                    f"{Colors.END}\n"
                )

            else:

                self.desaciertos += 1
                self.desaciertos_seguidos += 1

                errores_visual = "⚠️ " * self.desaciertos_seguidos

                message = (
                    f"\n{Colors.RED}"
                    "==============================\n"
                    f"        INTENTO #{self.intentos}\n"
                    "==============================\n"
                    f"🎲 Tu número: {client_number}\n"
                    f"🤖 Servidor: {server_number}\n"
                    "Resultado: DESACIERTO\n"
                    f"Desaciertos seguidos: {self.desaciertos_seguidos}\n"
                    f"{errores_visual}\n"
                    "=============================="
                    f"{Colors.END}\n"
                )

            self.conn.send(message.encode())

            if self.desaciertos_seguidos == 3:

                self.game_result = "ganaste"

                lose_message = (
                    f"\n{Colors.RED}"
                    "💀 PERDISTE 💀\n"
                    "El servidor tuvo 3 desaciertos seguidos.\n"
                    f"{Colors.END}"
                )

                self.conn.send(lose_message.encode())

                break

        self.show_results()

    def show_results(self):

        total = self.aciertos + self.desaciertos

        accuracy = (self.aciertos / total * 100) if total > 0 else 0

        if self.game_result == "ganaste":

            result_message = f"{Colors.GREEN}🎉 EL CLIENTE GANÓ 🎉{Colors.END}"

        elif self.game_result == "perdiste":

            result_message = f"{Colors.RED}💀 EL CLIENTE PERDIÓ 💀{Colors.END}"

        else:

            result_message = f"{Colors.WARNING}Juego terminado por el usuario{Colors.END}"

        results = (
            "\n==============================\n"
            "        RESULTADOS\n"
            "==============================\n"
            f"{result_message}\n\n"
            f"Aciertos del servidor: {self.aciertos}\n"
            f"Desaciertos del servidor: {self.desaciertos}\n"
            f"Porcentaje de aciertos del servidor: {accuracy:.2f}%\n"
            "==============================\n"
        )

        print(results)

        print("\nHistorial de jugadas\n")

        print("Intento | Cliente | Servidor | Resultado")
        print("-----------------------------------------")

        for intento in self.historial:

            print(
                f"{intento['intento']:>6} | "
                f"{intento['cliente']:>7} | "
                f"{intento['servidor']:>8} | "
                f"{intento['resultado']}"
            )

        self.conn.send(results.encode())

        self.conn.close()


if __name__ == "__main__":

    server = GameServer()
    server.start_game()