from paho.mqtt import client
import time

#criando uma função de callback para quando
#conectarmos ao broker
def conectar(client, userdata, flags, rc):
    print("Conectado ao broker!")

#criamos o cliente MQTT
cliente_pub = client.Client("cliente_pub")

cliente_pub.on_connect = conectar
cliente_pub.connect("localhost", 1883)

i = 10

while True:
    cliente_pub.publish("temperatura", i)
    cliente_pub.publish("umidade", i*2 + 1)
    cliente_pub.publish("Luminosidade", i*30)
    cliente_pub.loop_start()
    i += 1
    time.sleep(2)
