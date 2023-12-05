import csv
import os
import shutil

def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("Isi file:")
            print(content)
    except FileNotFoundError:
        print(f"File tidak ditemukan: {file_path}")


def write_to_text_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data)
    print(f"Data berhasil ditulis ke dalam file: {file_path}")


def read_csv_file(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            print("Isi file CSV:")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"File tidak ditemukan: {file_path}")


def write_to_csv_file(file_path, data):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print(f"Data berhasil ditulis ke dalam file CSV: {file_path}")


def create_and_move_directory(source_file, target_directory):
    try:
        # Membuat direktori baru
        os.makedirs(target_directory, exist_ok=True)

        # Menyalin file ke dalam direktori baru
        shutil.copy(source_file, target_directory)

        # Memindahkan file ke direktori lain
        shutil.move(source_file, os.path.join(target_directory, os.path.basename(source_file)))

        print(f"File berhasil disalin dan dipindahkan ke: {target_directory}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")