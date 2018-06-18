from socket import *
import threading
import sys
import pickle
from os import system

class C():    
    
    def __init__(self , serverHost = '192.168.0.15', serverPort=50007, nome=input('Nome: ')):
        

        self.sockobj = socket(AF_INET, SOCK_STREAM)
        self.sockobj.connect((str(serverHost), int(serverPort)))

        self.sockobj.send(pickle.dumps(nome))

        msg_recebida = threading.Thread(target=self.msg_recebida)

        msg_recebida.daemon = True
        msg_recebida.start()


        system("cls")
        while True:
            msg = input()
            if msg.lower() == 'sair' or msg.lower() =='exit':
                self.sockobj.close()
                sys.exit()
            else:
                msg = nome,': ',msg
                self.envia_msg(msg)


    def msg_recebida(self):
        while True:
            try:
                data = self.sockobj.recv(1024)
                if data:
                    X = pickle.loads(data)
                    y=len(X)
                    for i in range(y):
                        print(X[i],end=(''))
                    #print(f'> {pickle.loads(data)}')
                print()
            except:
                pass

    def envia_msg(self, msg):
        self.sockobj.send(pickle.dumps(msg))
        

c = C()
