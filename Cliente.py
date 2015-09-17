#-*-encoding: latin1 -*-
import socket
import thread

def run():
   try:

      while True:
          msg = clienteTcp.recv(1024)
          if msg == ' ':
            print "Conexão encerrada..."
            clienteTcp.close()
          print msg
          print "Responder > "
   except:
      print "Ocorreu uma falha no servidor... "

if __name__ == "__main__":
    HOST = '127.0.0.1'     # Endereco IP do Servidor
    PORT = 9000            # Porta que o Servidor esta
    clienteTcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (HOST, PORT)
    clienteTcp.connect(dest)

    try:
        teclado = raw_input("Digite seu nome: ")
        if len(teclado) <= 64:
            teclado = teclado.upper()
            clienteTcp.sendall(teclado)
        else:
            print'erro no tamanho da mensagem'

        thread.start_new_thread(run,())
        while True:
            msg = raw_input('Mensagem > ')
            if len(msg) <= 64:
                clienteTcp.sendall(msg)
            else:
                print'erro no tamanho da mensagem'

    except:
        print "Falha na conexão... "
        clienteTcp.close()
        thread.exit()
