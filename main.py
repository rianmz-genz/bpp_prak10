from my_module_10 import filesystem

# 1
file_path = 'example.txt'
filesystem.read_text_file(file_path)

# 2
data_to_write = "Hello World!"
filesystem.write_to_text_file(file_path, data_to_write)

# 3
file_csv = "save_the_bees.csv"
filesystem.read_csv_file(file_csv)

# 4
data_to_write_csv = [['Nama', 'Usia'], ['John', 25], ['Doe', 30]]
file_csv_to_write = "write.csv"
filesystem.write_to_csv_file(file_csv_to_write, data_to_write_csv)

# 5
source_file_path = 'example.txt'
target_directory_path = 'copyied'
filesystem.create_and_move_directory(source_file_path, target_directory_path)
