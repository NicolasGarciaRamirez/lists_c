from models.tree import Tree
from exceptions.read_exceptions import ReadInput

def insert(tree):
    value = ReadInput.read_int("Ingrese un valor: ")
    tree.insert(value)

def search(tree):
    value = ReadInput.read_int("Ingrese un valor a buscar: ")
    if tree.buscar(value):
        print("Encontrado")
    else:
        print("No encontrado")

def delete(tree):
    value = ReadInput.read_int("Ingrese un valor a eliminar: ")
    tree.delete(value)
    print("Eliminado")

def inorder(tree):
    print("Inorder: ")
    tree.inorder(tree.root)
    print("")

def preorder(tree):
    print("Preorder: ")
    tree.preorder(tree.root)
    print("")

def postorder(tree):
    print("Postorder: ")
    tree.postorder(tree.root)
    print('')

def count(tree):
    print("Total nodos: ", tree.count(tree.root))

def height(tree):
    print("Altura: ", tree.height(tree.root))

def show_tree(tree):
    print("\nArbol actual:\n")
    tree.show_tree()

def show_menu():
    print("\n===== MENU ARBOL BINARIO =====")
    print("1. Insertar")
    print("2. Buscar")
    print("3. Eliminar")
    print("4. Inorder")
    print("5. Preorder")
    print("6. Postorder")
    print("7. Contar Nodos")
    print("8. Altura")
    print("9. Mostrar Arbol")
    print("10. Salir")

def main():
    tree = Tree()

    actions = {
        1: lambda: insert(tree),
        2: lambda: search(tree),
        3: lambda: delete(tree),
        4: lambda: inorder(tree),
        5: lambda: preorder(tree),
        6: lambda: postorder(tree),
        7: lambda: count(tree),
        8: lambda: height(tree),
        9: lambda: show_tree(tree)
    }

    while True:
        show_menu()
        option = ReadInput.read_int("Seleccione una opción: ")

        if option == 10:
            print("Saliendo del programa...")
            break

        action = actions.get(option)
        if action:
            action()
            
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()