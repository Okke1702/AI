import os


def open_file(file_path):
    file_path = file_path.strip().strip('"')

    if not os.path.isfile(file_path):
        return f"Không tìm thấy file: {file_path}"

    try:
        os.startfile(file_path)
        return f"Đã mở file: {file_path}"

    except Exception as e:
        return f"Lỗi khi mở file: {e}"


def open_folder(folder_path):
    folder_path = folder_path.strip().strip('"')

    if not os.path.isdir(folder_path):
        return f"Không tìm thấy thư mục: {folder_path}"

    try:
        os.startfile(folder_path)
        return f"Đã mở thư mục: {folder_path}"

    except Exception as e:
        return f"Lỗi khi mở thư mục: {e}"