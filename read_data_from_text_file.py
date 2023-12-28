import json
from write_to_file import ghi_noi_dung_vao_file
from write_error_log import *

def process_json_line(line):
    try:
        data = json.loads(line)
        # Sử dụng dữ liệu JSON tại đây
        id = data['id']
        pic_url = data['pic_url']
        tag_name_level1 = data['tag_name_level1']
        tag_name_level2 = data['tag_name_level2']
        tag_name_level3 = data['tag_name_level3']

        # In các giá trị
        print(f'id: {id}')
        print(f'pic_url: {pic_url}')
        print(f'tag_name_level1: {tag_name_level1}')
        print(f'tag_name_level2: {tag_name_level2}')
        print(f'tag_name_level3: {tag_name_level3}')
        data = {
            "id":id,
            "pic_url":pic_url
        }
        return data
    except json.JSONDecodeError as e:
        print(f'Error decoding JSON: {e}')
        write_to_file(error=e,filename="text_folder/error_by_read_data_from_text_file.txt")


# Đường dẫn đến tệp văn bản chứa các đối tượng JSON
# text_file_path = 'data_1.txt'

# # Đọc từng dòng trong tệp văn bản và xử lý JSON
# with open(text_file_path, 'r') as file:
#     for line in file:
#         process_json_line(line)
        

def read_data_from_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  # Loại bỏ các ký tự trống (whitespace) thừa
            data.append(line)
    return data