import torch
import requests
from PIL import Image
from transformers import ViTFeatureExtractor, ViTForImageClassification

# Đường dẫn đến ảnh
url = 'https://iot-image.nextfarm.vn/avn/0902243822/1702373519673.png'

# Tải ảnh và tiền xử lý
image = Image.open(requests.get(url, stream=True).raw)
feature_extractor = ViTFeatureExtractor.from_pretrained('siddharth963/vit-base-patch16-224-in21k-finetuned-cassava',cache_dir="models")
inputs = feature_extractor(images=image, return_tensors="pt")

# Tạo mô hình và dự đoán
model = ViTForImageClassification.from_pretrained('siddharth963/vit-base-patch16-224-in21k-finetuned-cassava',cache_dir="models")
outputs = model(**inputs)
logits = outputs.logits
print(logits)
print(logits[0])
predicted_class_index = torch.argmax(logits, dim=1).item()
print(predicted_class_index)

# In ra tên class dự đoán
class_names = [
    "CBB",
    "CBSD",
    "CGM",
    "CMD",
    "H"
    ]  # Thay thế bằng danh sách các tên lớp bệnh
predicted_class_name = class_names[predicted_class_index]
print("Predicted class:", predicted_class_name)