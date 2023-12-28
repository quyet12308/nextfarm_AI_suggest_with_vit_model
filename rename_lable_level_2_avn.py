import requests
from security_info import tokens
import json

def labling_dataset_lavel2(
    id,tag_name_level2,tag_name_level2_predict_1,
    tag_name_level2_predict_percent_1,tag_name_level2_predict_2=None,tag_name_level2_predict_percent_2=None):

  url2 = f"  https://api.nextfarm.vn/api/ajinomoto/ai/labelling/{id}"
  token2 = tokens["token_avn_ajinomoto"]

  data_for_post_form = {
    "tag_name_level2":tag_name_level2,
    # "pic_url": url_img
    "tag_name_level2_predict_1":tag_name_level2_predict_1,
    "tag_name_level2_predict_2":tag_name_level2_predict_2,
    "tag_name_level2_predict_percent_1":tag_name_level2_predict_percent_1,
    "tag_name_level2_predict_percent_2":tag_name_level2_predict_percent_2

  }

  headers2 = {
    "Authorization": f"Bearer {token2}"
  }
  data_test_json = data_for_post_form
  print(data_test_json)
  print(type(data_test_json))
  response = requests.put(url2, headers=headers2, data=data_test_json)
  return response

# a = labling_dataset_lavel2(
  
#   id=11037,
#   tag_name_level2="kham_la_do_virut",
#   tag_name_level2_predict_1="kham_la_do_virut",
#   tag_name_level2_predict_percent_1=80.69,
#   tag_name_level2_predict_2="chay_la",
#   tag_name_level2_predict_percent_2=60
#   )

# # Kiểm tra mã trạng thái HTTP
# status_code = a.status_code
# print("Status code:", status_code)

# # Kiểm tra nội dung phản hồi
# response_data = a.json()
# print("Response data:", response_data)
# print(type(response_data))