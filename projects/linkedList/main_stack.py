from structures.stack import Stack
from exceptions.read_exceptions import ReadInput


def show_menu():
    print("\n===== HISTORIAL DE ACCIONES =====")
    print("1. Registrar acción")
    print("2. Mostrar historial completo")
    print("3. Deshacer última acción")
    print("4. Mostrar primera acción registrada")
    print("5. Salir")

def register_action(stack):
    action = ReadInput.read_str("Ingrese la acción realizada: ")
    stack.push(action)
    print("Acción registrada correctamente.")


def show_history(stack):
    print("\nHistorial de acciones:")
    print(stack.display())


def undo_last_action(stack):
    removed = stack.pop()
    if removed:
        print(f"Última acción deshecha: {removed}")
    else:
        print("No hay acciones para deshacer.")


def show_first_action(stack):
    first = stack.first_action()
    if first:
        print(f"Primera acción registrada: {first}")
    else:
        print("El historial está vacío.")

def main():
    stack = Stack()

    actions = {
        1: lambda: register_action(stack),
        2: lambda: show_history(stack),
        3: lambda: undo_last_action(stack),
        4: lambda: show_first_action(stack),
    }

    while True:
        show_menu()
        option = ReadInput.read_int("Seleccione una opción: ")

        if option == 5:
            print("Saliendo del programa...")
            break

        action = actions.get(option)
        if action:
            action()
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()