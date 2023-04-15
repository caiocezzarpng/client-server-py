import socket
import time
import random

def main():
    host = 'localhost' # substituir pelo IP do servidor, se necessário
    port = 3000

    while True:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_server:
            socket_server.connect((host, port))
            num_str = str(random.randint(1, 10**30)) 
            socket_server.sendall(num_str.encode())
            data = socket_server.recv(1024)
        
        print(f'numero enviado para o servidor: {num_str}')
        print(f'Resultado recebido do servidor: {data.decode()}')
        time.sleep(10) # pausa a execução por 10 segundos antes de enviar a próxima requisição

if __name__ == '__main__':
    main()
