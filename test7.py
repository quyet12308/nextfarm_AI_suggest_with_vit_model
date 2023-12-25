import json

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
    except json.JSONDecodeError as e:
        print(f'Error decoding JSON: {e}')

# Đường dẫn đến tệp văn bản chứa các đối tượng JSON
text_file_path = 'data_1.txt'

# Đọc từng dòng trong tệp văn bản và xử lý JSON
with open(text_file_path, 'r') as file:
    for line in file:
        process_json_line(line)