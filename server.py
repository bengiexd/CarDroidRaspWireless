#!/usr/bin/python

import socket
import serial
import socket
import sys
import time
from threading import Thread
from raspberry import Raspberry


class Cliente(Thread):
    """ hilo para subir un video al raspberry """

    def __init__(self, socket_cliente, raspberry):
        """ constructor """
        Thread.__init__(self)
        self.socket_cliente = socket_cliente
        self.raspberry = raspberry


    def run(self):
        dato = self.socket_cliente.recv(1)
        print type(dato)
        print 'dato recv: ', dato
        self.raspberry.ejecutar(dato)
        # Cerramos socket.
        self.socket_cliente.close()



class ServerThread():
    #ip = "192.168.10.105"
    port = 9999

    def __init__(self, ip=None, port=None):

        if ip:
            self.ip = ip
        if port:
            self.port = port

        self.raspberry = Raspberry()

        self.activo = True
        # Creamos el socket.
        server = socket.socket()
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # Conecta el socket con la direccion.
        server.bind((self.ip, self.port))
        # Empieza a escuchar conexiones.
        server.listen(2)
        print "Esperando conexion..."
        while self.activo:
            # Aceptamos una conexion, se bloquea hasta que alguien se conecte.
            socket_cliente, datos_cliente = server.accept()
            print "cliente: ", datos_cliente
            cliente = Cliente(socket_cliente, self.raspberry)
            cliente.start()
        server.close()

if __name__ == "__main__":
    # obtner ip local
    #ip = '192.168.12.1'
    ip = '192.168.12.1'
    ServerThread(ip=ip)
    #except:
    #    print "error al crear servidor de video"






