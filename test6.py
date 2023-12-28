# import json
# from write_to_file import ghi_noi_dung_vao_file

# def load_json_properties(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         data = json.load(file)

#     properties = {}
#     for key, value in data.items():
#         properties[key] = value
#     print(type(properties))
#     return properties

# # Sử dụng hàm để tải tên thuộc tính và giá trị từ tệp JSON
# json_file_path = 'test4.json'
# properties = load_json_properties(json_file_path)
# properties_data = properties['data']

# # In tên thuộc tính và giá trị
# for key, value in properties.items():
#     print(f'{key}')
#     # print(f"{type(properties['data'])}")
#     # pass
# print(f"{properties['data'][0]}")
# id = properties['data'][0]['id']
# print(f"{id}")
# pic_url = properties['data'][0]['pic_url']
# print(f"{pic_url}")
# tag_name_level1 = properties['data'][0]['tag_name_level1']
# print(f"{tag_name_level1}")
# tag_name_level2 = properties['data'][0]['tag_name_level2']
# print(f"{tag_name_level1}")
# tag_name_level3 = properties['data'][0]['tag_name_level3']
# print(f"{tag_name_level1}")

# data_1 = {
#     "id": id,
#     "pic_url": pic_url,
#     "tag_name_level1": tag_name_level1,
#     "tag_name_level2": tag_name_level2,
#     "tag_name_level3": tag_name_level3,
# }
# data_1_json = json.dumps(obj=data_1)
# print(type(data_1_json))
# # ghi_noi_dung_vao_file(file_name="data_1.txt",text=data_1_json)

# for data in range(len(properties_data)):
#     print(data)
#     id = properties_data[data]["id"]
#     pic_url = properties_data[data]["pic_url"]
#     tag_name_level1 = properties_data[data]["tag_name_level1"]
#     tag_name_level2 = properties_data[data]["tag_name_level2"]
#     tag_name_level3 = properties_data[data]["tag_name_level3"]
#     data_1 = {
#         "id": id,
#         "pic_url": pic_url,
#         "tag_name_level1": tag_name_level1,
#         "tag_name_level2": tag_name_level2,
#         "tag_name_level3": tag_name_level3,
#     }
#     data_1_json = json.dumps(obj=data_1)
#     print(type(data_1_json))
#     ghi_noi_dung_vao_file(file_name="data_1.txt",text=data_1_json)


numbers = [-1.6770434379577637, -1.3769924640655518, -0.0192255862057209, 1.9261091947555542, 0.2869201898574829]

# Lấy ra 2 số lớn nhất
# top_two_numbers = sorted(numbers)[-2:]

# # Lấy ra vị trí của 2 số lớn nhất
# indices = [i for i, num in enumerate(numbers) if num in top_two_numbers]

# # In ra 2 số lớn nhất và vị trí của chúng
# print("2 số lớn nhất:", top_two_numbers)
# print("Vị trí của 2 số lớn nhất:", indices)

def get_the_values_and_positions(logits_list,nums):
    # Lấy ra 2 số lớn nhất
    top_numbers = sorted(logits_list,reverse=True)[-nums:]

    # Lấy ra vị trí của 2 số lớn nhất
    indices = [i for i, num in enumerate(logits_list) if num in top_numbers]

    # In ra 2 số lớn nhất và vị trí của chúng
    print("2 số lớn nhất:", top_numbers)
    print("Vị trí của 2 số lớn nhất:", indices)
    return top_numbers,indices

def get_the_values_and_positions2(logits_list, nums):
    # Lấy ra 2 số lớn nhất
    top_numbers = sorted(logits_list, reverse=True)[:nums]

    # Lấy ra vị trí của 2 số lớn nhất
    indices = [i for i, num in sorted(enumerate(logits_list), key=lambda x: x[1], reverse=True)[:nums]]

    # In ra 2 số lớn nhất và vị trí của chúng
    print("2 số lớn nhất:", top_numbers)
    print(f"Vị trí của {nums} số lớn nhất:", indices)
    return top_numbers, indices

def get_the_values_and_positions3(logits_list, nums):
    # Lấy ra 2 số lớn nhất
    top_numbers = sorted(logits_list, reverse=True)[:nums]

    # Lấy ra vị trí của 2 số lớn nhất
    indices = [i for i, num in sorted(enumerate(logits_list), key=lambda x: x[1], reverse=True)[:nums]]

    # Kiểm tra nếu cả vị trí 2 và 3 xuất hiện trong danh sách vị trí
    if 2 in indices and 3 in indices:
        # Chỉ lấy một số (số có giá trị lớn hơn)
        max_index = indices.index(max(indices))
        print(max_index)
        indices = [indices[max_index]]

    # In ra 2 số lớn nhất và vị trí của chúng
    print("2 số lớn nhất:", top_numbers)
    print("Vị trí của 2 số lớn nhất:", indices)
    return top_numbers, indices

def get_the_values_and_positions6(logits_list, nums):
    # Lấy ra 2 số lớn nhất
    top_numbers = sorted(logits_list, reverse=True)[:nums]
    print(top_numbers)
    # Tạo cặp giá trị-vị trí tương ứng
    value_indices = [(num, i) for i, num in enumerate(logits_list)]
    print(value_indices)
    # Kiểm tra giá trị của phần tử ở vị trí 2 và 3 ( do cmd và cgm là trùng nhau đều là bệnh khảm)
    if value_indices[2][0] < value_indices[3][0]:
        del value_indices[2]
    else:
        del value_indices[3]
    print(value_indices)


    # Sắp xếp cặp giá trị-vị trí theo giá trị giảm dần
    sorted_value_indices = sorted(value_indices, key=lambda x: x[0], reverse=True)
    print(sorted_value_indices)
    # Lấy ra danh sách các vị trí đã sắp xếp
    indices = [vi[1] for vi in sorted_value_indices[:nums]]

    # In ra 2 số lớn nhất và vị trí của chúng
    print("2 số lớn nhất:", top_numbers)
    print(f"Vị trí của {nums} số lớn nhất:", indices)
    return top_numbers, indices

# numbers = [-1.6770434379577637, -1.3769924640655518, -0.0192255862057209, 1.9261091947555542, 0.2869201898574829]
# get_the_values_and_positions6(logits_list=numbers, nums=3)

