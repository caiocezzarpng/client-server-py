import socket
import threading

def handle_client(conn, address):
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            num_str = data.decode()
            if len(num_str) >= 10:
                result_str = '*' * len(num_str)
                conn.sendall(result_str.encode())
            else:
                num_str = float(num_str)
                if num_str % 2 == 1:
                    result_str = "IMPAR"
                    conn.sendall(result_str.encode())
                if num_str % 2 == 0:
                    result_str = "PAR"
                    conn.sendall(result_str.encode())

            print(f'Dados recebidos do cliente {address}: {num_str}')

def main():
    host = 'localhost' 
    port = 3000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_client:
        socket_client.bind((host, port))
        socket_client.listen()
        print(f'Servidor pronto para receber conexões na porta {port}...')

        while True:
            conn, address = socket_client.accept()
            print(f'Conexão recebida de {address}')

            client_thread = threading.Thread(target=handle_client, args=(conn, address))
            client_thread.start()

if __name__ == '__main__':
    main()
