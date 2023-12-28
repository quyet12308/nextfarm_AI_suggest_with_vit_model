from vit_model_cassava import pest_diagnosis_with_pytorch_and_vit_model_using_local_path_image
from write_data_log_for_csv_file import write_data_log_to_csv_file
from read_csv_file import read_csv_and_return_two_list,read_csv_line_by_line_new_dataset
from write_error_log import write_to_file,write_to_file2
from setting import threshold

for image_id, label in read_csv_line_by_line_new_dataset(r'csv_folder\new_dataset.csv'):
    try:
        new_path = f"C:/Users/Lenovo/Downloads/cassava_dataset3_3gb/train/" 
        # print(image_id)
        new_path_2 = f"{new_path}{image_id}"
        # print(new_path_2)
        predicted_class_name,predicted_class_confidence,predicted_class_index = pest_diagnosis_with_pytorch_and_vit_model_using_local_path_image(
             local_path=f"{new_path_2}",
             threshold=threshold

        )
        # print(label)
        write_data_log_to_csv_file(image_id=image_id,label=label,predicted_class=predicted_class_index,predicted_value_confidence=predicted_class_confidence)
    except Exception as e:
            # Xử lý ngoại lệ (lỗi)
            # print(f"Lỗi xử lý URL : {str(e)}")
            write_to_file(
                error=f"{str(e)}",
                filename="text_folder/error_log_from_predict_AI_model.txt"
            )

