from socket import *
import threading
import sys
import pickle
from os import system
import random

class C:    
    
    def __init__(self, nome, serverHost = 'localhost', serverPort=50007,):
        
        #Iniciando a conexão
        self.sockobj = socket(AF_INET, SOCK_STREAM)
        self.sockobj.connect((str(serverHost), int(serverPort)))

        # se passar nome vazio, pegará um nome aleatório
        if nome == '':
            arq = open('arquivos/nomes.txt', 'r')
            arq = arq.readlines()
            n = random.randint(1, 29)
            self.nome = arq[n].strip()
        else:
            self.nome = nome

        # Enviando o nome ao servidor
        self.sockobj.send(pickle.dumps(self.nome))

        msg_recebida = threading.Thread(target=self.msg_recebida)

        msg_recebida.daemon = True
        msg_recebida.start()


        system("cls")
        print(f"\n\n\tVocê está conectado ao servidor como {self.nome.upper()}\n\n")
        while True:
            msg = input()
            if msg.lower() == 'sair' or msg.lower() =='exit':
                self.sockobj.close()
                sys.exit()
            else:
                msgenvia = self.nome,':',msg
                self.envia_msg(msgenvia)


    def msg_recebida(self):
        while True:
            try:
                data = self.sockobj.recv(1024)
                if data:
                    X = pickle.loads(data)
                    y=len(X)
                    print("\t\t\t",end=(''))
                    for i in range(y):
                        print(X[i],end=(''))
                    #print(f'> {pickle.loads(data)}')
                print()
            except:
                pass

    def envia_msg(self, msg):
        self.sockobj.send(pickle.dumps(msg))
        

print(''' ===============================================================
|                                                               |
|    Seja Bem-vindo ao maior grupo de Bate-Papo do mundo!!      |
|                                                               |
 ===============================================================''')

nome = input('Nickname: ')
c = C(nome)
