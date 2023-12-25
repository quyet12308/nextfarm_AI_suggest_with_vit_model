import torch
import requests
from PIL import Image
from transformers import ViTFeatureExtractor, ViTForImageClassification

# Đường dẫn đến ảnh
# url = 'https://iot-image.nextfarm.vn/avn/0902243822/1702373519673.png'
# url = 'https://iot-image.nextfarm.vn/avn/0919331088/1701394672218.png'
# url = 'https://iot-image.nextfarm.vn/avn/0919331088/1701394708249.png'
# url = 'https://iot-image.nextfarm.vn/avn/0902243822/1701655889047.png'
# url = 'https://iot-image.nextfarm.vn/avn/0902243822/1701656548717.png'
# url = 'https://iot-image.nextfarm.vn/avn/0902243822/1701656618605.png'
url = 'https://iot-image.nextfarm.vn/avn/0902243822/1701656620255.png'

# Tải ảnh và tiền xử lý
image = Image.open(requests.get(url, stream=True).raw)
feature_extractor = ViTFeatureExtractor.from_pretrained('siddharth963/vit-base-patch16-224-in21k-finetuned-cassava', cache_dir="models")
inputs = feature_extractor(images=image, return_tensors="pt")

# Tạo mô hình và dự đoán
model = ViTForImageClassification.from_pretrained('siddharth963/vit-base-patch16-224-in21k-finetuned-cassava', cache_dir="models")
outputs = model(**inputs)
logits = outputs.logits.squeeze(0)
print(logits)

# Thiết lập ngưỡng
threshold = 0.3

# In ra danh sách lớp bệnh dự đoán và xác suất tương ứng
class_names = [
    "CBB",
    "CBSD",
    "CGM",
    "CMD",
    "H"
]  # Thay thế bằng danh sách các tên lớp bệnh



for i in range(len(class_names)):
    if logits[i].item() < threshold:
        print(logits[i].item())
        predicted_class_name = "Chưa xác định"
        prob = 0.0
    else:
        print(logits[i].item())
        predicted_class_name = class_names[i]
        prob = torch.softmax(logits, dim=0)[i].item()
    print(f"{predicted_class_name}: {prob:.3f}")