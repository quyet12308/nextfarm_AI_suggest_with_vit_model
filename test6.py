import json
from write_to_file import ghi_noi_dung_vao_file

def load_json_properties(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    properties = {}
    for key, value in data.items():
        properties[key] = value
    print(type(properties))
    return properties

# Sử dụng hàm để tải tên thuộc tính và giá trị từ tệp JSON
json_file_path = 'test4.json'
properties = load_json_properties(json_file_path)
properties_data = properties['data']

# In tên thuộc tính và giá trị
for key, value in properties.items():
    print(f'{key}')
    # print(f"{type(properties['data'])}")
    # pass
print(f"{properties['data'][0]}")
id = properties['data'][0]['id']
print(f"{id}")
pic_url = properties['data'][0]['pic_url']
print(f"{pic_url}")
tag_name_level1 = properties['data'][0]['tag_name_level1']
print(f"{tag_name_level1}")
tag_name_level2 = properties['data'][0]['tag_name_level2']
print(f"{tag_name_level1}")
tag_name_level3 = properties['data'][0]['tag_name_level3']
print(f"{tag_name_level1}")

data_1 = {
    "id": id,
    "pic_url": pic_url,
    "tag_name_level1": tag_name_level1,
    "tag_name_level2": tag_name_level2,
    "tag_name_level3": tag_name_level3,
}
data_1_json = json.dumps(obj=data_1)
print(type(data_1_json))
# ghi_noi_dung_vao_file(file_name="data_1.txt",text=data_1_json)

for data in range(len(properties_data)):
    print(data)
    id = properties_data[data]["id"]
    pic_url = properties_data[data]["pic_url"]
    tag_name_level1 = properties_data[data]["tag_name_level1"]
    tag_name_level2 = properties_data[data]["tag_name_level2"]
    tag_name_level3 = properties_data[data]["tag_name_level3"]
    data_1 = {
        "id": id,
        "pic_url": pic_url,
        "tag_name_level1": tag_name_level1,
        "tag_name_level2": tag_name_level2,
        "tag_name_level3": tag_name_level3,
    }
    data_1_json = json.dumps(obj=data_1)
    print(type(data_1_json))
    ghi_noi_dung_vao_file(file_name="data_1.txt",text=data_1_json)





