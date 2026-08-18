import socket


HOST = "127.0.0.1"
PORTA = 5000


cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


cliente.connect((HOST, PORTA))


print("Conectado ao servidor!")
print("Digite 'sair' para encerrar.")


while True:

    mensagem = input("Você: ")

    cliente.send(mensagem.encode())

    if mensagem == "sair":
        break

    resposta = cliente.recv(1024).decode()

    print("Servidor:", resposta)


cliente.close()