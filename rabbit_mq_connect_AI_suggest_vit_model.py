from security_info import rabbit_mq_infor,urls,tokens
# from tensorflow_model_pest_diagnosis import pest_diagnosis_with_tensorflow_and_mobilenet
from vit_model_cassava import pest_diagnosis_with_pytorch_and_vit_model,pest_diagnosis_with_pytorch_and_vit_model_and_acc_value_each_class,two_pests_diagnosis_with_pytorch_and_vit_model_and_acc_value_each_class
from yolo_model_for_count_object import count_la_khoai_mi_with_url
import pika
import json
from write_error_log import write_to_file,write_to_file2,write_to_file3
from setting import threshold
from write_error_log import gettime2
import requests
from rename_lable_level_2_avn import labling_dataset_lavel2



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

def listen_rabbitmq(queue_name):
    # Kết nối tới RabbitMQ
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

    # Định nghĩa và khai báo hàng đợi
    channel.queue_declare(queue=queue_name,durable=False)

    # Hàm callback được gọi khi nhận được tin nhắn
    def callback(ch, method, properties, body):
        # print(gettime2())
        time_txt = gettime2()
        request_data = body.decode()
        print("Received message:", request_data)
        print(type(request_data))
        request_data = json.loads(request_data)
        print(request_data)
        print(type(request_data))
        id = request_data["id"]
        url_image = request_data["pic_url"]

        disease_probabilities = two_pests_diagnosis_with_pytorch_and_vit_model_and_acc_value_each_class(
            threshold=threshold,
            url_img=url_image
        )

        print(disease_probabilities)
        response_by_put_data_to_avn = labling_dataset_lavel2(
            id=id,
            tag_name_level2=disease_probabilities[0]["ten_benh"],
            tag_name_level2_predict_1=disease_probabilities[0]["ten_benh"],
            tag_name_level2_predict_percent_1=disease_probabilities[0]["percent"],
            tag_name_level2_predict_2=disease_probabilities[1]["ten_benh"],
            tag_name_level2_predict_percent_2=disease_probabilities[1]["percent"],
        )
        # Kiểm tra mã trạng thái HTTP
        status_code = response_by_put_data_to_avn.status_code
        print("Status code:", status_code)

        # Kiểm tra nội dung phản hồi
        response_data = response_by_put_data_to_avn.json()
        print("Response data:", response_data)
        # print(type(response_data))
        write_to_file3(
            filename="text_folder/note_response_put_data_to_avn_web.txt",
            id=id,
            response=str(response_data),
            status=status_code
        )

        

        


    # Bắt đầu lắng nghe trên hàng đợi
    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

    print("Listening for messages. To exit, press CTRL+C")

    # Bắt đầu tiêu thụ tin nhắn
    channel.start_consuming()

flag = True
while flag:
    try:
        listen_rabbitmq(queue_name=rabbit_mq_infor['quese_post_data_test'])
    except Exception as e:
        # Xử lý ngoại lệ (lỗi)
        # print(f"Lỗi xử lý URL : {str(e)}")
        write_to_file(
            error=f"{str(e)}",
            filename="text_folder/error_to_connect_rabbitmq.txt"
        )
        # Bỏ qua URL lỗi và tiếp tục vòng lặp
        continue