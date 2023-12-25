from transformers import ViTImageProcessor, ViTModel
from PIL import Image
import requests

url = 'https://iot-image.nextfarm.vn/avn/0902243822/1702373519673.png'
image = Image.open(requests.get(url, stream=True).raw)

processor = ViTImageProcessor.from_pretrained('siddharth963/vit-base-patch16-224-in21k-finetuned-cassava',cache_dir="models")
model = ViTModel.from_pretrained('siddharth963/vit-base-patch16-224-in21k-finetuned-cassava',cache_dir="models")
inputs = processor(images=image, return_tensors="pt")

outputs = model(**inputs)
last_hidden_states = outputs.last_hidden_state

print(outputs)
print(last_hidden_states)