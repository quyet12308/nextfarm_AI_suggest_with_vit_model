import pika
from security_info import rabbit_mq_infor,urls
import json
import time
from read_data_from_text_file import read_data_from_file

def send_message(message,quese_name):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=urls["url_rabbitmq"],
            port=rabbit_mq_infor["port"],
            virtual_host=rabbit_mq_infor["virtual_host"],
            credentials=pika.PlainCredentials(
                username=rabbit_mq_infor["user_name"],
                password=rabbit_mq_infor["password"]
            )
        )
    )
    channel = connection.channel()
    channel.queue_declare(queue=quese_name,durable=False)
    
    channel.basic_publish(
        exchange='',
        routing_key=quese_name,
        # routing_key='nextfarm_ai_message',
        body=message
    )
    connection.close()
    return {"mesage":'Message sent successfully'}

# my_dict = {
#     "id": "testid",
#     "url": "https://img.nextcrm.vn/nextcrm/hosco/1703238625304/1703238625301.png",
#     "tree_name": "cay_khoai_mi"
#     }

# data1 = read_data_from_file(file_path="data_2.txt")
# # send_message(message=data1[0],quese_name=rabbit_mq_infor["quese_post_data"])
# for i in range(len(data1)):
#     # send_message(message=data1[i],quese_name=rabbit_mq_infor["quese_post_data"])
#     send_message(message=data1[i],quese_name="nextfarm_ai_ajinomoto_suggest_update_level_lable_nextx_using_yolo_and_vit_model_test")

# Mã hóa từ điển thành chuỗi JSON

