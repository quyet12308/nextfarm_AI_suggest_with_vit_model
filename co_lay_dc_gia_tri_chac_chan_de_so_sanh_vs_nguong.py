import torch
import requests
from PIL import Image
from transformers import ViTFeatureExtractor, ViTForImageClassification

# Đường dẫn đến ảnh
url = 'https://iot-image.nextfarm.vn/avn/0902243822/1702373519673.png'

# Tải ảnh và tiền xử lý
image = Image.open(requests.get(url, stream=True).raw)
feature_extractor = ViTFeatureExtractor.from_pretrained('siddharth963/vit-base-patch16-224-in21k-finetuned-cassava', cache_dir="models")
inputs = feature_extractor(images=image, return_tensors="pt")

# Tạo mô hình và dự đoán
model = ViTForImageClassification.from_pretrained('siddharth963/vit-base-patch16-224-in21k-finetuned-cassava', cache_dir="models")
outputs = model(**inputs)
logits = outputs.logits
print(logits)
print(logits[0])
predicted_class_index = torch.argmax(logits, dim=1).item()
print(predicted_class_index)

predicted_class_confidence = logits[0, predicted_class_index].item()
print(predicted_class_confidence)
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
predicted_class_name = class_names[predicted_class_index]

# Kiểm tra ngưỡng
threshold = 0.35
# print(torch.max(torch.softmax(logits, dim=1)))
if predicted_class_confidence > threshold:
    print("Predicted class:", predicted_class_name)
    print("ten benh:", name_pest_list[predicted_class_name])
else:
    print("Uncertain prediction")
    print("ten benh:" ,"chua_xac_dinh")