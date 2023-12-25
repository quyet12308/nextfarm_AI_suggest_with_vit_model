import torch
import requests
from PIL import Image
from transformers import ViTFeatureExtractor, ViTForImageClassification

# Đường dẫn đến ảnh
# url = 'https://iot-image.nextfarm.vn/avn/0902243822/1702373519673.png'
url = "https://iot-image.nextfarm.vn/avn/0902243822/1702373111259.png"

def ai_suggest_labling_cassava(url):
    # Tải ảnh và tiền xử lý
    image = Image.open(requests.get(url, stream=True).raw)
    feature_extractor = ViTFeatureExtractor.from_pretrained('siddharth963/vit-base-patch16-224-in21k-finetuned-cassava', cache_dir="models")
    inputs = feature_extractor(images=image, return_tensors="pt")

    # Tạo mô hình và dự đoán
    model = ViTForImageClassification.from_pretrained('siddharth963/vit-base-patch16-224-in21k-finetuned-cassava', cache_dir="models")
    outputs = model(**inputs)
    logits = outputs.logits.squeeze(0)
    print(logits)
    print(type(logits))
    probabilities = torch.softmax(logits, dim=0)
    print(probabilities)
    # In ra danh sách lớp bệnh dự đoán và xác suất tương ứng
    class_names = [
        "CBB",
        "CBSD",
        "CGM",
        "CMD",
        "H"
    ]  # Thay thế bằng danh sách các tên lớp bệnh
    sorted_probabilities, sorted_indices = torch.sort(probabilities, descending=True)
    print(sorted_probabilities)
    print(sorted_indices)

    # return data


    for prob, idx in zip(sorted_probabilities, sorted_indices):
        class_name = class_names[idx]
        print(f"{class_name}: {prob.item():.3f}")


ai_suggest_labling_cassava(url=url)