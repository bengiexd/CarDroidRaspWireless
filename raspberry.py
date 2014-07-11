__author__ = 'knick'

from RPi import GPIO
from threading import Thread
import time

class Motor1(Thread):
    """
        # motor 1, derecha - izquierda
    """
    __act_orden = 0.4
    __delay_orden = 0.1
    # __estado : (0:recto,  1:derecha, 2:izquierda)
    __estado = 0

    __motor_1_a = 3
    __motor_1_b = 5

    def __init__(self):
        Thread.__init__(self)
        GPIO.setup(self.__motor_1_a, GPIO.OUT)
        GPIO.setup(self.__motor_1_b, GPIO.OUT)

    def accionar(self, n):
        self.__estado = n

    def __recto(self):
        GPIO.output(self.__motor_1_a, False)
        GPIO.output(self.__motor_1_b, False)

    def __derecha(self):
        GPIO.output(self.__motor_1_a, True)
        GPIO.output(self.__motor_1_b, False)

    def __izquierda(self):
        GPIO.output(self.__motor_1_a, False)
        GPIO.output(self.__motor_1_b, True)

    def run(self):
        while True:
            # actualizar motor 1
            if self.__estado == 1:
                self.__derecha()
            elif self.__estado == 2:
                self.__izquierda()
            time.sleep(self.__delay_orden)
            # desactivar orden
            self.__recto()
            # delay de actualizacion
            time.sleep(self.__act_orden)

class Motor2(Thread):
    """
        # motor 2, adelante - atras
    """
    __act_orden = 0.2
    __delay_orden = 0.4
    # __estado : (0:parado, 1:adelante, 2:atras)
    __estado = 0

    __motor_2_a = 8
    __motor_2_b = 10

    def __init__(self):
        Thread.__init__(self)
        GPIO.setup(self.__motor_2_a, GPIO.OUT)
        GPIO.setup(self.__motor_2_b, GPIO.OUT)

    def accionar(self, n):
        self.__estado = n

    def __parado(self):
        GPIO.output(self.__motor_2_a, False)
        GPIO.output(self.__motor_2_b, False)

    def __adelante(self):
        GPIO.output(self.__motor_2_a, True)
        GPIO.output(self.__motor_2_b, False)

    def __atras(self):
        GPIO.output(self.__motor_2_a, False)
        GPIO.output(self.__motor_2_b, True)

    def run(self):
        while True:
            # actualizar motor 2
            if self.__estado == 1:
                self.__adelante()
            elif self.__estado == 2:
                self.__atras()
            # duracion de orden
            time.sleep(self.__delay_orden)
            # desactivar orden
            self.__parado()
            # delay de actualizacion
            time.sleep(self.__act_orden)

class Raspberry():

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)

        self.motor_1 = Motor1()
        self.motor_1.start()
        self.motor_2 = Motor2()
        self.motor_2.start()

    def ejecutar(self, n):
        # interpretar y almacenar valor
        self.__interpretar_orden(n)

    def __interpretar_orden(self, n):
        if n == '0':
            # derecha
            self.motor_1.accionar(1)
        elif n == '1':
            # izquierda
            self.motor_1.accionar(2)
        elif n == '2':
            # adelante
            self.motor_2.accionar(1)
        elif n == '3':
            # atras
            self.motor_2.accionar(2)
        elif n == '4':
            # recto
            self.motor_1.accionar(0)
        elif n == '5':
            # parado
            self.motor_2.accionar(0)
        elif n == '6':
            # alto
            self.motor_1.accionar(0)
            self.motor_2.accionar(0)





