import torch
import requests
from PIL import Image
from transformers import ViTFeatureExtractor, ViTForImageClassification
from setting import threshold,acc_dicts
# Đường dẫn đến ảnh
url = 'https://iot-image.nextfarm.vn/avn/0902243822/1702373519673.png'

def get_the_values_and_positions6(logits_list, nums):
    # Lấy ra 2 số lớn nhất
    top_numbers = sorted(logits_list, reverse=True)[:nums]
    print(top_numbers)
    # Tạo cặp giá trị-vị trí tương ứng
    value_indices = [(num, i) for i, num in enumerate(logits_list)]
    # print(value_indices)
    # Kiểm tra giá trị của phần tử ở vị trí 2 và 3 ( do cmd và cgm là trùng nhau đều là bệnh khảm)
    if value_indices[2][0] < value_indices[3][0]:
        del value_indices[2]
    else:
        del value_indices[3]
    # print(value_indices)
    # Sắp xếp cặp giá trị-vị trí theo giá trị giảm dần
    sorted_value_indices = sorted(value_indices, key=lambda x: x[0], reverse=True)
    # print(sorted_value_indices)
    # Lấy ra danh sách các vị trí đã sắp xếp
    indices = [vi[1] for vi in sorted_value_indices[:nums]]

    # In ra 2 số lớn nhất và vị trí của chúng
    # top_numbers trả lại giá trị list ban đầu khác với cái cần , nhưng có thể sau này sẽ fix thêm nên cứ giữ nguyên
    # print("2 số lớn nhất:", top_numbers)
    print(f"Vị trí của {nums} số lớn nhất:", indices)
    return top_numbers, indices


def pest_diagnosis_with_pytorch_and_vit_model(url_img,threshold):
    # Tải ảnh và tiền xử lý
    image = Image.open(requests.get(url_img, stream=True).raw)
    feature_extractor = ViTFeatureExtractor.from_pretrained('siddharth963/vit-base-patch16-224-in21k-finetuned-cassava', cache_dir="models/pytorch_model")
    inputs = feature_extractor(images=image, return_tensors="pt")

    # Tạo mô hình và dự đoán
    model = ViTForImageClassification.from_pretrained('siddharth963/vit-base-patch16-224-in21k-finetuned-cassava', cache_dir="models/pytorch_model")
    outputs = model(**inputs)
    logits = outputs.logits
    print(logits)
    print(logits[0])
    predicted_class_index = torch.argmax(logits, dim=1).item()
    print(predicted_class_index)

    predicted_class_confidence = logits[0, predicted_class_index].item()
    print(f"trị số dự đoán : {predicted_class_confidence}")
    # In ra tên class dự đoán
    class_names = [
        "cbb",
        "cbsd",
        "cgm",
        "cmd",
        "healthy"
    ]  # Thay thế bằng danh sách các tên lớp bệnh

    name_pest_list = {
    'cbb': "chay_la",
        'cbsd' : "benh_dom_mat",
        'cgm' :"kham_la_do_virut",
        'cmd' :"kham_la_do_virut",
        'healthy':"khoe_manh"
    }

    name_pest_list_vn = {
        "chay_la" : "bệnh cháy lá",
        "benh_dom_mat" : "bệnh đốm mắt",
        "kham_la_do_virut" : "bệnh khảm lá do virut",
        "khoe_manh" : "cây khỏe mạnh"
    }
    predicted_class_name = class_names[predicted_class_index]


    # print(torch.max(torch.softmax(logits, dim=1)))
    if predicted_class_confidence > threshold:
        print("Predicted class:", predicted_class_name)
        print("ten benh:", name_pest_list[predicted_class_name])
        print(f"tên bệnh vn : {name_pest_list_vn[name_pest_list[predicted_class_name]]}")
        return name_pest_list[predicted_class_name]
    else:
        print("Uncertain prediction")
        print("ten benh:" ,"chua_xac_dinh")
        predicted_class_name = "benh_chua_xac_dinh"
        return predicted_class_name
    
def pest_diagnosis_with_pytorch_and_vit_model_using_local_path_image(local_path,threshold):
    # Tải ảnh và tiền xử lý
    # image = Image.open(requests.get(url_img, stream=True).raw)
    image = Image.open(local_path)
    feature_extractor = ViTFeatureExtractor.from_pretrained('siddharth963/vit-base-patch16-224-in21k-finetuned-cassava', cache_dir="models/pytorch_model")
    inputs = feature_extractor(images=image, return_tensors="pt")

    # Tạo mô hình và dự đoán
    model = ViTForImageClassification.from_pretrained('siddharth963/vit-base-patch16-224-in21k-finetuned-cassava', cache_dir="models/pytorch_model")
    outputs = model(**inputs)
    logits = outputs.logits
    print(logits)
    print(logits[0])
    predicted_class_index = torch.argmax(logits, dim=1).item()
    print(predicted_class_index)

    predicted_class_confidence = logits[0, predicted_class_index].item()
    # print(predicted_class_confidence)
    print(f"trị số dự đoán : {predicted_class_confidence}")
    # In ra tên class dự đoán
    class_names = [
        "cbb",
        "cbsd",
        "cgm",
        "cmd",
        "healthy"
    ]  # Thay thế bằng danh sách các tên lớp bệnh

    name_pest_list = {
    'cbb': "chay_la",
        'cbsd' : "benh_dom_mat",
        'cgm' :"kham_la_do_virut",
        'cmd' :"kham_la_do_virut",
        'healthy':"khoe_manh"
    }

    name_pest_list_vn = {
        "chay_la" : "bệnh cháy lá",
        "benh_dom_mat" : "bệnh đốm mắt",
        "kham_la_do_virut" : "bệnh khảm lá do virut",
        "khoe_manh" : "cây khỏe mạnh"
    }
    predicted_class_name = class_names[predicted_class_index]


    # print(torch.max(torch.softmax(logits, dim=1)))
    if predicted_class_confidence > threshold:
        print("Predicted class:", predicted_class_name)
        print("ten benh:", name_pest_list[predicted_class_name])
        print(f"tên bệnh vn : {name_pest_list_vn[name_pest_list[predicted_class_name]]}")
        return name_pest_list[predicted_class_name] ,predicted_class_confidence,predicted_class_index
    else:
        print("Uncertain prediction")
        print("ten benh:" ,"chua_xac_dinh")
        predicted_class_name = "benh_chua_xac_dinh"
        return predicted_class_name,predicted_class_confidence,predicted_class_index
    
# a = pest_diagnosis_with_pytorch_and_vit_model_using_local_path_image(local_path=r"C:\Users\Lenovo\Downloads\cassava_dataset3_3gb\train\train-healthy-98.jpg",threshold=0.35)
# print(a)
    
# hàm lấy ra 1 bệnh và % của nó dựa trên thống kê test , tổng % các bệnh sẽ không bằng 100%
def pest_diagnosis_with_pytorch_and_vit_model_and_acc_value_each_class(url_img,threshold):
    # Tải ảnh và tiền xử lý
    image = Image.open(requests.get(url_img, stream=True).raw)
    feature_extractor = ViTFeatureExtractor.from_pretrained('siddharth963/vit-base-patch16-224-in21k-finetuned-cassava', cache_dir="models/pytorch_model")
    inputs = feature_extractor(images=image, return_tensors="pt")

    # Tạo mô hình và dự đoán
    model = ViTForImageClassification.from_pretrained('siddharth963/vit-base-patch16-224-in21k-finetuned-cassava', cache_dir="models/pytorch_model")
    outputs = model(**inputs)
    logits = outputs.logits
    print(logits)
    print(logits[0])
    predicted_class_index = torch.argmax(logits, dim=1).item()
    print(predicted_class_index)

    predicted_class_confidence = logits[0, predicted_class_index].item()
    print(f"trị số dự đoán : {predicted_class_confidence}")
    # In ra tên class dự đoán
    class_names = [
        "cbb",
        "cbsd",
        "cgm",
        "cmd",
        "healthy"
    ]  # Thay thế bằng danh sách các tên lớp bệnh

    name_pest_list = {
    'cbb': "chay_la",
        'cbsd' : "benh_dom_mat",
        'cgm' :"kham_la_do_virut",
        'cmd' :"kham_la_do_virut",
        'healthy':"khoe_manh"
    }

    name_pest_list_vn = {
        "chay_la" : "bệnh cháy lá",
        "benh_dom_mat" : "bệnh đốm mắt",
        "kham_la_do_virut" : "bệnh khảm lá do virut",
        "khoe_manh" : "cây khỏe mạnh"
    }
    predicted_class_name = class_names[predicted_class_index]

    
    # print(torch.max(torch.softmax(logits, dim=1)))
    if predicted_class_confidence > threshold:
        percent_predicted_class_confidence = ""
        if predicted_class_confidence >= acc_dicts[f"{predicted_class_index}"]:
            percent_predicted_class_confidence = 0.99
        elif predicted_class_confidence < acc_dicts[f"{predicted_class_index}"]:
            percent_predicted_class_confidence =  predicted_class_confidence / acc_dicts[f"{predicted_class_index}"]

        print("Predicted class:", predicted_class_name)
        print("ten benh:", name_pest_list[predicted_class_name])
        print(f"tên bệnh vn : {name_pest_list_vn[name_pest_list[predicted_class_name]]}")
        print(f"percent = {percent_predicted_class_confidence}")
        return name_pest_list[predicted_class_name],percent_predicted_class_confidence
    else:
        print("Uncertain prediction")
        print("ten benh:" ,"chua_xac_dinh")
        percent_predicted_class_confidence = 0
        predicted_class_name = "benh_chua_xac_dinh"
        print(f"percent = {percent_predicted_class_confidence}")
        return predicted_class_name,percent_predicted_class_confidence
    
# pest_diagnosis_with_pytorch_and_vit_model_and_acc_value_each_class(threshold=threshold,url_img="https://iot-image.nextfarm.vn/avn/0902243822/1703135346934.png")
    
# hầm chi đều xác suất của các bệnh tổng là 100%
def pest_diagnosis_with_pytorch_and_vit_model_and_acc_value_each_class_num_diseases(url_img, threshold, num_diseases):
    # Tải ảnh và tiền xử lý
    image = Image.open(requests.get(url_img, stream=True).raw)
    feature_extractor = ViTFeatureExtractor.from_pretrained('siddharth963/vit-base-patch16-224-in21k-finetuned-cassava', cache_dir="models/pytorch_model")
    inputs = feature_extractor(images=image, return_tensors="pt")

    # Tạo mô hình và dự đoán
    model = ViTForImageClassification.from_pretrained('siddharth963/vit-base-patch16-224-in21k-finetuned-cassava', cache_dir="models/pytorch_model")
    outputs = model(**inputs)
    logits = outputs.logits

    probabilities = torch.softmax(logits, dim=1)
    print(probabilities)
    class_probabilities = probabilities[0].tolist()
    print(class_probabilities)

    # Lấy ra các xác suất và tên lớp bệnh
    class_names = [
        "cbb",
        "cbsd",
        "cgm",
        "cmd",
        "healthy"
    ]

    name_pest_list = {
        'cbb': "chay_la",
        'cbsd' : "benh_dom_mat",
        'cgm' :"kham_la_do_virut",
        'cmd' :"kham_la_do_virut",
        'healthy':"khoe_manh"
    }

    name_pest_list_vn = {
        "chay_la" : "bệnh cháy lá",
        "benh_dom_mat" : "bệnh đốm mắt",
        "kham_la_do_virut" : "bệnh khảm lá do virut",
        "khoe_manh" : "cây khỏe mạnh"
    }

    # Lưu trữ các bệnh và xác suất tương ứng trong một danh sách
    disease_probabilities = []
    for i, probability in enumerate(class_probabilities):
        disease_name = class_names[i]
        disease_vn_name = name_pest_list_vn[name_pest_list[disease_name]]
        disease_probabilities.append({
            'name': disease_name,
            'vn_name': disease_vn_name,
            'probability': round(number=probability*100,ndigits=2) 
        })

    # Sắp xếp danh sách bệnh theo xác suất giảm dần
    disease_probabilities = sorted(disease_probabilities, key=lambda x: x['probability'], reverse=True)

    # Giới hạn số lượng bệnh trả về theo num_diseases
    disease_probabilities = disease_probabilities[:num_diseases]

    # In ra các bệnh và xác suất tương ứng
    for disease in disease_probabilities:
        print("Predicted class:", disease['name'])
        print("Tênbệnh:", name_pest_list[disease['name']])
        print("Tên bệnh (tiếng Việt):", disease['vn_name'])
        print("Xác suất:", disease['probability'])
        print()

    return disease_probabilities

# c = pest_diagnosis_with_pytorch_and_vit_model_and_acc_value_each_class_num_diseases(
#     num_diseases=3,
#     threshold=0.35,
#     url_img="https://iot-image.nextfarm.vn/avn/0902243822/1703135346934.png"
# )

def two_pests_diagnosis_with_pytorch_and_vit_model_and_acc_value_each_class(url_img,threshold):
    # Tải ảnh và tiền xử lý
    image = Image.open(requests.get(url_img, stream=True).raw)
    feature_extractor = ViTFeatureExtractor.from_pretrained('siddharth963/vit-base-patch16-224-in21k-finetuned-cassava', cache_dir="models/pytorch_model")
    inputs = feature_extractor(images=image, return_tensors="pt")

    # Tạo mô hình và dự đoán
    model = ViTForImageClassification.from_pretrained('siddharth963/vit-base-patch16-224-in21k-finetuned-cassava', cache_dir="models/pytorch_model")
    outputs = model(**inputs)
    logits = outputs.logits
    # print(logits)
    # print(logits[0])
    logits_list = logits[0].tolist()
    print(logits_list)
    class_names = [
        "cbb",
        "cbsd",
        "cgm",
        "cmd",
        "healthy"
    ]  # Thay thế bằng danh sách các tên lớp bệnh

    name_pest_list = {
    'cbb': "chay_la",
        'cbsd' : "benh_dom_mat",
        'cgm' :"kham_la_do_virut",
        'cmd' :"kham_la_do_virut",
        'healthy':"khoe_manh"
    }

    name_pest_list_vn = {
        "chay_la" : "bệnh cháy lá",
        "benh_dom_mat" : "bệnh đốm mắt",
        "kham_la_do_virut" : "bệnh khảm lá do virut",
        "khoe_manh" : "cây khỏe mạnh"
    }
    top_numbers,indices = get_the_values_and_positions6(logits_list=logits_list,nums=2)
    print(indices)
    disease_probabilities = []
    for i in range(len(indices)):
        predicted_class_confidence = logits[0, indices[i]].item()
        print(f"class : {indices[i]} , predicted_class_confidence = {predicted_class_confidence}")
        print(f"class name : {name_pest_list[class_names[indices[i]]]} , percent = {round(number=predicted_class_confidence,ndigits=2)}")
        if predicted_class_confidence > threshold:
            percent_predicted_class_confidence = ""
            if predicted_class_confidence >= acc_dicts[f"{indices[i]}"]:
                percent_predicted_class_confidence = 0.99
            elif predicted_class_confidence < acc_dicts[f"{indices[i]}"]:
                percent_predicted_class_confidence =  predicted_class_confidence / acc_dicts[f"{indices[i]}"]

            print("Predicted class:", indices[i])
            pest_name = name_pest_list[class_names[indices[i]]]
            print("ten benh:", pest_name)
            percent = round(ndigits=2,number=percent_predicted_class_confidence*100)
            print(f"percent = {percent}%")
            data_response = {
                "ten_benh":pest_name,
                "percent":percent
            }
            disease_probabilities.append(data_response)
            # return pest_name,percent
        else:
            print("Uncertain prediction")
            pest_name = "chua_xac_dinh"
            # nếu độ chắc chắn ( xác suất của class) trả về là số âm thì hiện chưa biết sử lý thế nào nên đẩy tậm về 70% là chưa xác định
            if predicted_class_confidence < 0 :
                percent_predicted_class_confidence = 0.5
            # percent_predicted_class_confidence = 0
            else:
                percent_predicted_class_confidence =  predicted_class_confidence / acc_dicts[f"{indices[i]}"]
            percent = round(ndigits=2,number=percent_predicted_class_confidence*100)
            print("ten benh:" ,pest_name)
            print(f"percent = {percent}%")
            # return predicted_class_name,percent_predicted_class_confidence
            data_response = {
                "ten_benh":pest_name,
                "percent":percent
            }
            disease_probabilities.append(data_response)
    return disease_probabilities
    
    

# g = two_pests_diagnosis_with_pytorch_and_vit_model_and_acc_value_each_class(
#     threshold=threshold,
#     url_img="https://iot-image.nextfarm.vn/avn/0902243822/1703135346934.png"
# )
# print("===================================================================")
# print(g)