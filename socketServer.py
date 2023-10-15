from socket import *


def main():
    # Creación del socket
    sock = socket(AF_INET, SOCK_STREAM)
    # Asociación del socket a un puerto
    host = "localhost"
    port = 7750
    sock.bind((host, port))

    # Escucha de conexiones entrantes
    sock.listen(1)

    # Mensaje de bienvenida
    print("Servidor escuchando en el puerto 7750...")

    try:
        # Aceptación de una conexión entrante
        conn, address = sock.accept()

        # Bucle de recepción de mensajes
        while True:
            # Recepción del mensaje del cliente
            message = conn.recv(1024)
            if not message:
                break

            print("Mensaje del cliente:", message.decode('utf-8'))

            # Envío de la respuesta al cliente
            if message != "exit":
                conn.sendall(message)
            else:
                break

    except ConnectionError as e:
        print("Error de conexión:", e)
    finally:
        # Cierre de las conexiones
        conn.close()
        sock.close()


if __name__ == "__main__":
    main()