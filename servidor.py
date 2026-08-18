import socket


HOST = "127.0.0.1"
PORTA = 5000


servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


servidor.bind((HOST, PORTA))


servidor.listen(1)


print("Servidor iniciado...")
print("Aguardando cliente...")


conexao, endereco = servidor.accept()


print("Cliente conectado!")


while True:

    mensagem = conexao.recv(1024).decode()

    if mensagem == "sair":
        print("Cliente encerrou a conexão.")
        break

    print("Cliente:", mensagem)

    resposta = input("Servidor: ")

    conexao.send(resposta.encode())


conexao.close()
servidor.close()