
# Comunicação Cliente-Servidor TCP

Projeto acadêmico desenvolvido em Python para demonstrar uma comunicação entre cliente e servidor utilizando sockets e o protocolo TCP.

## Sobre o projeto

O objetivo deste projeto é colocar em prática conceitos básicos de Redes de Computadores e programação de redes, estabelecendo uma comunicação entre duas aplicações.

# O projeto possui:

cliente.py — responsável por se conectar ao servidor e enviar mensagens.
servidor.py — responsável por aceitar a conexão e responder às mensagens.

## Tecnologias utilizadas

Python
Socket
TCP
IPv4

## Estrutura do projeto

comunicacao-cliente-servidor-tcp/
│
├── cliente.py
├── servidor.py
└── README.md

## Como executar
### Iniciar o servidor

Abra um terminal na pasta do projeto e execute:

python servidor.py

O servidor ficará aguardando uma conexão.

### Iniciar o cliente

Abra outro terminal na mesma pasta e execute:

python cliente.py

O cliente realizará a conexão com o servidor.

## Comunicação

Após a conexão, será possível enviar mensagens entre o cliente e o servidor.

Para encerrar a comunicação, digite:

sair

## Objetivo acadêmico

Este projeto foi desenvolvido como atividade acadêmica para demonstrar uma comunicação utilizando o protocolo TCP, colocando em prática conceitos de conexão cliente-servidor, sockets, envio e recebimento de dados.

## Autor

Erick Wesley Ribeiro Vieira

Estudante de Sistemas de Informação.