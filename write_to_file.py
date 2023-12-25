def ghi_noi_dung_vao_file(file_name, text):
    try:
        with open(file_name, 'a',encoding='utf-8') as file:
            file.write(text)
            file.write('\n')  # Thêm dòng mới sau mỗi lần ghi nội dung
        print(f"Đã ghi nội dung vào {file_name} thành công.")
    except IOError:
        print(f"Có lỗi xảy ra khi ghi nội dung vào {file_name}.")