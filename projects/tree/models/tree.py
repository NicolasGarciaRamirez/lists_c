from models.nodo import Node

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert(node.left, value)
        elif  value > node.value:
            node.right = self._insert(node.right, value)
        
        return node

    def search(self, value):
        return self._search(self.root, value)
    
    def _search(self, node, value):
        if node is None:
            return False
        
        if value == node.value:
            return True
        elif value < node.value:
            return self._search(node.left, value)
        elif value > node.value:
            return self._search(node.right, value)

    def delete(self, value):
        return self._delete(self.root, value)
    
    def _delete(self, node, value):
        if node is None:
            return node

        if value < node.left:
            node.left = self._delete(self.left, value)
        elif value > node.right:
            node.right = self._delete(self.right, value)
        else:
            if node.left is None:
                return node.right
            if node.left is None:
                return node.left

            sucesor = self._min(node.right)
            node.value = sucesor.value
            node.right = self._delete(node.right, sucesor.value)

        return node
    
    def _min(self, node):
        while node.left:
            node = node.left
        return node

    # Recorridos

    def print_value(self, node):
        print(node.value, end=" ")
        

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            self.print_value(node)
            self.inorder(node.right)


    def preorder(self, node):
        if node:
            self.print_value(node)
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            self.print_value(node)

    
    def count(self, node):
        if node is None:
            return 0
        
        return 1 + self.count(node.left) + self.count(node.right)

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.right), self.height(node.right))

    def show_tree(self):
        lines, _, _, _ = self._build_tree_string(self.root)
        for line in lines:
            print(line)
        
    def _build_tree_string(self, node):

        if node is None:
            return [], 0, 0, 0

        node_repr = str(node.value)

        # Nodo hoja
        if node.left is None and node.right is None:
            width = len(node_repr)
            height = 1
            middle = width // 2
            return [node_repr], width, height, middle

        # Solo hijo izquierdo
        if node.right is None:
            lines, n, p, x = self._build_tree_string(node.left)
            u = len(node_repr)

            first_line = (x + 1) * " " + (n - x - 1) * "_" + node_repr
            second_line = x * " " + "/" + (n - x - 1 + u) * " "

            shifted_lines = [line + u * " " for line in lines]

            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Solo hijo derecho
        if node.left is None:
            lines, n, p, x = self._build_tree_string(node.right)
            u = len(node_repr)

            first_line = node_repr + x * "_" + (n - x) * " "
            second_line = (u + x) * " " + "\\" + (n - x - 1) * " "

            shifted_lines = [u * " " + line for line in lines]

            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Dos hijos
        left, n, p, x = self._build_tree_string(node.left)
        right, m, q, y = self._build_tree_string(node.right)

        u = len(node_repr)

        first_line = (x + 1) * " " + (n - x - 1) * "_" + node_repr + y * "_" + (m - y) * " "
        second_line = x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "

        if p < q:
            left += [" " * n] * (q - p)
        elif q < p:
            right += [" " * m] * (p - q)

        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [l + u * " " + r for l, r in zipped_lines]

        return lines, n + m + u, max(p, q) + 2, n + u // 2