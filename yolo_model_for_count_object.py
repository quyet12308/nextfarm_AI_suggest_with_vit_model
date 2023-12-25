from ultralytics import YOLO
import numpy as np
import requests

from io import BytesIO
from PIL import Image

import PIL.Image as Image

def count_la_khoai_mi_with_url(url):
    
    # define the model
    model = YOLO('models/model_yolo_for_count_cassava.pt')
    image = Image.open(requests.get(url, stream=True).raw)
    # run inference on the source image
    # results = model('images/1702452877119.png')
    results = model(image)
    # get the model names list
    names = model.names
    # get the 'car' class id
    car_id = list(names)[list(names.values()).index('la_khoai_mi')]
    # count 'car' objects in the results
    count = results[0].boxes.cls.tolist().count(car_id)
    print(count)
    return count

