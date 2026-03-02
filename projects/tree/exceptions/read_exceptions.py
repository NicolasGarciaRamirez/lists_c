MENSAJE_INVALIDO = "Valor ingresado invalido. Porfavor ingresa un"

class ReadInput:
    @staticmethod
    def read_input(prompt, cast_func, tipo):
        while True:
            try:
                return cast_func(input(prompt))
            except ValueError:
                print(MENSAJE_INVALIDO + f" {tipo}")

    @staticmethod
    def read_str(prompt):
        return ReadInput.read_input(prompt, str, "texto")

    @staticmethod
    def read_int(prompt):
        return ReadInput.read_input(prompt, int, "entero")
