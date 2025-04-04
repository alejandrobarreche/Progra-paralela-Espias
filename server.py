from multiprocessing.connection import Listener
import queue

PORT = 1234
GLOBAL_LISTENER = "0.0.0.0"
password = b'password'

listener = Listener((GLOBAL_LISTENER, PORT), authkey=password)


# Tareas
queue.Queue = {
    "Intercepta y suma los dígitos de 274961": 2 + 7 + 4 + 9 + 6 + 1,  # 29
    "Descifra este anagrama: 'otnerc' (pista: moneda)": "centro",
    "Ubica la letra más frecuente en 'infiltración'": "i",
    "Convierte 1337 a binario (es una pista numérica)": bin(1337),  # '0b10100111001'
    "Cuenta las vocales en 'comunicacionesencriptadas'": sum(1 for c in 'comunicacionesencriptadas' if c in 'aeiou'),  # 12
    "Calcula raíz cuadrada entera de 762423": int(762423 ** 0.5),  # 873
    "¿Es primo el número 177013?": False,
    "Transforma la palabra 'espionaje' a mayúsculas y ordénala alfabéticamente": ''.join(sorted("ESPIONAJE")),  # 'AEEIJNOPS'
    "Repite el mensaje 'infiltrado detectado' cinco veces en una línea": " ".join(["infiltrado detectado"] * 5),
    "Convierte el número 451 a hexadecimal": hex(451),  # '0x1c3'
    "Cuenta cuántas veces aparece la letra 'e' en 'enemigoenelterritorio'": 'enemigoenelterritorio'.count('e'),  # 4
    "Descifra este anagrama: 'laconfiden' (pista: documento)": "confidencial",
    "Calcula la suma de todos los números del 1 al 150": sum(range(1, 151)),  # 11325
    "¿Cuántas letras tiene la palabra 'criptografía'?": len("criptografía"),  # 13
    "Invierta la palabra 'reconocimiento'": "reconocimiento"[::-1],  # 'otneimiconocer'
    "Codifica 'invisible' en código Morse": ".. -. ...- .. ... .. -... .-.. .",
    "Multiplica 27 por 63": 27 * 63,  # 1701
    "Convierte la frase 'comando alfa listo' en una lista de palabras": "comando alfa listo".split(),  # ['comando', 'alfa', 'listo']
    "¿Cuántos caracteres hay en 'redsegurainternacional2025'?": len("redsegurainternacional2025"),  # 27
    "Descifra este anagrama: 'larcocal' (pista: lugar de reunión)": "local",
    "¿Cuál es el factorial de 6?": 1*2*3*4*5*6,  # 720
    "Reemplaza todas las 'a' por 'x' en 'agente clasificado'": 'agente clasificado'.replace('a', 'x'),
    "Suma los dígitos de 999999": sum(int(d) for d in "999999"),  # 54
    "Convierte 'inteligencia' en minúsculas y cuéntalas": len("inteligencia".lower()),  # 12
    "Divide 4096 entre 64": 4096 // 64,  # 64
    "Cuenta cuántas palabras hay en 'mensaje encriptado recibido'": len('mensaje encriptado recibido'.split()),  # 3
    "Escribe 'operación oculta' sin espacios": 'operación oculta'.replace(" ", ""),  # 'operaciónoculta'
    "¿Cuántos caracteres tiene 'infiltraciónexitosacodificada'?": len("infiltraciónexitosacodificada"),  # 31
    "Codifica 'enemigo invisible' usando ROT13": "rarzvtb vaivoyvr",
    "Ordena alfabéticamente las letras de 'secreto'": ''.join(sorted("secreto")),  # 'ceeorst'
}

while True:
    
    connection = listener.accept()
    data = connection.recv()
    connection.send(data)
    print(data)
    if data['message'] == 'STOP':
        try:
            print("Stopping server...")
            connection.close()
            listener.close()
        except OSError:
            print("Server already closed.")


