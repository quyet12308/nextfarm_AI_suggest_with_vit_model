import os
import pandas as pd

def analyze_dataset(dataset_folder, labels_file):
    # Đếm số lượng ảnh trong thư mục
    image_count = len(os.listdir(dataset_folder))
    print("Tổng số ảnh trong thư mục:", image_count)

    # Đọc file csv gán nhãn
    labels_df = pd.read_csv(labels_file)

    # Đếm số lượng ảnh cho từng lớp
    class_counts = labels_df['label'].value_counts()
    print("Số lượng ảnh từng lớp:")
    print(class_counts)

# Sử dụng hàm analyze_dataset
# dataset_folder = r"C:\Users\Lenovo\Downloads\cassava_dataset3_3gb\train"
# labels_file = r"C:\Users\Lenovo\Downloads\cassava_dataset3_3gb\merged.csv"
# analyze_dataset(dataset_folder, labels_file)
    

def balance_dataset(original_csv_file, output_csv_file, target_count=300):
    # Đọc file CSV ban đầu
    original_df = pd.read_csv(original_csv_file)

    # Tạo một DataFrame rỗng để lưu tập dữ liệu cân bằng
    balanced_df = pd.DataFrame(columns=['image_id', 'label'])

    # Duyệt qua từng lớp
    for label in original_df['label'].unique():
        # Lấy các ảnh của lớp hiện tại
        label_images = original_df[original_df['label'] == label]

        # Lấy tối đa target_count ảnh từ lớp hiện tại
        sampled_images = label_images.sample(n=min(target_count, len(label_images)), random_state=42)

        # Thêm các ảnh đã lấy vào DataFrame cân bằng
        balanced_df = balanced_df._append(sampled_images)

    # Ghi DataFrame cân bằng vào file CSV mới
    balanced_df.to_csv(output_csv_file, index=False)

# Sử dụng hàm balance_dataset
original_csv_file = r"C:\Users\Lenovo\Downloads\cassava_dataset3_3gb\merged.csv"
output_csv_file = r"csv_folder\new_dataset.csv"
balance_dataset(original_csv_file, output_csv_file)