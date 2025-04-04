import sys
from multiprocessing.connection import Client

PORT = 1234

if __name__ == "__main__":
    # Verifica si se ha pasado un argumento al script
    if len(sys.argv) != 2:
        print("Uso: python client.py <mensaje>")
        sys.exit(1)

    # Obtiene el mensaje del argumento
    mensaje = sys.argv[1]

    # Crea la conexión con el servidor
    connection = Client(('localhost', PORT), authkey=b'password')

    # Envía el mensaje al servidor
    connection.send({'message': mensaje})

    # Espera la respuesta del servidor
    respuesta = connection.recv()
    print(respuesta)

    # Cierra la conexión
    connection.close()
if len(sys.argv) != 2:
    print("Uso: python client.py <mensaje>")
    sys.exit(1)

mensaje = sys.argv[1]

connection = Client(('192.168.112.1', 1234), authkey=b'password')
connection.send({'message': mensaje})
respuesta = connection.recv()
print(respuesta)
connection.close()