import socket
import threading
import time

def procClientData(client):
    opt = (client.recv(2048)).decode()
    ans = ""
    if(opt == "1"):
        ans = time.strftime("%d/%m/%y")
    elif(opt == "2"):
        ans = time.strftime("%H:%M")
    elif(opt == "3"):
        ans = time.strftime("%d/%m/%y %H:%M")
    client.send(ans.encode())
    client.close()

def server(host="localhost", port=3000):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((host, port))
        sock.listen(5)
        while True:
            print("Waiting...")
            client, address = sock.accept()
            t = threading.Thread(target=procClientData, args=(client,))
            t.start()
            time.sleep(5)
            t.join()

if __name__ == "__main__":
    server()
