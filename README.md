1. paho_mqtt_sub.py 설명
    - import paho.mqtt.client as mqtt : •mqtt 관련 모듈 import
    - def on_connect : mqtt 서버에 연결됐을때 실행되는 콜백함수
    - def on_message: 메시지를 수신했을때 실행되는 콜백함수
    - client.connect("localhost", 1883, 60) : 포트번호와 keepalive 설정
 
2. paho_mqtt_pub.py 설명
    - mqtt.Client() 함수: MQTT 클라이언트 객체 생성
    - mqtt.publish() 메서드 : 메시지 발행
