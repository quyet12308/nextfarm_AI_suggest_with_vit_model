import csv

def write_data_log_to_csv_file(image_id, label, predicted_value_confidence, predicted_class):
    log_data = [image_id, label, predicted_value_confidence, predicted_class]

    with open('csv_folder/log_data_test_for_predicted_value_confidence_1500_img.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(log_data)

# write_data_log_to_csv_file(image_id="test.jpg",predicted_class=1,predicted_value_confidence=2.5,label=0)