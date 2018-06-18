from socket import *
import threading
import sys
import pickle

class S():
    def __init__(self, serverHost= '192.168.0.15', serverPort =50007):

        self.clientes = []

        self.sockobj = socket(AF_INET, SOCK_STREAM)
        self.sockobj.bind((str(serverHost), int(serverPort)))
        self.sockobj.listen(5)
        self.sockobj.setblocking(False)

        aceitar = threading.Thread(target = self.aceitarCon)
        procesar = threading.Thread(target = self.procesarCon)

        aceitar.daemon = True
        aceitar.start()

        procesar.daemon = True
        procesar.start()

        while True:
            msg = input()
            if msg.lower() == 'sair' or msg.lower() == 'exit':
                self.sockobj.close()
                sys.exit()
            else:
                pass

    def msg_todos(self, msg, cliente):
        for c in self.clientes:
            try:
                if c != cliente:
                    c.send(msg)
                    #name.send(nome)
            except:
                self.clientes.remove(c)

    def aceitarCon(self):
        while True:
            try:
                conexao, endereco = self.sockobj.accept()
                #print('Um cliente foi conectado por',endereco)
                conexao.setblocking(False)
                self.clientes.append(conexao)
                
            except:
                pass
            

    def procesarCon(self):
        while True:
            if len(self.clientes) > 0:
                for c in self.clientes:
                    try:
                        data = c.recv(1024)
                        #name = nome.recv(1024)
                        if data:
                            self.msg_todos(data,c)
                    except:
                        pass


s = S()
