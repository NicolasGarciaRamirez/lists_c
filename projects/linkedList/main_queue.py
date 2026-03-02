from structures.queue import Queue
from exceptions.read_exceptions import ReadInput


def add_requests(queue):
    n = ReadInput.read_int("Ingrese el número de solicitudes: ")

    for i in range(n):
        student_id = ReadInput.read_str(f"Ingrese ID del estudiante #{i + 1}: ")
        reason = ReadInput.read_str("Ingrese el motivo de la solicitud: ")
        queue.enqueue(student_id, reason)

    print("Solicitudes registradas correctamente.")


def show_requests(queue):
    print("\nSolicitudes pendientes:")
    print(queue.display())


def attend_request(queue):
    removed = queue.dequeue()
    if removed:
        print(
            f"Solicitud atendida -> ID: {removed.student_id}, Motivo: {removed.reason}"
        )
    else:
        print("No hay solicitudes para atender.")


def show_count(queue):
    print(f"Solicitudes en espera: {queue.size()}")

def show_menu():
    print("\n===== COLA DE SOLICITUDES =====")
    print("1. Registrar solicitudes")
    print("2. Mostrar solicitudes pendientes")
    print("3. Atender primera solicitud")
    print("4. Mostrar cantidad de solicitudes")
    print("5. Salir")

def main():
    queue = Queue()

    actions = {
        1: lambda: add_requests(queue),
        2: lambda: show_requests(queue),
        3: lambda: attend_request(queue),
        4: lambda: show_count(queue),
    }

    while True:
        show_menu()
        option = ReadInput.read_int("Seleccione una opción: ")

        if option == 5:
            print("Saliendo del sistema de solicitudes...")
            break

        action = actions.get(option)
        if action:
            action()
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
