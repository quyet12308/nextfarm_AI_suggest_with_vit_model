import csv

def read_csv_line_by_line_new_dataset(file_path):
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield row['image_id'], row['label']

def read_csv_and_return_two_list(file_path):
    image_ids = []
    labels = []

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            image_ids.append(row['image_id'])
            labels.append(row['label'])

    return image_ids, labels


def analyze_predictions(file_path):
    # Khởi tạo các biến đếm và giá trị tối đa/tối thiểu ban đầu
    class_counts = {}  # Số lượng dự đoán cho từng class
    correct_counts = {}  # Số lượng dự đoán chính xác cho từng class
    incorrect_counts = {}  # Số lượng dự đoán sai cho từng class
    max_confidence_correct = {}  # Độ chắc chắn lớn nhất của dự đoán đúng cho từng class
    min_confidence_correct = {}  # Độ chắc chắn bé nhất của dự đoán đúng cho từng class
    max_confidence_incorrect = {}  # Độ chắc chắn lớn nhất của dự đoán sai cho từng class
    min_confidence_incorrect = {}  # Độ chắc chắn bé nhất của dự đoán sai cho từng class

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            image_id = row['image_id']
            label = row['label']
            predicted_value_confidence = float(row['predicted_value_confidence'])
            predicted_class = row['predicted_class']

            # Cập nhật số lượng dự đoán cho từng class
            if predicted_class in class_counts:
                class_counts[predicted_class] += 1
            else:
                class_counts[predicted_class] = 1

            # Cập nhật số lượng dự đoán chính xác và sai cho từng class
            if label == predicted_class:
                if predicted_class in correct_counts:
                    correct_counts[predicted_class] += 1
                else:
                    correct_counts[predicted_class] = 1

                # Cập nhật độ chắc chắn lớn nhất và bé nhất của dự đoán đúng
                if predicted_class in max_confidence_correct:
                    max_confidence_correct[predicted_class] = max(max_confidence_correct[predicted_class], predicted_value_confidence)
                else:
                    max_confidence_correct[predicted_class] = predicted_value_confidence

                if predicted_class in min_confidence_correct:
                    min_confidence_correct[predicted_class] = min(min_confidence_correct[predicted_class], predicted_value_confidence)
                else:
                    min_confidence_correct[predicted_class] = predicted_value_confidence
            else:
                if predicted_class in incorrect_counts:
                    incorrect_counts[predicted_class] += 1
                else:
                    incorrect_counts[predicted_class] = 1

                # Cập nhật độ chắc chắn lớn nhất và bé nhất của dự đoán sai
                if predicted_class in max_confidence_incorrect:
                    max_confidence_incorrect[predicted_class] = max(max_confidence_incorrect[predicted_class], predicted_value_confidence)
                else:
                    max_confidence_incorrect[predicted_class] = predicted_value_confidence

                if predicted_class in min_confidence_incorrect:
                    min_confidence_incorrect[predicted_class] = min(min_confidence_incorrect[predicted_class], predicted_value_confidence)
                else:
                    min_confidence_incorrect[predicted_class] = predicted_value_confidence

    # Tính toán tỷ lệ chính xác và in kết quả
    accuracy_rates = {}
    for class_label in class_counts.keys():
        total_predictions = class_counts[class_label]
        correct_predictions = correct_counts.get(class_label, 0)
        accuracy_rates[class_label] = correct_predictions / total_predictions if total_predictions > 0 else 0.0

    return accuracy_rates, incorrect_counts, max_confidence_correct, min_confidence_correct, max_confidence_incorrect, min_confidence_incorrect

# a = read_csv_and_return_two_list(file_path="csv_folder/new_dataset.csv")
# print(a)

# for image_id, label in read_csv_line_by_line_new_dataset(r'csv_folder\new_dataset.csv'):
#     print(image_id)
#     print(label)

b = analyze_predictions(file_path=f"csv_folder/log_data_test_for_predicted_value_confidence_1500_img.csv")
# print(b)
accuracy_rates, incorrect_counts, max_confidence_correct, min_confidence_correct, max_confidence_incorrect, min_confidence_incorrect = b

print("accuracy_rates = " + str(accuracy_rates) )
print("incorrect_counts = " + str(incorrect_counts) )
print("max_confidence_correct = " + str(max_confidence_correct) )
print("min_confidence_correct = " + str(min_confidence_correct) )
print("max_confidence_incorrect = " + str(max_confidence_incorrect) )
print("min_confidence_incorrect = " + str(min_confidence_incorrect) )