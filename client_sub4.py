from paho.mqtt import client

#criando uma função de callback para quando
#conectarmos ao broker
def conectar(client, userdata, flags, rc):
    print("Conectado ao broker!")

#criando uma função de callback para quando recebermos 
#mensagens do broker
def recebimento_msg(client, userdata, msg):
    mensagem = msg.payload.decode()
    print("Mensagem recebida: ", mensagem)

    if mensagem == '20':
        #cancelando a assinatura do tópico temperatura
        client.unsubscribe("temperatura")

#essa função é de callback para um tópico específico
def recebimento_umidade(client, userdata, msg):
    mensagem = msg.payload.decode()
    topico = msg.topic
    print("Mensagem recebida: ", mensagem, "Tópico:", topico)

#essa função é de callback para um tópico específico
def recebimento_luminosidade(client, userdata, msg):
    mensagem = msg.payload.decode()
    topico = msg.topic
    print("Mensagem recebida: ", mensagem, "Tópico:", topico)

#criamos o cliente MQTT
cliente_sub = client.Client("cliente_sub4")

cliente_sub.on_connect = conectar

cliente_sub.message_callback_add("umidade", recebimento_umidade)
cliente_sub.message_callback_add("temperatura", recebimento_msg)
cliente_sub.message_callback_add("Luminosidade", recebimento_luminosidade)

cliente_sub.connect("localhost", 1883)
cliente_sub.subscribe("temperatura")
cliente_sub.subscribe("umidade")
cliente_sub.subscribe("Luminosidade")

cliente_sub.loop_forever()