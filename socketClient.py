from socket import *


def main():
    # Creación del socket
    sock = socket(AF_INET, SOCK_STREAM)

    # Asociación del socket al servidor
    host = "localhost"
    port = 7750

    try:
        sock.connect((host, port))

        # Bucle de recepción de mensajes
        while True:
            # Envío de un mensaje al servidor
            message = input("Escribe un mensaje: ")
            sock.sendall(message.encode('utf-8'))

            # Recepción de la respuesta del servidor
            response = sock.recv(1024)
            print("Respuesta del servidor:", response.decode('utf-8'))

            if message == "exit":
                break

    except ConnectionError as e:
        print("Error de conexión:", e)
    finally:
        # Cierre del socket
        sock.close()


if __name__ == "__main__":
    main()