import hashlib

class Archivo():
    
    def __init__(self, nombre) -> None:
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    def leer(self):
        with open(self.__nombre, "r") as f:
            data = f.read()
        return data
        
class Codificacion():

    def __init__(self):
        pass

    def codificar(self, codigo, data:str):
        if codigo == "md5":
            resultado = hashlib.md5(data.encode()).hexdigest()
        elif codigo == "sha256":
            resultado = hashlib.sha256(data.encode()).hexdigest()
        elif codigo == "sha3":
            resultado = hashlib.sha3_224(data.encode()).hexdigest()
        else:
            print("Error de codificacion.")
        return resultado

def main():
    archivo = Archivo("archivo.txt")
    data = archivo.leer()
    codificacion = Codificacion()
    inp = input("Ingrese codificacion: ")
    resultado = codificacion.codificar(inp, data)
    print(resultado)

if __name__ == '__main__':
    main()