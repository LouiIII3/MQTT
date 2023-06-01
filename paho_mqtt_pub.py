import paho.mqtt.client as mqtt

mqtt = mqtt.Client("mypub")
mqtt.connect("localhost", 1883)

mqtt.publish("mqtt/my_rpi_msg/1", 
"This is the first rpi mosquitto msg.")
mqtt.publish("mqtt/my_rpi_msg/2/multilevel2", 
"This is the second rpi mosquitto msg.")
mqtt.publish("mqtt/my_rpi_msg/3", 
"This is the third rpi mosquitto msg.")

print("The message is published.")
mqtt.loop(2)

