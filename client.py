import socket

def client(host="localhost", port=3000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        menu="""Qual informação deseja saber?
1) Desejo saber a data.
2) Desejo saber a hora.
3) Desejo saber a data e a hora."""
        op = ""
        print(menu)
        while(op not in ["1", "2", "3"]):
            op = input("Insira sua opção: ")
            if op not in ["1", "2", "3"]:
                print("Opção inválida, por favor tente novamente!")
        sock.send(op.encode('utf-8'))
        print(sock.recv(2048).decode())



if __name__ == "__main__":
    client()
